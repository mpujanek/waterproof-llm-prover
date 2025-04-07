from openai import OpenAI
from anthropic import Anthropic

def estimate_anthropic_cost(model_name, prompt_tokens, completion_tokens):
    # Pricing in USD per 1M tokens (as of early 2025, change if outdated)
    pricing = {
        "claude-3-opus-20240229": {"input": 15.0, "output": 75.0},
        "claude-3-7-sonnet-20250219": {"input": 3.0, "output": 15.0},
        "claude-3-5-haiku-20241022": {"input": 0.8, "output": 4.0}
    }
    
    model_price = pricing.get(model_name)
    if not model_price:
        raise ValueError("Unknown model: {}".format(model_name))
    
    input_cost = (prompt_tokens / 1000000) * model_price["input"]
    output_cost = (completion_tokens / 1000000) * model_price["output"]
    
    return input_cost + output_cost

def configure_thinking(enable_extended_thinking: bool, token_budget: int = 1000):
    if enable_extended_thinking:
        return {"type": "enabled", "budget_tokens": token_budget}
    else:
        return {"type": "disabled"}

#openai_client = OpenAI()
anthropic_client = Anthropic()

with open("tutorial.txt", "r") as file:
    tutorial = file.read()

with open("generic_wp_prompt.txt", "r") as file:
    generic_prompt = file.read()

prompt = generic_prompt + tutorial

proof = """
Variable f : ℝ → ℝ.
Variable g : ℝ → ℝ.

Lemma exercise_3_11_4 :
  (∀ M1 ∈ ℝ, ∃ y > 0, ∀ x > y, f (x) > M1) ⇒
    (∀ M2 < 4, ∃ z > 0, ∀ x > z, g (x) > M2) ⇒
      ∃ c ∈ ℝ, f(c) + g(c) > 10.
Proof.
"""

input = prompt + proof

thinking = True

def response_openai():
    response = openai_client.responses.create(
        model="o1",
        input=input
    )
    print(response.output_text)

def response_anthropic():
    model = "claude-3-7-sonnet-20250219"

    message = anthropic_client.messages.create(
        model=model,
        max_tokens=20000,
        thinking = configure_thinking(thinking, 16000),
        messages=[
            {"role": "user", "content": input}
        ]
    )

    text = next(item.text for item in message.content if item.type == "text")

    prompt_tokens = message.usage.input_tokens
    completion_tokens = message.usage.output_tokens

    cost = estimate_anthropic_cost(model, prompt_tokens, completion_tokens)

    return text, cost

#response_openai()
#response_anthropic()

def export_result_anthropic():
    text, cost = response_anthropic()

    results = f"""## Prompt:\n
    {generic_prompt}\n
    <tutorial.txt>\n
    {proof}\n
    ## Response:\n
    {text}\n
    ## Comments:\n
    Thinking: {"yes" if thinking else "no"}
    Cost: {cost}
    """

    with open("result.txt", "w") as file:
        file.write(results)

export_result_anthropic()