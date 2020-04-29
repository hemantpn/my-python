#!/home/ec2-user/my_app/env/bin/python
x=4
y=5.6
z=3+4j

x=4;y=5.6;z=3+4j
print(x,y,z)
#print(split().(x,y,z))

print(type(x))
print(type(y))
print(type(z))
print("#==========================================")

name = 'hemant'  #should be in '' or ""
print(name,type(name))
print("#==========================================")

my_value=True #should be in cap for boolean
my_value_new=False
print(my_value,type(my_value))
print(my_value_new,type(my_value_new))
print("#===============\"convert-data-type\"===========================")

x=43
print(x,type(x))

y=str(x)
print(y,type(y))

z=bool(x)    #0 ise false except 0 true
print(z,type(z))
p=0
print(type(p))
q=bool(p)
print(type(q))

Print("#=======================Note=============================== \nAny data can be converted into boolean\nbool(any_data_type)=True or False\n\nbool(empty)=False ==>bool(0) ,bool(None),bool(()),bool({}),bool([])\nbool(non-empty)=True\n\nAny data can be converted into string but reverse is not true")
