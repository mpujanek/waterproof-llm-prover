from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

PRICING = {
        "anthropic/claude-3.7-sonnet": {"input": 3.0, "output": 15.0},
        "anthropic/claude-sonnet-4": {"input": 3.0, "output": 15.0},
        "anthropic/claude-3.7-sonnet:thinking": {"input": 3.0, "output": 15.0},
        "openai/o4-mini": {"input": 1.1, "output": 4.4},
        "openai/o3": {"input": 10.0, "output": 40.0},
        "openai/o3-mini": {"input": 1.1, "output": 4.4},
        "openai/o1": {"input": 15.0, "output": 60.0},
        "openai/o1-mini": {"input": 1.1, "output": 4.4},
        "openai/o1-pro": {"input": 150.0, "output": 600.0},
        "google/gemini-2.5-flash-preview-05-20": {"input": 0.15, "output": 0.60},
        "google/gemini-2.5-flash-preview-05-20:thinking": {"input": 0.15, "output": 0.60},
        "google/gemini-2.5-pro-preview": {"input": 1.25, "output": 10.0}
}


def call_api(model, input):
    output = {}

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": input
            }
        ]
    )

    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens

    response_text = completion.choices[0].message.content

    output["output"] = response_text
    output["input_tokens"] = prompt_tokens
    output["output_tokens"] = completion_tokens
    output["token_count"] = prompt_tokens + completion_tokens
    output["cost"] = estimate_cost(model, prompt_tokens, completion_tokens)
    output["thinking_mode"] = True

    print(response_text)
    print(output)

    return output

def estimate_cost(model_name, input_tokens, output_tokens):
    # Pricing in USD per 1M tokens (as of early 2025, change if outdated)
    
    model_price = PRICING.get(model_name)
    if not model_price:
        return None
    
    input_cost = (input_tokens / 1000000) * model_price["input"]
    output_cost = (output_tokens / 1000000) * model_price["output"]
    
    return input_cost + output_cost