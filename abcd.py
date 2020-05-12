#!/home/ec2-user/my_app/env/bin/python
import os
import datetime
def main():
    path=os.listdir("/home/ec2-user/hemant") #/home/ec2-user/ansible-environments/aws
    #path1=os.system("ls -lh")
    for each in path:
        #print('*'.join(each))
        if os.path.isdir(path.splitline()):
         path1=os.path.join("/home/ec2-user/hemant",each)
         print(path)       
         path2=os.listdir(path1) 

main()

print("==================================")
