import os

def find_largest_file(directory):
    max_size = 0
    max_file = None
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                if size > max_size:
                    max_size = size
                    max_file = file_path
            except Exception as e:
                pass
    return max_file, max_size

if __name__ == "__main__":
    directory = r"."
    file_name, size = find_largest_file(directory)
    if file_name:
        print(f"File with maximum size: {file_name} ({size} bytes)")
    else:
        print("No files found.")
