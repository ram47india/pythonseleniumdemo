#Function is a group of related statements that perform a specific task.

def func():         #function definition
    print("Hello from a function")
func()

def func1(name):   #function with parameter
    print("Hello " + name + ", Welcome to Python Automation Testing")
func1("Ram")

def func2(a, b):   #function with multiple parameters
    print(a + b)
func2(5,13)

def func3(x, y ):      #function with return value
    return x * y
print(func3(6, 9))

def GreetUser(username):
    print("Hello, " + username + " Welcome to the Python course")
GreetUser("John!")

def CalculateAverage(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average
print("The average of 10, 20 and 30 is", CalculateAverage(10, 20, 30))