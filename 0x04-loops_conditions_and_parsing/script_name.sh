#!/bin/bash

# Loop through each file in the directory
for file in *.txt; do
    # Check if the file exists and is a regular file
    if [ -f "$file" ]; then
        # Remove the .txt extension from the file name
        new_file="${file%.txt}"
        
        # Rename the file
        mv "$file" "$new_file"
        
        echo "Renamed $file to $new_file"
    fi
done
