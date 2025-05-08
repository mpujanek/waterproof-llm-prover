import subprocess
import tempfile

def compile_output(proof, imports, exercise):
    print("Compiling model output...")

    full_text = imports + exercise + proof + "\nQed."

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".v", delete=False) as tmpfile:
        tmpfile.write(full_text)
        tmp_path = tmpfile.name  # Store the path if needed later

    # Print temp file contents for debugging
    with open(tmp_path, "r") as f:
        print("--- Temp file contents ---")
        print(f.read())

    # Run the script and capture the output
    result = subprocess.run(["bash", "exercises/checkproof.sh", tmp_path], capture_output=True, text=True)

    # Access stdout and stderr (debug)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    return result.stderr