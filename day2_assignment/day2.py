"""
file_operations.py - Solutions for file operations questions
"""
import os
import glob

def find_largest_file(directory):
    """Question-3: Given a directory, find out the file Name having max size recursively"""
    max_size = 0
    max_file = None
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > max_size:
                max_size = file_size
                max_file = file_path
    
    return max_file, max_size

def collect_filtered_files(directory, extension, output_file):
    """Question-4: Recursively go below a dir and based on filter, dump those files into single file"""
    with open(output_file, "wt") as f_out:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    f_out.write(f"\n# FILE: {file_path}\n")
                    
                    with open(file_path, "rt") as f_in:
                        lines = f_in.readlines()
                        f_out.writelines(lines)

# Directory to search
path = "."

# Question-3: Find largest file
largest, size = find_largest_file(path)
print(f"Largest file: {largest}, Size: {size} bytes")

# Question-4: Collect Python files
collect_filtered_files(path, ".py", "all_python_files.txt")
print("Python files collected in: all_python_files.txt")