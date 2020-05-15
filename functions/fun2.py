#!/home/ec2-user/my_app/env/bin/python
x=eval(input("enter a value: "))  #eval doesn't work in python 2.7
y=eval(input("enter a value: "))
add=x+y
sub=(x-y)

print (add)

def addition(x,y):
  x=2
  y=1
  print(f'addition of {x} and {y}:{add}')
  subtraction(x,y)
  return None
  
def subtraction(x,y):
  print(f'sub of {x} and {y}: {sub}')
  return None

#x=5
#y=11
addition(x,y)
#subtraction(x,y)
