import json
import os
from datetime import datetime

def export_json(model, exercise, output, proof_result, directory):
    # Prepare data
    data = {
    "output": output["output"],
    "token_count": output["token_count"],
    "input_tokens": output["input_tokens"],
    "output_tokens": output["output_tokens"],
    "cost": output["cost"],
    "thinking_mode": output["thinking_mode"],
    "compiles": proof_result
    }

    # Get current date and time for folder name
    now = datetime.now()
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Make path for the new folder
    base_path = os.path.join(os.getcwd(), directory)
    folder_path = os.path.join(base_path, folder_name)

    # Create the new folder
    os.makedirs(folder_path)

    # Create file name
    exercise_name = exercise.replace(".", "-")
    filename = f"{model}_{exercise_name}.json"
    file_path = os.path.join(folder_path, filename)

    # Save to new file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Finished running {model} on exercise {exercise}.")