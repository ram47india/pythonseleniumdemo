str = "ramkumar"
str1 = "Welcome to Python Programming"
print(str[1])   #accessing character at index 1
print(str[0:3])   #accessing characters from index 0 to 2
print(str + "\n" + str1)  #string concatenation
str2 = "kumar"
Result = str2 in str    #String presence check
print(Result)

var = str1.split(" ")   #Splitting string based on space
print(var[0])   #accessing first word after split
print(var[3])   #accessing fourth word after split
str3 = "  Hello World  "
print(str3.strip())  #removing leading and trailing spaces
print(str3.lstrip()) #removing leading spaces
print(str3.rstrip()) #removing trailing spaces
