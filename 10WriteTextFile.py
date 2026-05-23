#read all lines in file and store them in a list
#reverse the list
#write the reversed list to a new file
with open('test.txt', 'r') as file:
    content = file.readlines()
    print(content)
    content.reverse()
    print(content)
    with open('test.txt', 'w') as writer:
        for line in content:
            writer.write(line)