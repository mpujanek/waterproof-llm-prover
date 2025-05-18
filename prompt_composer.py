

def compose(prompt_filename, tutorial_filename):
    with open(prompt_filename, "r") as file:
        no_tutorial_prompt = file.read()

    with open(tutorial_filename, "r") as file:
        tutorial = file.read()

    full_prompt = no_tutorial_prompt.replace("%tutorial%", tutorial)

    return no_tutorial_prompt, full_prompt