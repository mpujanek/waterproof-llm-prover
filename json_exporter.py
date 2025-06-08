import json
import os
from datetime import datetime

def export_json(model, exercise, exercises, prompt, tutorial, full_input, output, proof_errors, folder_path, line_with_error, run_index, run_id, attempt, max_attempts):
    # Prepare data
    data = {
        "model": model,
        "exercise": exercise,
        "prompt": prompt,
        "tutorial": tutorial,
        "full_input": full_input,
        "exercise_content": exercises[exercise],
        "output": output["output"],
        "token_count": output["token_count"],
        "input_tokens": output["input_tokens"],
        "thinking_tokens": output["thinking_tokens"],
        "output_tokens": output["output_tokens"],
        "cost": output["cost"],
        "thinking_mode": output["thinking_mode"],
        "errors": proof_errors,
        "line_with_error": line_with_error,
        "success": proof_errors == "" and line_with_error is None,
        "run_id": run_id,
        "attempt": attempt,
        "max_attempts": max_attempts,
    }

    # Create file name
    exercise_name = exercise.replace("_", "-")
    model_name = model.replace("/", "-")
    filename = f"{model_name}_{exercise_name}_run-{run_index}_attempt-{attempt}.json"
    file_path = os.path.join(folder_path, filename)

    # Save to new file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Finished running {model} on exercise {exercise}, attempt {attempt} of {max_attempts}.")

def make_folder(directory, relative_to=None):
    # Get current date and time for folder name
    now = datetime.now()
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")

    if relative_to is None:
        base_path = os.path.abspath(directory)
    else:
        base_path = os.path.abspath(os.path.join(relative_to, directory))

    folder_path = os.path.join(base_path, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    return folder_path
