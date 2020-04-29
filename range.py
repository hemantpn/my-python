#!/home/ec2-user/my_app/env/bin/python
print(range(5))   #in python3 output will come in tuple, in python2 it'lll in list, so we use 2nd method

print(list(range(5)))
print(list(range(0,5)))     #by default step value is 1
print(list(range(0,5,1)))    #here 0 is start, 5 stop, 1 is step

print(list(range(0,10,3)))

print(list(range(4,20,3)))

print(list(range(40,20)))   #empty list  
print(list(range(40,20,-3)))

print(list(range(-10,2)))
print(list(range(10,-2)))


my_list= [10,20,30,"hemant"]

for each_index in range(len(my_list)):
   print(f'index-->{each_index}: value-->{my_list[each_index]}')
