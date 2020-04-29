#!/home/ec2-user/my_app/env/bin/python
def add(*data): #we can use any varaible *arg, *args
   print(data)
   return None
add()      #output will be in tuple
add(4,5)     #output will be in tuple
add(10,23)    #output will be in tuple

print("=================keep value same===================")

def my_sql_user(a,b):
    print(f'{a},{b}')

my_sql_user(a=3,b=4)   #most
my_sql_user(b=3,a=4)   #most
my_sql_user(4,3)   #most
