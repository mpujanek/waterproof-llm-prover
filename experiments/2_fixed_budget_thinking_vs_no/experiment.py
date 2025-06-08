import os
from main import run

models = {"openai/gpt-4.1": 50, 
          "openai/o4-mini": 5,
          "anthropic/claude-sonnet-4": 12, 
          "anthropic/claude-3.7-sonnet:thinking": 3,
          "google/gemini-2.5-flash-preview-05-20": 50,
          "google/gemini-2.5-flash-preview-05-20:thinking": 15,
          "deepseek/deepseek-chat-v3-0324": 50, 
          "deepseek/deepseek-r1-0528": 10
          }

exercise_numbers = ["3_11_4"]

# provide list of generic definitions in prompt?
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

run(models, exercise_numbers, defs_no_context, defs_in_context, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs)