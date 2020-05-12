#!/home/ec2-user/my_app/env/bin/python
import re
'''
findall = it picks all words but cna't check index
finditer = same work but using of it we can index
'''

my_files=("this is python python2 python3")
my_files1=("this is python2 python1 python3")

my_pat1= r"\bpython[23]?\b"
print(re.findall(my_pat1,my_files))   



print(re.finditer(my_pat1,my_files))      #OUTPUT: <callable_iterator object at 0x7f9e5b194290>
fi_1=re.finditer(my_pat1,my_files)
#we can giva condition , if patern not found it'll give a error (in case of search)

for each_ib in re.finditer(my_pat1,my_files):
    print("the match is: {each_ib.group()}")

#if fi_1: #if exist
print(fi_1.group())
#    print(fi_1.group())
#
#    print('starting index: ',fi_1.start())
#    print('ending index: ',fi_1.end()-1)
#    print('Length: ',fi_1.start()-fi_1.end()-1)
#
#else:
#    print: 'no match found'

