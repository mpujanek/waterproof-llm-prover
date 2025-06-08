import os
from main import run

models = ["openai/gpt-4.1", "openai/o4-mini",
          "anthropic/claude-sonnet-4", "anthropic/claude-3.7-sonnet:thinking",
          "google/gemini-2.5-flash-preview-05-20", "google/gemini-2.5-flash-preview-05-20:thinking",
          "deepseek/deepseek-chat-v3-0324", "deepseek/deepseek-r1-0528"]

exercise_numbers = ["10_7_6", "10_7_intermediate"]

# provide list of generic definitions in prompt?
defs_no_context = False

# expand all definitions in proof?
defs_in_context = False

# in this directory
prompt_filename = "generic_wp_prompt.txt"
tutorial_filename = "tutorial.txt"
revision_filename = "revision_prompt.txt"

base_dir = os.path.dirname(os.path.abspath(__file__))
directory = "results"

runs = 1
max_attempts = 1

# first run thinking models, one attempt each
run(models, exercise_numbers, defs_no_context, defs_in_context, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs, max_attempts)