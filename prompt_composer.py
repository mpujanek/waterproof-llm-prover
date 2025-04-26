

def compose(prompt_filename, tutorial_filename):
    with open(prompt_filename, "r") as file:
        generic_prompt = file.read()

    with open(tutorial_filename, "r") as file:
        tutorial = file.read()

    return generic_prompt, tutorial