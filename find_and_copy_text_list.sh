#!/bin/bash

echo "This script works in the present folder and searches recursively into subfolders"

# Prompt user for the filename to search for or the .txt file
read -p "Enter the filename to search for or the path to the .txt file containing the filenames: " input

# Prompt user for the destination folder
read -p "Enter the destination folder: " destination_folder

# Check if the input is a file or a filename
if [ -f "$input" ]; then
  # Read the filenames from the .txt file
  search_names=$(cat "$input")
else
  # Set the input as the filename to search for
  search_names=$input
fi

# Loop through the filenames and search for files with the specified name
for search_name in $search_names; do
  found_files=$(find . -name $search_name -type f -print0 | xargs -0 -I {} cp {} $destination_folder)
done

echo "Finished copying files"