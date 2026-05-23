#Class - user defined blueprint or prototype . Can have methods, class variables, instance variables, constructors

class simple:
    num = 10   #class variable
    def display(self):   #method - same as function but defined inside class
        print("Hello from class method")
objsimple = simple()   #instance of class
objsimple.display()
print(objsimple.num)   #accessing class variable

class BasicCalculator:
    def __init__(self, a, b):
        self.firstnum = a
        self.secondnum = b
    def Addition(self):
        return print("Addition:", self.firstnum + self.secondnum)
    def Subtraction(self):
        return print("Subtraction:", self.firstnum - self.secondnum)
    def Multiplication(self):
        multiplication = print("Multiplication:", self.firstnum * self.secondnum)
        return multiplication
    def Division(self):
        division = print("Division:", self.firstnum / self.secondnum)
        return division
objcal = BasicCalculator(10, 5)         #instance of class
objcal.Addition()
objcal.Subtraction()
objcal.Multiplication()
objcal.Division()