#!/home/ec2-user/my_app/env/bin/python
import subprocess
''' pattern:
sp=subprocess.Popen(cmd,shell=True/False),stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()   #return code
out,err=sp.communicate()
print(f'Output is: {out}')
print(f'Error is : {err}')


cmd='ls -lh'  #cmd in string
then shell=True, python will open new terminal to execute cmd
if cmd is list ['ls','-lh']  then shell=False
'''
cmd=['bash','--version']
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
     if "version" in each_line and "release" in each_line:
       print(each_line.split()[3].split('(')[0])
else:
    print("error is ",e)
