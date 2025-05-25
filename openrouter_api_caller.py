from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import os

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

PRICING = {
        "qwen/qwen3-235b-a22b": {"input": 0.14, "output": 0.60, "thinking": True},
        "qwen/qwq-32b:free": {"input": 0.15, "output": 0.20, "thinking": True},
        "qwen/qwen-2.5-72b-instruct": {"input": 0.12, "output": 0.39, "thinking": False},
        "anthropic/claude-3.7-sonnet:thinking": {"input": 3.0, "output": 15.0, "thinking": True},
        "anthropic/claude-3.7-sonnet": {"input": 3.0, "output": 15.0, "thinking": False},
        "anthropic/claude-sonnet-4": {"input": 3.0, "output": 15.0, "thinking": False},
        "deepseek/deepseek-r1:free": {"input": 0.5, "output": 2.18, "thinking": True},
        "deepseek/deepseek-prover-v2:free": {"input": 0.5, "output": 2.18, "thinking": False},
        "deepseek/deepseek-chat-v3-0324:free": {"input": 0.3, "output": 0.88, "thinking": False},
        "x-ai/grok-3-mini-beta": {"input": 0.30, "output": 0.50, "thinking": True},
        "openai/o4-mini": {"input": 1.1, "output": 4.4, "thinking": True},
        "openai/o3-mini": {"input": 1.1, "output": 4.4, "thinking": True},
        "openai/o1-mini": {"input": 1.1, "output": 4.4, "thinking": True},
        "google/gemini-2.5-flash-preview-05-20": {"input": 0.15, "output": 0.60, "thinking": False},
        "google/gemini-2.5-flash-preview-05-20:thinking": {"input": 0.15, "output": 0.60, "thinking": True},
        "meta-llama/llama-3.3-70b-instruct": {"input": 0.07, "output": 0.25, "thinking": False},
        "nousresearch/hermes-3-llama-3.1-405b": {"input": 0.70, "output": 0.80, "thinking": False},
        "nousresearch/hermes-3-llama-3.1-70b": {"input": 0.12, "output": 0.30, "thinking": False},
        "meta-llama/llama-4-maverick": {"input": 0.16, "output": 0.60, "thinking": False},
}

# Map OpenRouter models to closest known OpenAI tokenizer
TOKENIZER_MAP = {
    "openai/o4-mini": "gpt-4",
    "openai/o3-mini": "gpt-4",
    "openai/o1-mini": "gpt-4",
    "anthropic/claude-3.7-sonnet": "gpt-4",
    "anthropic/claude-3.7-sonnet:thinking": "gpt-4",
    "anthropic/claude-sonnet-4": "gpt-4",
    "deepseek/deepseek-prover-v2:free": "gpt-3.5-turbo",
    "deepseek/deepseek-chat-v3-0324:free": "gpt-3.5-turbo",
    "deepseek/deepseek-r1:free": "gpt-3.5-turbo",
    "meta-llama/llama-3.3-70b-instruct": "cl100k_base",
    "meta-llama/llama-4-maverick": "cl100k_base",
    "x-ai/grok-3-mini-beta": "cl100k_base",
    "qwen/qwen3-235b-a22b": "cl100k_base",
    "qwen/qwen-2.5-72b-instruct": "cl100k_base",
    "google/gemini-2.5-flash-preview-05-20": "gpt-3.5-turbo",
    "google/gemini-2.5-flash-preview-05-20:thinking": "gpt-3.5-turbo",
    "nousresearch/hermes-3-llama-3.1-70b": "cl100k_base",
    "nousresearch/hermes-3-llama-3.1-405b": "cl100k_base",
}


def call_api(model, history):

    completion = client.chat.completions.create(
        model=model,
        messages=history,
    )

    output = extract_data(completion, model)

    return output

def extract_data(completion, model):
    output = {}

    response_text = completion.choices[0].message.content # does not include thinking

    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens # includes thinking + response

    if PRICING.get(model).get("thinking"):
        output_tokens = count_tokens(response_text, model)
        thinking_tokens = completion_tokens - output_tokens
        output["thinking_tokens"] = thinking_tokens
        output["output_tokens"] = output_tokens
    else: 
        output["thinking_tokens"] = 0
        output["output_tokens"] = completion_tokens

    output["input_tokens"] = prompt_tokens
    output["output"] = response_text
    output["token_count"] = output["input_tokens"] + output["thinking_tokens"] + output["output_tokens"]
    output["cost"] = estimate_cost(model, prompt_tokens, completion_tokens)
    output["thinking_mode"] = PRICING.get(model).get("thinking")

    print(response_text)
    print(output)
    print(completion_tokens)

    return output

def estimate_cost(model_name, input_tokens, output_tokens):
    model_price = PRICING.get(model_name)
    if not model_price:
        return None
    
    input_cost = (input_tokens / 1000000) * model_price["input"]
    output_cost = (output_tokens / 1000000) * model_price["output"]
    
    return input_cost + output_cost

def count_tokens(text, model_name):
    tokenizer_name = TOKENIZER_MAP.get(model_name, "cl100k_base")
    try:
        enc = tiktoken.encoding_for_model(tokenizer_name)
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))