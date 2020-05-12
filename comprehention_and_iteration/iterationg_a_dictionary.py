#!/home/ec2-user/my_app/env/bin/python
friends_ages={"a":20 , "b":34,"c":"23"}  # same we can do in list [('a',20),('b',30)] #note :inside a list values a tuple
for age in friends_ages:  #itlso we use as  for age in friends_ages.keys():    t'll wick only key
  print(f'age of {age}')
print("===================================================")
for age in friends_ages.values():   #it'll pic only values
  print(f'age of {age}')

print("===================================================")
for name,age in friends_ages.items():   #will pick both
  print(f'age of {name} is {age}')

print("============change list to dixtionary=======================")
list = [('a',20),('b',30)] #inside a list values are tuple
print(dict(list))


for name,age in list:
    print(f'age of {name} is {age}')
