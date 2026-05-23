#lambda with map  : add =  lambda x,x:x+y
#multiply each element of the list by 2
n = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, n))
print(result)

#lamba with filter : filter the even numbers from the list
res_even = list(filter(lambda x: x % 2 == 0, n))
print("Even numbers are:", res_even)

#sort a list
l = [5, 2, 9, 1, 12, 6]
print("Sorted:", sorted(l))

#reverse sort a list
li = [5, 2, 9, 1, 12, 6]
print("Reverse:", li[::-1])  #This will reverse the list but not sort it
print("Reverse Sorted:", sorted(li, reverse=True)) #This will sort the list in reverse order