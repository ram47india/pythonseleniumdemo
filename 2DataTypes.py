#Python DataTypes
# Numeric ->int, long(Deprecated in pythin 3.x), float, complex
# Sequence -> list, tuple, range
# Text -> str
# Mapping -> dict
from time import process_time_ns

#Numeric DataTypes
print("--------------Numeric DataTypes------------------------")
#int Variable
num1 = 10
print("The type of variable",num1,"is", type(num1))
#float Variable
num2 = 10.5789
print("The type of variable",num2,'is',type(num2))
#complex Variable
num3 = 2 + 3j
print("The type of variable",num3,"is",type(num3))

#Text - String DataType
print("--------------String DataType------------------------")
str1 = "Hello, Python in a double quotes"
str2 = 'Hello, Python in a single quotes'
print("The type of variable",str1,"is",type(str1))
print('The type of variable',str2,'is',type(str2))
#use ',' to concatenate 2 or several strings
print(str1,"concatenated with",str2)
#use '+' to concatenate 2 or several strings
print(str1+'concatenated with'+str2)
#Multiline String
str3 = """This is a
multiline string
example."""
print("The type of variable",str3,"is",type(str3))

#Sequence DataTypes - List, Tuple
print("--------------List DataType------------------------")
#List - Defined in  []  format
#Mutable -> Possible to modify after defined
#Allows multiple values & can be different data types
val = [1,2,"ram",4,5.6]
print("The variable",val,"is",type(val))
print(val[0])    #First Index
print(val[3])    #Fourth Index
print(val[-1])   #-1 -> Last index
print(val[1:3])  #Slicing
val.insert(3,"Kumar")   #add value at specific index position
print(val)
val.append("New Value")         #add value at last position in list
print(val)
val[2] = "Modified/Updated Value"    #Update/Modify value at specific index position
print(val)
del val[1]             #remove based on index position
print(val)
print("--------------Tuple DataType------------------------")
#Tuple - Defined in  ()  format
# Immutable -> Not Possible to modify after defined/created
# Same as List data type
tu = (1,2,"world",3.5,10)
print("The Variable",tu,"is",type(tu))
print(tu[1])
# tu[2] = "test"     #Error

#Mapping-Dictionary DataType-> Key-value pair -> defined as {Key : Value}
print("--------------Dictionary DataType------------------------")
dic1 = {"str":2, 4:5, 6:'Value', "Test": "Pass"}
print(dic1['str'])
print(dic1[4])
print(dic1[6])
print(dic1["Test"])
dic2 = {}           #Empty Dictionary
dic2["first"] = "Ram"
dic2["Last"] = "Kumar"
dic2[45] = 4565
print("The variable",dic2,"is",type(dic2))
dic2["gender"] = 'male'
print(dic2)

#Exercise1 List
fruits = ["apple", "banana", "cherry","date","elderberry"]
print("First fruit:",fruits[0])
print("Last fruit:",fruits[-1])
print("Fruits from index 1 to 2:",fruits[1:3])
#Exercise2 Tuple
person = ("Rahul",25,5.9)
print("Age:",person[1])
#Exercise3 Dictionary
car = {"make": "Toyota", "model":"Camry","year":2020,"color":"Blue"}
print("Car model:",car["model"])
car["owner"] = 'Rahul'
print("Updated car dictionary:",car)