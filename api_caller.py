from openai import OpenAI
from anthropic import Anthropic

openai_client = OpenAI()
anthropic_client = Anthropic()

openai_models = ["o4-mini", "o3", "o3-mini", "o1", "o1-mini", "o1-pro"]
anthropic_models = ["claude-3-7-sonnet", "claude-3-7-sonnet-thinking"]

def call_api(model, input):
    response = None

    if model in openai_models:
        response = response_openai(model=model, input=input)
    elif model in anthropic_models:
        response = response_anthropic(model=model, input=input)

    return response


def response_openai(model, input):
    output = {}

    response = openai_client.responses.create(
        model=model,
        input=input
    )

    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens

    output["solution"] = response.output_text
    output["token_count"] = prompt_tokens + completion_tokens
    output["cost"] = estimate_cost(model, prompt_tokens, completion_tokens)
    output["thinking_mode"] = (model == "claude-3-7-sonnet-thinking")

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

    prompt_tokens = response.usage.input_tokens
    completion_tokens = response.usage.output_tokens

    output["solution"] = next(item.text for item in response.content if item.type == "text")
    output["token_count"] = prompt_tokens + completion_tokens
    output["cost"] = estimate_cost(model, prompt_tokens, completion_tokens)
    output["thinking_mode"] = True

    return output


def configure_thinking(model, token_budget: int = 1000):
    if model == "claude-3-7-sonnet-thinking":
        return {"type": "enabled", "budget_tokens": token_budget}
    else:
        return {"type": "disabled"}


def estimate_cost(model_name, prompt_tokens, completion_tokens):
    # Pricing in USD per 1M tokens (as of early 2025, change if outdated)
    pricing = {
        "claude-3-7-sonnet": {"input": 3.0, "output": 15.0},
        "claude-3-7-sonnet-thinking": {"input": 3.0, "output": 15.0},
        "o4-mini": {"input": 1.1, "output": 4.4},
        "o3": {"input": 10.0, "output": 40.0},
        "o3-mini": {"input": 1.1, "output": 4.4},
        "o1": {"input": 15.0, "output": 60.0},
        "o1-mini": {"input": 1.1, "output": 4.4},
        "o1-pro": {"input": 150.0, "output": 600.0}
    }
    
    model_price = pricing.get(model_name)
    if not model_price:
        raise ValueError("Unknown model: {}".format(model_name))
    
    input_cost = (prompt_tokens / 1000000) * model_price["input"]
    output_cost = (completion_tokens / 1000000) * model_price["output"]
    
    return input_cost + output_cost