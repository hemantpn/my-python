#!/home/ec2-user/my_app/env/bin/python
path=['usr/bin','usr/bin/httpd','usr/bin/local']

for each_path in path:
    print (each_path)    #how loop works
    if 'httpd' in each_path:
        print(each_path)
        break        #to stop


print("#==============while-loop====================#")

cnt=1
while True:
    print(cnt)
    if cnt==100:
       break
    cnt=cnt+1

print("#==============while-loop====================#")

cnt=1
while cnt<=200:
  print(cnt)
  cnt=cnt+1


print("#==============while-loop====================#")

cnt=1
while cnt<=5:
  print("hello")
  cnt=cnt+1

print("#==============Continue====================#")

for each in range(1,11):
    if each !=7:
       print(each) #(it will skip 7)
       print ("================hi======================")
    print ("================OR======================")  #it'll not check condition , outside of for loop condition
print("#==============hi====================#")  #outside of loop

print("#==============alternative-Continue====================#")

for each in range(1,11):
    if each ==7:
        continue
        print("#this is the line inside of your skip condition=#")  #after use of continue it'll automatically skip
    print(each) #(it will skip 7)

print("#==============Pass: to avoid an error====================#")

for each in range(10):
    pass  #if i want to use loop but as pe current don't know what can i right to avoid error we can use pass

