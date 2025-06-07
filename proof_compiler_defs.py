import subprocess
import tempfile
import re

def close_section(file_content: str) -> str:
    match = re.search(r'^Section\s+([^\s.]+)\.', file_content, re.MULTILINE)
    if match:
        section_name = match.group(1)
        return f'\nEnd {section_name}.'
    return ''

def compile_output(proof, imports, exercise, exercise_number):
    #print("Compiling model output...")

    full_text = imports + exercise + "\n" + proof + "\nQed." + close_section(exercise)

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".v", prefix="E" + exercise_number + "_", delete=False) as tmpfile:
        tmpfile.write(full_text)
        tmp_path = tmpfile.name

    # Print temp file contents for debugging
    with open(tmp_path, "r") as f:
        #print("--- Temp file contents ---")
        temp_full = f.read()
        #print(temp_full)

    # Run the script and capture the output
    result = subprocess.run(["bash", "exercises/checkproof.sh", tmp_path], capture_output=True, text=True)

    # Access stdout and stderr (debug)
    #print("STDOUT:", result.stdout)
    #print("STDERR:", result.stderr)

    def extract_first_expanded_definition(text):
        # Match from "We need to show that" to the first period "."
        pattern = re.compile(
            r"We need to show that\s*(.*?)\.", 
            re.DOTALL
        )

        match = pattern.search(text)
        if match:
            # Reconstruct full block with ending "."
            return "We need to show that " + match.group(1) + "."
        else:
            return None

    expanded_def = extract_first_expanded_definition(result.stdout)

    # No error
    return expanded_def