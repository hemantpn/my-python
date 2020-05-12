#!/home/ec2-user/my_app/env/bin/python
import os
import datetime
def main():
    path=os.listdir("/home/ec2-user/ansible-environments/aws") #/home/ec2-user/ansible-environments/aws
    #path1=os.system("ls -lh")
    for each in path:
        #print('*'.join(each))
        path1=os.path.join("/home/ec2-user/ansible-environments/aws",each)
        if os.path.isdir(path1):
         print(path1)       
         path2=os.listdir(path1) 
       # print(path2)
       # if os.path.isdir(path2):
         for each1 in path2:
            path3=os.path.join(path1,each1)
'''splitlines() use to change string list'''
            pa=path3.splitlines()
           # print(path3)
      #      print(pa)            
           #`` path4=list(path3)
           # print(path4)

 #print(path1)
#        print(path2)
            for each_f in pa:
                if each_f.endswith(".sql"):

                    #          #:wq
                #  print(each_f)
                  x=[]
                  x.append(each_f)
                  ##print(x)
                  file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_f))
                  print(file_cre_date,each_f)
                  today=datetime.datetime.now()
                  diff_days=(today-file_cre_date).days
                  print(diff_days)
                  if diff_days >= 0 and diff_days < 1:
                     a=('').join(x)
                     print(a)
                     os.remove(a)
       # if os.path.isfile(path2):

#   print(path2)
#today=datetime.datetime.now()

main()

print("==================================")
