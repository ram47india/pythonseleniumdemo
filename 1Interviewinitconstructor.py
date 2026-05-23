#__int__ is a special method in Python classes, also known as a constructor.
#It is automatically called when an instance of the class is created.
#The purpose of the __int__ method is to initialize the attributes of the class with specific values when an object is instantiated.

class constructor:
    def __init__(self, name, age):  #constructor
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

obj = constructor("Rahul", 30)  #creating an object of the class and passing values to the constructor
obj.display_info()  #calling the method to display the information of the object
