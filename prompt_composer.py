

def compose(prompt_filename, tutorial_filename, defs_no_context):
    with open(prompt_filename, "r") as file:
        no_tutorial_prompt = file.read()

    with open(tutorial_filename, "r") as file:
        tutorial = file.read()

    full_prompt = no_tutorial_prompt.replace("***tutorial***", tutorial)

    if defs_no_context:
        with open("all_definitions.txt", "r") as file:
            defs = file.read()
        full_prompt = full_prompt.replace("***definitions***", defs)

    return no_tutorial_prompt, full_prompt, tutorial

def compose_revision(revision_filename, proof_errors, line_with_error):
    with open(revision_filename, "r") as file:
        revision_prompt = file.read()

    error_message = proof_errors + "Line with error:\n" + line_with_error

    full_prompt = revision_prompt.replace("***message***", error_message)

    return full_prompt