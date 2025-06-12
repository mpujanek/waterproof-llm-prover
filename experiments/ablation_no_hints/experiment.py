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
    "2_non_degenerate_2",
    "2_positive_2",
    "2_reflexive_2",
    "3_11_1", "3_11_2",
    "10_7_intermediate",  
]

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

# provide list of generic definitions in prompt?
defs_no_context = False

# expand all definitions in proof?
defs_in_context = True

# in this directory
prompt_filename = "generic_wp_prompt_no_hints.txt"
tutorial_filename = "tutorial.txt"
revision_filename = "revision_prompt_no_hints.txt"

base_dir = os.path.dirname(os.path.abspath(__file__))
directory = "results"

runs = 1

run(models, exercise_numbers, defs_no_context, defs_in_context, prompt_filename, tutorial_filename, revision_filename, directory, base_dir, runs)