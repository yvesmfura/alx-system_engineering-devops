#!/bin/bash

# Loop through all files with .txt extension
for file in *.txt; do
    # Check if the file exists
    if [ -e "$file" ]; then
        # Remove the .txt extension from the filename
        new_name="${file%.txt}"
        # Rename the file
        mv "$file" "$new_name"
        echo "Removed .txt extension from $file"
    fi
done
