from Constructor6 import Calculator
class Child(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self, 30, 40)   #calling parent class constructor
    def getcompletedata(self):
        total = self.firstnum + self.secondnum + Calculator.num + Child.num2
        return print("Total is:", total)
objChild = Child()   #instance of child class
objChild.getcompletedata()
objChild.summation()   #calling parent class method
print(objChild.num2)   #accessing child class variable
print(objChild.num)    #accessing parent class variable
print(Calculator.num)