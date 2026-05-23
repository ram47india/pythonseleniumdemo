class Parent:
    def parent_method(self):
        return "This is the parent method."

class Child(Parent):
    def child_method(self):
        # return "This is the child method."
        return super().parent_method()+" This is the child method."
obj_child = Child()
print(obj_child.child_method())
print(obj_child.parent_method())
