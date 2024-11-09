class MyClass:
    x = 100
    
    def hello(self):
        print("Hello!")
        

myobject = MyClass()


print(myobject.x)


myobject.x -= 50
print(myobject.x)


myobject.hello()
