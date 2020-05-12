#!/home/ec2-user/my_app/env/bin/python
import os
'''
os.path.sep : to check seprator, win(\) ,linux(/)
os.path.basename(path): it shows tail part , like in /home/ubuntu/a.py   , So here output is a.py
os.path.dirname(path): it show head part like in home/ubuntu/a.py   , So here output is /home/ubuntu/  
os.path.join(path1,path2)  : to join two paths , output will be string 
os.path.split(path): is used to split the path into a pair head and tail
os.path.getsize(path): in bytes ,to check size of file, dir

os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)
os.path.islink(path)
'''

def main():
 path=input("enter the path: ")
 if os.path.exists(path):
   if os.path.isfile(path):
     print(f'path of file is {path}')
   else:
     print(f'path of dir is {path}')
 else:
   print("please choose right path")
   return None

main()
