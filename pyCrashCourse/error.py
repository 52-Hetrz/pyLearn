file_path="text.txt"
try:
    with open(file_path) as file:
        contents = file.read()
except FileNotFoundError:
    print(file_path+" is not found")
else:
    text_split = contents.split()
    words = len(text_split)
    print(words)