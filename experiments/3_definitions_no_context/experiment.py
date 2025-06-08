import os
from main import run

models = ["openai/o4-mini"]

exercise_numbers = ["5_9_1"]

# provide list of generic definitions in prompt? DONT FORGET TO CHANGE PROMPT FILENAME
defs_no_context = True

# expand all definitions in proof?
defs_in_context = False

# in this directory
prompt_filename = "generic_wp_prompt_with_defs.txt"
tutorial_filename = "tutorial.txt"
revision_filename = "revision_prompt.txt"

base_dir = os.path.dirname(os.path.abspath(__file__))
directory = "results"

runs = 1
max_attempts = 1

run(models, exercise_numbers, defs_no_context, defs_in_context, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs, max_attempts)