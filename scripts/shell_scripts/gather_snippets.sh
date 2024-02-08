#!/bin/bash

# Define the array of temperature values
temperatures=(0 1 2)

# Define the array of tasks
tasks=("python" "javaTopython" "pythonTojava")

# Loop over each temperature
for temp in "${temperatures[@]}"; do
    # Loop over each task
    for task in "${tasks[@]}"; do
        # Run the command with the current temperature and task
        python3 gather_snippets.py --prompt reverse_int --model gpt-3.5-turbo --temperature "$temp" --task "$task"
    done
done
