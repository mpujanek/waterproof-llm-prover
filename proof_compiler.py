import subprocess
import tempfile
import re

def close_section(file_content: str) -> str:
    match = re.search(r'^(Section|Module)\s+([^\s.]+)\.', file_content, re.MULTILINE)
    if match:
        keyword = match.group(1)  # "Section" or "Module"
        name = match.group(2)
        return f'\nEnd {name}.'
    return ''

def compile_output(proof, imports, exercise, exercise_number):
    print("Compiling model output...")

    full_text = imports + exercise + "\n" + proof + "\nQed." + close_section(exercise)

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".v", prefix="E" + exercise_number + "_", delete=False) as tmpfile:
        tmpfile.write(full_text)
        tmp_path = tmpfile.name

    # Print temp file contents for debugging
    with open(tmp_path, "r") as f:
        print("--- Temp file contents ---")
        temp_full = f.read()
        print(temp_full)

    # Run the script and capture the output
    result = subprocess.run(["bash", "exercises/checkproof.sh", tmp_path], capture_output=True, text=True)

    # Access stdout and stderr (debug)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    # If there is an error, split text by lines and extract the line with the error
    if result.stderr:
        lines = temp_full.splitlines()
        match = re.search(r'line (\d+)', result.stderr)
        if match:
            line_number = int(match.group(1))
            if 1 <= line_number <= len(lines):
                return result.stderr, lines[line_number - 1]
        # If no valid line number found
        return result.stderr, "Line not specified."

    # No error
    return "", None