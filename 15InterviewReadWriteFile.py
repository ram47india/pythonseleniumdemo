with open("test.txt", "w") as f:
    f.write("This is a test file.\n")
    f.write("It contains multiple lines of text.\n")
    f.write("This is the third line.\n")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)

