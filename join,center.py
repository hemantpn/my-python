#!/home/ec2-user/my_app/env/bin/python
import os
x="python"

print('*'.join(x))

print('\n'.join(x))



print(x.center(10))


print(x.zfill(10))  #it calls padding operation#

print("------------\'==========\'")
print("------------\'==========")

y="scripting"
''' use for define paths , bydefault it takes / in between both paths '''
print(os.path.join(x,y))   #use for define paths , bydefault it takes / in between both paths
