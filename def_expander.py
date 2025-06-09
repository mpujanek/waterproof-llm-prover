from exercise_parser_defs import parse
from prompt_composer import compose
from proof_compiler_defs import compile_output
import os

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

exercises, imports = parse(all_exercises)

prompt_filename = "generic_wp_prompt.txt"
tutorial_filename = "tutorial.txt"
revision_filename = "revision_prompt.txt"

# Compose prompt from given files
no_tutorial_prompt, prompt, tutorial = compose(prompt_filename, tutorial_filename)

defs = ["infimum", "supremum", "maximum", "upper bound", "converges to",
        "bounded", "bounded below", "bounded above", "diverges to ∞", "diverges to -∞",
        "index sequence", "subsequence", "closed", "open", "interior point", "continuous",
        "accumulation point", "limit", "isolated point"]
definition = "asd"

# Define the target directory where you want to store the file
output_dir = "expanded_definitions"

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

output_filename = f"{definition}.txt"

# Full path to the output file
output_path = os.path.join(output_dir, output_filename)

for exercise_key in exercises:
    if exercise_key == "13_11_3":
        expanded_def = compile_output(
                        "",
                        imports[exercise_key],
                        exercises[exercise_key],
                        exercise_key
                    )
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(expanded_def)