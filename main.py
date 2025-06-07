from exercise_parser import parse, clean
from prompt_composer import compose, compose_revision
from openrouter_api_caller import call_api, PRICING
from proof_compiler import compile_output
from json_exporter import export_json, make_folder
from concurrent.futures import ThreadPoolExecutor, as_completed

## STEP 1: Specify models to test

# Some example models you can use are given in PRICING
# You can also input any other model id from openrouter.ai

models = ["x-ai/grok-3-mini-beta", "openai/o4-mini"]

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

exercise_numbers = ["11_not_closed"]


## STEP 3: Specify prompt and provide a syntax tutorial
# These are loaded from files in this directory. 
# In the prompt file, specify where the tutorial should be inserted by using the marker "%tutorial%". 

prompt_filename = "generic_wp_prompt.txt"
tutorial_filename = "tutorial.txt"
revision_filename = "revision_prompt.txt"


## STEP 3: Specify folder to store results
# Define below a master folder (in this directory) in which the test results will be stored.
# Each test run will have its results stored in a new folder within the specified folder.

directory = "responses"

## Run tests

def run(models, exercise_numbers, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs=1, max_attempts=1):

    # Parse exercise sheets to extract desired exercises
    # Returns dict with exercise numbers as keys and content as values
    exercises, imports = parse(exercise_numbers)

    # Compose prompt from given files
    no_tutorial_prompt, prompt, tutorial = compose(prompt_filename, tutorial_filename)

    # Make a folder in the specified directory for storing results of this run
    folder_path = make_folder(directory, relative_to=base_dir)

    # Define the task of running a model on an exercise; these will be run concurrently
    def task(model, exercise_key, run_index, max_attempts):

        # In case of multiple runs per model
        run_id = f"{model}::{exercise_key}::{run_index}"

        # For keeping track of errors between iterations
        proof_errors = None
        line_with_error = None
        conversation_history = []

        for attempt in range(1, max_attempts + 1):

            if attempt == 1:
                # Concatenate exercise to the prompt
                input = prompt + "\n" + exercises[exercise_key]
            else: 
                # Use revision prompt instead if model is revising
                input = compose_revision(revision_filename, proof_errors, line_with_error)

            conversation_history.append({"role": "user", "content": input})

            # Call API of given model with input
            output = call_api(model, conversation_history)

            # Append model's response to conversation history
            conversation_history.append({"role": "assistant", "content": output["output"]})

            # Extract and clean the LLM's proof attempt before compiling (compile only between "Proof." and "Qed.")
            proof_attempt = clean(output["output"])

            # Compile response to check if proof is correct
            proof_errors, line_with_error = compile_output(
                proof_attempt,
                imports[exercise_key],
                exercises[exercise_key],
                exercise_key
            )

            # Export result to JSON
            export_json(
                model,
                exercise_key,
                exercises,
                no_tutorial_prompt,
                tutorial,
                input,
                output,
                proof_errors,
                folder_path,
                line_with_error,
                run_index,
                run_id,
                attempt,
                max_attempts
            )

            if proof_errors == "":
                break

    # Run each model on each exercise concurrently
    futures = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        for exercise_key in exercises:
            for model in models:
                for run_index in range(1, runs + 1):
                    futures.append(executor.submit(task, model, exercise_key, run_index, max_attempts))

        for future in as_completed(futures):
            try:
                future.result()  # Raises exception if any
            except Exception as e:
                print("Error during API run:", e)


#run(models, exercise_numbers, prompt_filename, tutorial_filename, revision_filename, directory, 2, 3)