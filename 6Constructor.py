#Constructor - name should be __init_, class variable, instance variable used to initialize the object
#self - represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python

class Calculator:
    num = 100   #class variable
    def __init__(self, a, b):   #constructor with parameters
        self.firstnum = a      #instance variable
        self.secondnum = b     #instance variable
        print("Called automatically with default constructor")
    def getdata(self):
        print("Method inside class called")
    def summation(self):
        return print("Sum is:", self.firstnum + self.secondnum+Calculator.num)
objcalculator = Calculator(15, 25)   #instance of class
objcalculator.getdata()
objcalculator.summation()
print(objcalculator.num)

objcalculator1 = Calculator(50, 70)   #instance of class
objcalculator1.getdata()
print(objcalculator1.num)
objcalculator1.summation()