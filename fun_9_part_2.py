#!/home/ec2-user/my_app/env/bin/python
import fun_9_part_1      #don't write .py


print(dir(fun_9_part_1))  #check script 1 functions

def multi(a,b):
    print(f'multi of {a} and {b}: {a*b}')
    return None

def main():
    x=10
    y=20
    multi(x,y)
    fun_9_part_1.addition(x,y)    #script name
    return None

if __name__=="__main__":
    main()



