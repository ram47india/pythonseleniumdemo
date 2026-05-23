#Exceoption Handling using Try and Catch

#prints the exception message define by default
try:
    print(Variable_not_defined)
except:
    print("Variable_not_defined is not defined")

#prints the exception message returned by the interpreter
try:
    print(Variable_not_defined)
except Exception as e:
    print(e)
finally:
    print("Execution completed")

#Custom Exception - Shopping Cart Validation
def add_to_cart(items_to_add):
    ItemsInCart = 0
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart Limit exceeded")
    ItemsInCart = ItemsInCart + items_to_add
    print(f"{items_to_add} items added. Total in cart:{ItemsInCart}")
try:
    add_to_cart(2)
    add_to_cart(-1)

except Exception as e:
    print(e)

#Tuple - immutable (cannot be changed) collection of items
person = ("Ram", 25, 6.5)
print("Age:", person[1])
try:
    person[0] = "Kumar"
except Exception as e:
    print(e)