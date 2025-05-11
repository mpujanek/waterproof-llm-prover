

# Returns dict with exercise numbers as keys and content as values
def parse(exercise_numbers):
    print("Parsing exercise sheets...")

    exercises = {}
    imports = {}

    # Initialize dict keys
    for exercise in exercise_numbers:
        # Get exercise content path and open it
        exercise_path = f"./exercises/E{exercise}.v"
        with open(exercise_path, "r") as file:
            content = file.read()

        # Get exercise imports path and open it
        imports_path = f"./exercises/imports/E{exercise}.v"
        with open(imports_path, "r") as file:
            exerciseimports = file.read()

        # Get all library imports
        libimports_path = f"./exercises/libimports.v"
        with open(libimports_path, "r") as file:
            libimports = file.read()

        exercises[exercise] = content
        imports[exercise] = libimports + exerciseimports

    return exercises, imports

def clean(exercise):
    lines = exercise.strip().splitlines()

    # Remove starting 'Proof.' if present
    if lines and lines[0].strip() == "Proof.":
        lines = lines[1:]

    # Remove ending 'Qed.' if present
    if lines and lines[-1].strip() == "Qed.":
        lines = lines[:-1]

    return "\n".join(lines).strip()