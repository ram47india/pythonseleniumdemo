#if condition

greeting = "Morning"
if greeting == "Morning":
    print("Condition Matched")
else:
    print("Condition not Matched")
print("Condition Check Completed")
#if else condition
greet = "Hello1"
if greet == "Hello":
    print("Hello There!\nHow can I assist you today?")
else:
    print("Greetings!")
print("Greet Check Completed")
#Number comparison
b = 5
if b > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less")
print("Comparison Completed")
#Multiple conditions with elif
user = 5
if 5 <= user <= 11:
    print("Good Morning")
elif 12 <= user <= 17:
    print("Good Afternoon")
elif 18 <= user <= 21:
    print("Good Evening")
else:
    print("Good Night")
print("Time-based Greeting Completed")

#For Loop
obj = [2,3,4,7,9]
for i in obj:
    print("for Loop Iteration Value is:",i)
for i in obj:
    print("for Loop Multiplied with 2 is:",i*2)
for i in obj:
    print("for Loop Multiplied with 3 is:",i*3)
#sum of first 5 numbers
sum = 0
for j in range(1,6):    #range(start, end-1)
    sum = sum + j
print("Sum of first 5 numbers:",sum)
for j in range(1,10,2):    #range(start, end-1, step)
    print("Odd Numbers between 1 to 10 are:",j)
for l in range(15):
    print("Loop Value is:",l)
#While Loop  - condition is true continue execution until condition is false
t = 5
while t < 14:
    print("While Loop Value is:",t)
    t = t + 1   #increment to avoid infinite loop
print("While Loop Completed")
t = 5
while t > 1:
    if t != 3:
        print("Not Equal to 3, Current Value is:",t)
    t =t -1
#break statement  - exit from loop when condition met and stop further execution
r = 4
while r > 1:
    print("R Current Value is:",r)
    if r !=3:
       break
    print("Break Statement Current Value is:",r)
    r = r - 1
#continue statement - skip the current iteration when condition met and continue with next iteration
g = 14
while g > 1:
    print("G Current Value is:",g)
    if g == 9:
        g = g -1
        continue
    if g == 3:
        break
    print("Continue Statement Current Value is:",g)
    g = g - 1
print("Continue Statement Completed")
