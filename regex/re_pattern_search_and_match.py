#!/home/ec2-user/my_app/env/bin/python
import re
'''
findall = it picks all words
search = it picks first word of the sequence
match = pick only starting word of the string,won't look for others line second,third ... ,other words find from 0th index

'''

my_files=("this is python python2 python3")
my_files1=("this is python2 python1 python3")

my_pat1= r"\bpython[23]?\b"
print(re.findall(my_pat1,my_files))   



print(re.search(my_pat1,my_files))      #OUTPUT: <re.Match object; span=(8, 14), match='python'>  how to store value in variable
print(re.search(my_pat1,my_files1))     #OUTPUT: <re.Match object; span=(8, 14), match='python2'>
search_1=re.search(my_pat1,my_files)
search_2=re.search(my_pat1,my_files1)
#we can giva condition , if patern not found it'll give a error (in case of search)
if search_1: #if exist

    print(search_1.group())
    print(search_2.group())

    print('starting index: ',search_1.start())
    print('ending index: ',search_1.end()-1)
    print('Length: ',search_1.start()-search_1.end()-1)

else:
    print: 'no match found'
print"----------------match--------------------"
print(re.match(my_pat1,my_files))

my_pat2= r"\bthis"
print(re.match(my_pat2,my_files))   #OUTPUT: <re.Match object; span=(0, 4), match='this'>

match_ob=re.match(my_pat2,my_files)
if search_1: #if exist 

    print(match_ob.group())

    print('starting index: ',match_ob.start())
    print('ending index: ',match_ob.end()-1)
    print('Length: ', match_ob.end()-match_ob.start())

else:
    print: 'no match found'

