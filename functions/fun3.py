#!/home/ec2-user/my_app/env/bin/python
def my_f1(x):
    x=10
    print("this is function1,using local variable:",x)
    my_f2(x,y)
    return None

def my_f2(x,y):
    print("welecome!! ,using local variable:",x)
    print("welecome!! ,using local variable:",y)
    return None

def main():
    global x    #not a good prectise
    global y
    x=1  
    y=2
    my_f1(x)
    my_f2(x,y)
    return None

main()

print("======================")
def main2():
    y=22
    my_f1(x)
    my_f2(x,y)
    return None
main2()
print("======================")
def main3(x,y):
    my_f1(x)
    my_f2(x,y)
    return None

main3(111,222)
