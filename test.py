from openai import OpenAI
client = OpenAI()

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

response = client.responses.create(
    model="o3-mini",
    input=prompt
)

print(response.output_text)
