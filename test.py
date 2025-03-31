from openai import OpenAI
from anthropic import Anthropic

openai_client = OpenAI()
anthropic_client = Anthropic()

with open("tutorial.txt", "r") as file:
    tutorial = file.read()

with open("generic_wp_prompt.txt", "r") as file:
    prompt = file.read()

prompt = prompt + tutorial

proof = """
Lemma exercise_3_11_2 :
  ∀ x ∈ ℝ,
    ∃ y ∈ ℝ,
      ∀ u > 0,
          ∃ v > 0, x + u < y + v.
Proof.
"""

prompt = prompt + proof

def print_openai():
    response = openai_client.responses.create(
        model="o1",
        input=prompt
    )
    print(response.output_text)

def print_anthropic():
    message = anthropic_client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=20000,
        thinking={
            "type": "enabled",
            "budget_tokens": 16000
        },
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = next(item.text for item in message.content if item.type == "text")


    print(text)

print_openai()
#print_anthropic()
