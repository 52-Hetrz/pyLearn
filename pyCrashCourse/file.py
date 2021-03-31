file_path = "programming.txt"

with open("pi.txt") as file:
    contents1 = file.read()
    print(contents1)

with open('pi.txt') as file:
    contents2 = []
    for line in file:
        contents2.append(line.rstrip())
    print(contents2)

birthday = '19991012'
with open("pi.txt") as file:
    lines = file.readlines()
    file_str = ""
    for line in lines:
        file_str += line.rstrip()
    print(file_str)
    if birthday in file_str:
        print("in")

with open(file_path, 'w') as file:
    file.write("i love programming.")
    file.write("i love play games.\n")
    file.write("i love listen to music.\n")

with open(file_path, 'a') as file:
    file.write("\nthis is add.")
