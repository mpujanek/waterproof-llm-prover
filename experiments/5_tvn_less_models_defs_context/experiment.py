import os
from main import run

#models = {"openai/o4-mini": 10,
#          "anthropic/claude-sonnet-4": 10, 
#          "google/gemini-2.5-flash-preview-05-20:thinking": 10,
#          "x-ai/grok-3-mini-beta": 10
#         }

models = {"x-ai/grok-3-mini-beta": 0,
          "x-ai/grok-3-beta": 10
         }

exercise_numbers = ["4_9_1"]

# provide list of generic definitions in prompt?
defs_no_context = False

# expand all definitions in proof?
defs_in_context = True

# in this directory
prompt_filename = "generic_wp_prompt.txt"
tutorial_filename = "tutorial.txt"
revision_filename = "revision_prompt.txt"

base_dir = os.path.dirname(os.path.abspath(__file__))
directory = "results"

runs = 1

run(models, exercise_numbers, defs_no_context, defs_in_context, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs)