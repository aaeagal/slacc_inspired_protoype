#!/bin/bash

# Target directory to process subdirectories within
TARGET_DIR="./"

# Loop through each subdirectory in the target directory
for SUBDIR in "$TARGET_DIR"*/; do
    # Check if the item is a directory
    if [ -d "$SUBDIR" ]; then
        echo "Processing $SUBDIR"
        # Create folders 0, 1, and 2 within the subdirectory
        mkdir -p "${SUBDIR}/0" "${SUBDIR}/1" "${SUBDIR}/2"
    fi
done

echo "Folders created successfully."