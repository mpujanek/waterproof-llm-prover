from exercise_parser import parse
from prompt_composer import compose
from api_caller import call_api
from proof_compiler import compile_output
from json_exporter import export_json

## STEP 1: Specify models to test

# List of models to choose from (put chosen ones in "models" variable)
supported_models = ["o4-mini", "o3", "o3-mini", "o1", "o1-mini", "o1-pro", "claude-3-7-sonnet", "claude-3-7-sonnet-thinking"]

models = ["o3-mini"]


## STEP 2: Specify what exercises to test on
# Input a list of strings of the format "3.11.2" where 3 is the chapter name,
# 11 is the subchapter name, and 2 is the number of the exercise
# Input "all" if you want to test models on all exercises

exercise_numbers = []


## STEP 3: Specify prompt and provide a syntax tutorial
# These are loaded from files in this directory. 

prompt_filename = "generic_wp_prompt.txt"
tutorial_filename = "tutorial.txt"


## STEP 3: Specify folder to store results
# Define below a master folder (in this directory) in which the test results will be stored.
# Each test run will have its results stored in a new folder within the specified folder.

directory = "responses"


## Run tests

def run(models, exercise_numbers, prompt_filename, tutorial_filename):
    # Check that all chosen models are supported
    for model in models:
        if model not in supported_models:
            print(f"Unsupported model specified: {model}")
            return

    # Parse exercise sheets to extract desired exercises 
    # Returns dict with exercise numbers as keys and content as values
    exercises = parse(exercise_numbers)

    # Compose prompt from given files
    prompt = compose(prompt_filename, tutorial_filename)

    # Run all models on all exercises, export output
    for exercise in exercises:
        # Concatenate exercise to the prompt
        input = prompt + "\n" + exercises[exercise]

        for model in models:
            # Call APIs of given model with input
            output = call_api(model, input)

            # Compile response to check if proof is correct
            proof_result = compile_output(output["output"])

            # Export result to JSON
            export_json(model, exercise, output, proof_result, directory)

run(models, exercise_numbers, prompt_filename, tutorial_filename)