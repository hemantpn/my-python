#!/home/ec2-user/my_app/env/bin/python
def my_f1():
    x=10  #local variable
    print("this is function1 ,using local variable:",x) #includ function2 in function1 , but local variable won't included in function2  it'll pick global variable 
    my_f2()
    return None

def my_f2():
    print("welecome!!,using global variable:",x)
    return None
x=20
my_f1()

print("==========use of local variable in both functin===================")
def my_f1():
    x=10  #local variable
    print("this is function1,using local variable:",x)
    my_f2()
    return None

def my_f2():
    x=30
    print("welecome!! ,using local variable:",x)
    return None

x=20
my_f1()
