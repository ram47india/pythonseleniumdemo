file = open('test.txt')
# print(file.read())
print(file.read(15))
print(file.readline())
print(file.readline())
print("-------------------------------------Readline---------------------------------")
#Readline - reads a single line from the file
file = open('test.txt')
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
print("-------------------------------------Readlines---------------------------------")
#Readlines - reads all the lines and returns a list of lines
file = open('test.txt')
for line in file.readlines():
    print(line)
print("-------------------------------------Open method---------------------------------")
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
print("---------Count and print total number of line in file-----------")
with open("test.txt","r") as file:
    count = 0
    for line in file:
        count += 1
print(f"Total number of lines in file: {count}")