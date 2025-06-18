import os
from main import run

models = {"openai/gpt-4.1": 0, 
          "openai/o4-mini": 0,
          "anthropic/claude-sonnet-4": 10, 
          "anthropic/claude-3.7-sonnet:thinking": 0,
          "google/gemini-2.5-flash-preview-05-20": 0, 
          "google/gemini-2.5-flash-preview-05-20:thinking": 10,
          "deepseek/deepseek-chat-v3-0324": 0, 
          "deepseek/deepseek-r1-0528": 0,
          "x-ai/grok-3-mini-beta": 0,
          "x-ai/grok-3-beta": 0
          }

exercise_numbers = [
    "10_7_intermediate",
    "4_9_1", "4_9_3",   
    "5_9_1",
    "13_11_3"         
]

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

run(models, exercise_numbers, defs_no_context, defs_in_context, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs)