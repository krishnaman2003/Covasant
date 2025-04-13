"""
Question-4:
Recursively go below a dir and based on filter, dump those files in to  single file 
(work with only text file)
"""

import os
def dump_files(given_dir, output_file):
    with open(output_file, "wt") as outfile:
        for root, _, files in os.walk(given_dir):
            for file in files:
                if file.lower().endswith(".txt"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rt") as infile:
                            contents = infile.read()
                        outfile.write(f" Start of {file_path} \n")
                        outfile.write(contents)
                        outfile.write(f"\n----- End of {file_path} -----\n\n")
                    except Exception as e:
                        pass

if __name__ == "__main__":
    given_dir = r"C:\Users\Krishna Raj\Downloads\handson\handson"
    output_file = "combined_texts.txt"
    dump_files(given_dir, output_file)
    print(f"All files from {given_dir} have been dumped into {output_file}")
