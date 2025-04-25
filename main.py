from exercise_parser import parse
from prompt_composer import compose
from api_caller import call_api
from proof_compiler import compile_output
from json_exporter import export_json

## STEP 1: Specify models to test

# List of models to choose from (put chosen ones in "models" variable)
supported_models = []

models = []


## STEP 2: Specify what exercises to test on
# Input a list of strings of the format "3.11.2" where 3 is the chapter name,
# 11 is the subchapter name, and 2 is the number of the exercise
# Input "all" if you want to test models on all exercises

exercise_numbers = []


## STEP 3: Specify prompt and provide a syntax tutorial
# These are loaded from files in this directory. 

prompt_filename = "generic_wp_prompt.txt"
tutorial_filename = "tutorial.txt"


## Run tests

def run(models, exercise_numbers, prompt_filename, tutorial_filename):
    # Check that all chosen models are supported
    for model in models:
        if model not in supported_models:
            print(f"Unsupported model specified: {model}")
            return

    # Parse exercise sheets to extract desired exercises
    exercises = parse(exercise_numbers)

    # Compose prompt from given files
    prompt = compose(prompt_filename, tutorial_filename)

    # Run all models on all exercises, export output
    for exercise in exercises:
        # Concatenate exercise to the prompt
        input = prompt + "\n" + exercise

        for model in models:
            # Call APIs of given model with input
            response = call_api(model, input)

            # Compile response to check if proof is correct
            result = compile_output(response)

            # Export result to JSON
            export_json(result)

run(models, exercise_numbers, prompt_filename, tutorial_filename)