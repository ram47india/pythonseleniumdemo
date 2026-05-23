class Myclass:
    def instance_method(self):
        print("This is an instance method.")

    @classmethod
    def class_method(cls):
        print("This is a class method.")
obj = Myclass()
print(obj.instance_method())     #Instance method can be called using the object of the class
print(Myclass.class_method())   #Class method can be called using the class name