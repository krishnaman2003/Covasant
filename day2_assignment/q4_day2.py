import os

def dump_text_files(source_dir, output_file):
    with open(output_file, "wt", encoding="utf-8") as outfile:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(".txt"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rt", encoding="utf-8") as infile:
                            contents = infile.read()
                        outfile.write(f"----- Start of {file_path} -----\n")
                        outfile.write(contents)
                        outfile.write(f"\n----- End of {file_path} -----\n\n")
                    except Exception as e:
                        pass

if __name__ == "__main__":
    source_dir = r"."
    output_file = "combined_texts.txt"
    dump_text_files(source_dir, output_file)
    print(f"All text files from {source_dir} have been dumped into {output_file}")
