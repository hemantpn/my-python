#!/home/ec2-user/my_app/env/bin/python

numbers=[0,1,2,3,4,5]
d_n=[]
for each_num in numbers:
   d_n.append(each_num*2)
   print(d_n)

print("=======================================")
print(d_n)

print("==================other -way=============")

doubled_num=[each_num*2 for each_num in numbers]
print(doubled_num)

print("==================other -way=============")
doubled_n=[each_num*2 for each_num in range(6)]
print(doubled_n)

print("==================other -way=============")
ages= [2,4,56,43]
print([f"my friend is {age} year old" for age in ages])
