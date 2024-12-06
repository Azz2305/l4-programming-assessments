def read_files(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        print(f"Contents of {file1}:\n{f1.read()}")
        print(f"\nContents of {file2}:\n{f2.read()}")
read_files('file1', 'file2.txt')