import re

# Returns dict with exercise numbers as keys and content as values
def parse(exercise_numbers, defs_in_context):
    print("Parsing exercise sheets...")

    if defs_in_context:
        dir = "exercises_with_defs"
    else:
        dir = "exercises"

    exercises = {}
    imports = {}

    # Initialize dict keys
    for exercise in exercise_numbers:
        # Get exercise content path and open it
        exercise_path = f"./{dir}/E{exercise}.v"
        with open(exercise_path, "r") as file:
            content = file.read()

        # Get exercise imports path and open it
        imports_path = f"./{dir}/imports/E{exercise}.v"
        with open(imports_path, "r") as file:
            exerciseimports = file.read()

        # Get all library imports
        libimports_path = f"./{dir}/libimports.v"
        with open(libimports_path, "r") as file:
            libimports = file.read()

        exercises[exercise] = content
        imports[exercise] = libimports + exerciseimports

    return exercises, imports

def clean(text):
    # Remove surrounding backticks or code fences
    text = text.strip().strip("`")

    # Find positions of last 'Proof.' and last 'Qed.'
    proof_start = text.rfind("Proof.")
    qed_end = text.rfind("Qed.")

    if proof_start == -1:
        start = 0
    else:
        start = proof_start + len("Proof.")

    if qed_end == -1:
        end = len(text)
    else:
        end = qed_end

    cleaned = text[start:end].strip()

    # Normalize line endings and remove empty lines
    lines = [line.strip() for line in cleaned.splitlines() if line.strip()]
    return "\n".join(lines)