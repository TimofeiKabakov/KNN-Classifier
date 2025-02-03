import os
import shutil
import re

# Define paths
source_folder = './MPEG7dataset/pngs'  # Folder containing all files
folder_1 = './MPEG7dataset/training-set'  # Files 1-10
folder_2 = './MPEG7dataset/testing-set'  # Files 11-20

# Create output folders if they don't exist
os.makedirs(folder_1, exist_ok=True)
os.makedirs(folder_2, exist_ok=True)

# Regex pattern to match filenames like "apple-1", "banana-15", etc.
pattern = re.compile(r'^(.*)-(\d+)\.(\w+)$')  # Adjust if file extensions are different

# Iterate over all files in the source folder
for filename in os.listdir(source_folder):
    match = pattern.match(filename)
    if match:
        category, number, extension = match.groups()
        number = int(number)

        src_path = os.path.join(source_folder, filename)

        if 1 <= number <= 10:
            dest_path = os.path.join(folder_1, filename)
        elif 11 <= number <= 20:
            dest_path = os.path.join(folder_2, filename)
        else:
            continue  # Skip files outside the 1-20 range

        # Move the file (or use shutil.copy() if you prefer copying)
        shutil.move(src_path, dest_path)

        print(f'Moved: {filename} → {dest_path}')

print("✅ Files successfully split into two folders!")
