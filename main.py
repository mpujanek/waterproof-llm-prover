from exercise_parser import parse, clean
from prompt_composer import compose
from api_caller import call_api
from proof_compiler import compile_output
from json_exporter import export_json, make_folder

## STEP 1: Specify models to test

# List of models to choose from (put chosen ones in "models" variable)
supported_models = [
    "o4-mini", "o3", "o3-mini", "o1", "o1-mini", "o1-pro",
    "claude-3-7-sonnet", "claude-3-7-sonnet-thinking",
    "gemini-2.5-flash-preview-04-17", "gemini-2.5-pro-preview-05-06"
]

models = ["o4-mini"]


## STEP 2: Specify what exercises to test on
# Input a list of strings of the format "3_11_2" where 3 is the chapter name,
# 11 is the subchapter name, and 2 is the number of the exercise
# Input "all" if you want to test models on all exercises

all_exercises = [
    "2_non_degenerate_1", "2_non_degenerate_2",
    "2_positive_1", "2_positive_2",
    "2_reflexive_1", "2_reflexive_2",
    "2_symmetric_1", "2_symmetric_2",
    "2_triangle_inequality_1", "2_triangle_inequality_2",
    "3_11_1", "3_11_2", "3_11_4",
    "4_9_1", "4_9_2", "4_9_3",
    "5_9_1", "5_9_2",
    "6_8_1", "6_8_2",
    "10_7_3",
    "10_7_6", "10_7_intermediate",
    "11_not_closed", "11_not_open",
    "13_11_2", "13_11_3"
]

exercise_numbers = ["2_non_degenerate_2"]


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
    exercises, imports = parse(exercise_numbers)

    # Compose prompt from given files
    generic_prompt, tutorial = compose(prompt_filename, tutorial_filename)
    prompt = generic_prompt + tutorial

    # Make a folder in the specified directory for storing results of this run
    folder_path = make_folder(directory)

    # Run all models on all exercises, export output
    for exercise in exercises:
        # Concatenate exercise to the prompt
        input = prompt + "\n" + exercises[exercise]

        for model in models:
            # Call APIs of given model with input
            output = call_api(model, input)

            # Extract the LLM's proof attempt
            proof_attempt = output["output"]

            # Clean output before compiling (remove leading/trailing "Proof."/"Qed.")
            proof_attempt = clean(proof_attempt)

            # Compile response to check if proof is correct
            proof_result, line_with_error = compile_output(proof_attempt, imports[exercise], exercises[exercise], exercise)

            # Export result to JSON (tutorial is big so it is not included in JSON)
            export_json(model, exercise, exercises, generic_prompt, output, proof_result, folder_path, line_with_error)


proof = """
Take x ∈ ℝ.
We need to show that (∃ y ∈ ℝ, ∀ u > 0, ∃ v > 0, x + u < y + v).
Choose y := (x).
* Indeed, (y ∈ ℝ).
* We need to show that (∀ u > 0, ∃ v > 0, x + u < y + v).
  Take u > 0.
  We need to show that (∃ v > 0, x + u < y + v).
  Choose v := (u + 1).
  - Indeed, (v > 0).
  - We need to show that (x + u < y + v).
    It holds that (y = x).
    It holds that (v = u + 1).
    It holds that (y + v = x + (u + 1)).
    It holds that (x + u < x + u + 1).
    We conclude that (x + u < y + v).
"""
with open("exercises/imports/E3_11_2.v", "r") as file:
            imports = file.read()
with open("exercises/E3_11_2.v", "r") as file:
            exercise = file.read()

#print(compile_output(proof, imports, exercise) == "")

#print(parse(exercise_numbers))

run(models, exercise_numbers, prompt_filename, tutorial_filename)