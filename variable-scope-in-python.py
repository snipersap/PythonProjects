#Variable scope in python
a = 10 #global
b = 20
def sample():
    a = 20  #local to the function
    print("local a:",a)

def sample_func():
    global b        #referencing to the globally defined b
    b = 30
    print("B in func:",b)

def sample_local():
    b = 40
    print("local b in func:",b)

print("global a:",a)
sample()
sample_func()   #modifies global b
print("b outside of func:",b)
sample_local()  #modifies local b
print("b outside of func:",b)

