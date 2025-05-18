from openai import OpenAI
from anthropic import Anthropic
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")

openai_client = OpenAI(api_key=openai_key)
anthropic_client = Anthropic(api_key=anthropic_key)
gemini_client = genai.Client(api_key=google_key)

openai_models = ["o4-mini", "o3", "o3-mini", "o1", "o1-mini", "o1-pro"]
anthropic_models = ["claude-3-7-sonnet", "claude-3-7-sonnet-thinking"]
google_models = ["gemini-2.5-flash-preview-04-17", "gemini-2.5-pro-preview-05-06"]

def call_api(model, input):
    print(f"Calling API for {model}...")

    response = None

    if model in openai_models:
        response = response_openai(model=model, input=input)
    elif model in anthropic_models:
        response = response_anthropic(model=model, input=input)
    elif model in google_models:
        response = response_google(model=model, input=input)

    return response


def response_openai(model, input):
    output = {}

    response = openai_client.responses.create(
        model=model,
        input=input
    )

    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens

    output["output"] = response.output_text
    output["input_tokens"] = input_tokens
    output["output_tokens"] = output_tokens
    output["token_count"] = input_tokens + output_tokens
    output["cost"] = estimate_cost(model, input_tokens, output_tokens)
    output["thinking_mode"] = True

    return output


def response_anthropic(model, input):
    output = {}

    response = anthropic_client.messages.create(
        model=model,
        max_tokens=20000,
        thinking = configure_thinking(model, 16000),
        messages=[
            {"role": "user", "content": input}
        ]
    )

    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens

    output["output"] = next(item.text for item in response.content if item.type == "text")
    output["input_tokens"] = input_tokens
    output["output_tokens"] = output_tokens
    output["token_count"] = input_tokens + output_tokens
    output["cost"] = estimate_cost(model, input_tokens, output_tokens)
    output["thinking_mode"] = (model == "claude-3-7-sonnet-thinking")

    return output

def response_google(model, input):
    output = {}

    response = gemini_client.models.generate_content(
        model=model,
        contents=[{"role": "user", "parts": [{"text": input}]}]
    )

    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count

    output["output"] = response.candidates[0].content.parts[0].text
    output["input_tokens"] = input_tokens
    output["output_tokens"] = output_tokens
    output["token_count"] = input_tokens + output_tokens
    output["cost"] = estimate_cost(model, input_tokens, output_tokens)
    output["thinking_mode"] = (model == "gemini-2.5-flash")  # only Flash has thinking tiers

    return output


def configure_thinking(model, token_budget: int = 1000):
    if model == "claude-3-7-sonnet-thinking":
        return {"type": "enabled", "budget_tokens": token_budget}
    else:
        return {"type": "disabled"}


def estimate_cost(model_name, input_tokens, output_tokens):
    # Pricing in USD per 1M tokens (as of early 2025, change if outdated)
    pricing = {
        "claude-3-7-sonnet": {"input": 3.0, "output": 15.0},
        "claude-3-7-sonnet-thinking": {"input": 3.0, "output": 15.0},
        "o4-mini": {"input": 1.1, "output": 4.4},
        "o3": {"input": 10.0, "output": 40.0},
        "o3-mini": {"input": 1.1, "output": 4.4},
        "o1": {"input": 15.0, "output": 60.0},
        "o1-mini": {"input": 1.1, "output": 4.4},
        "o1-pro": {"input": 150.0, "output": 600.0},
        "gemini-2.5-flash-preview-04-17": {"input": 0.15, "output": 0.60},
        "gemini-2.5-pro-preview-05-06": {"input": 1.25, "output": 10.0}
    }
    
    model_price = pricing.get(model_name)
    if not model_price:
        raise ValueError("Unknown model: {}".format(model_name))
    
    input_cost = (input_tokens / 1000000) * model_price["input"]
    output_cost = (output_tokens / 1000000) * model_price["output"]
    
    return input_cost + output_cost