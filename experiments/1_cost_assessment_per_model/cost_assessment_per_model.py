import os
from main import run

models = {"openai/gpt-4.1": 2, "openai/o4-mini": 2,
          "anthropic/claude-sonnet-4": 2, "anthropic/claude-3.7-sonnet:thinking": 2,
          "google/gemini-2.5-flash-preview-05-20": 2, "google/gemini-2.5-flash-preview-05-20:thinking": 2,
          "deepseek/deepseek-chat-v3-0324": 2, "deepseek/deepseek-r1-0528": 2}

exercise_numbers = ["3_11_4", "4_9_3"]

# provide list of generic definitions in prompt?
defs_no_context = True

# expand all definitions in proof?
defs_in_context = False

prompt_filename = "generic_wp_prompt_with_defs.txt"
tutorial_filename = "tutorial.txt"
revision_filename = "revision_prompt.txt"

base_dir = os.path.dirname(os.path.abspath(__file__))
directory = "results"

runs = 1

run(models, exercise_numbers, defs_no_context, defs_in_context, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs)