#!/home/ec2-user/my_app/env/bin/python
import re

my_files=("xa xz xaz addaaa pythonnn  pythonnnnnq xaaaaz xaaaz xaasza xaaazd")
#print(re.findall(my_pat10,my_files))

my_pat1= r"\bpythonnnnn\b"
my_pat2= r"\bpython{5}q\b"   
print(re.findall(my_pat1,my_files))   
print(re.findall(my_pat2,my_files))

my_pat3=r"\bpython{1,5}"   #it'll find 1 to 5 time words  , here n
my_pat4=r"\bpython{1,}q\b"    #it'll find 1 to more times 2,3,4....
my_pat5=r"\bpython+q\b"    #it'll find 1 to more times 2,3,4....
print(re.findall(my_pat3,my_files))
print(re.findall(my_pat4,my_files))
print(re.findall(my_pat5,my_files))


my_pat6="xa*z"   #it'll find 0 to more times 2,3,4....
print(re.findall(my_pat6,my_files))

my_pat7="xa?z"   #  #it'll find 0 or 1 time
print(re.findall(my_pat7,my_files))

'''
{2} = exactly 2 times, {3}= exactly 3 times
{2,4} = exactly 2,3,4 times
{1,} = 1 or more time
+   =  1 or more time
*  = 0 or more times
?  = 0 to 1 time
'''
