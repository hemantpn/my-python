#!/home/ec2-user/my_app/env/bin/python
def add(**kargs): #it means define key,value like a=4,b=8
   print(kargs)
   return None
'''add(3,4)      #will give a error'''
add(a=4,b=5)     #output will be in tuple
add(a=10,x=23,name='hemant')    #output will be in tuple

print("============output will be in dictionary================")

def add_1(p,**kargs): #it means define key,value like a=4,b=8
    print (p)
    print(kargs)
    return None
'''add_1(3,4)      #will give a error'''
add_1(10,a=4,b=5)     #output will be in tuple
add_1(23,a=10,x=23,name='hemant')    #output will be in tuple
