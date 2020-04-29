#!/home/ec2-user/my_app/env/bin/python
try:
    print("hemant")
except:
    print("sharma")

print("================other-way-1==================")
try:
    file_open=open("hemant.txt")
    print(file_open.read())
    file_open.close()
except:
    print("hemant Sharma")  #write any thing


print("================other-way-2==================")
try:
    file_open=open("hemant.txt")
    print(file_open.read())
    file_open.close()
except Exception as e:    #we choose anything except e, i am representing here e as a error
    print(e)



try:
    my_list=[3,4,5]
    print(my_list[2])
    print(my_list[4])
except Exception as k:
    print('error is:',k)
