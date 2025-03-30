from openai import OpenAI
client = OpenAI()

with open("tutorial.txt", "r") as file:
    tutorial = file.read()

with open("generic_wp_prompt.txt", "r") as file:
    prompt = file.read()

instruct = prompt + tutorial

with open("proof.txt", "r") as file:
    input_text = file.read()

response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
