#!/home/ec2-user/my_app/env/bin/python
import os
'''
use of os.walk is list of path, dir and files sequencly output comes in list in side of tuple but we can change in string using og os.path.join()

'''
def main():
 path=("/home/ec2-user/ansible-environments/aws/")
 x=list(os.walk(path))   #in the os.walt data comes like p1: path, d1: dir,f1:files
 for (p1,d1,f1) in x:
#  print(p1,d1,f1)
#  print(f1)
#  print("==========================")
#    for each_f in p1:~
  if len(f1) !=0:
#    print(p1)
#    print("==========================")
    for each_f in f1: 
    # print(each_f)
#        print("==========================")
      if each_f.endswith(".sql"):
        print(os.path.join(p1,each_f))
    
#  for (p,d,f) in x:
#   print(p)
#   print(d)
#   print(f)
#   print("====================")
#   print(os.path.join(x,f))
main()
