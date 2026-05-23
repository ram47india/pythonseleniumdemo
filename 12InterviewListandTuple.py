#Lists are mutable, ordered collection of items, defined using square brackets [],
#List can be modified after creation, you can add, remove, or change items in a list.
#Lists can contain items of different data types, including other lists.
#You can access individual items in a list using their index, which starts at 0.
#Lists are commonly used for storing and manipulating collections of data in Python.
my_li = [1, 2, 3, "Hello", [4, 5]]
print(my_li)
my_li[0] = 10  # Modifying the first element
print(my_li)
my_li.append("New")  # Adding a new element to the end of the list
print(my_li)
my_li.pop(1)  # Removing the second element
print(my_li)

#Tuples are immutable, ordered collection of items, defined using parentheses ()
#Tuples cannot be modified after creation, you cannot add, remove, or change items in a tuple.
my_tu = (1, 2, 3, "Hello", [4, 5])
# my_tu[0] = 10  # This will raise an error because tuples are immutable
print(my_tu)