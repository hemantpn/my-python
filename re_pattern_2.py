#!/home/ec2-user/my_app/env/bin/python
import re

my_files=("hi this is python3, it  learn a 34265 is very easy to learn")

my_pat1= "is"
my_pat2="i[st]"
print(re.findall(my_pat1,my_files))   #will create a list
print(re.findall(my_pat2,my_files))

my_pat3="\w"  #will include every word in sentence
my_pat4="\w\w\w"
print(re.findall(my_pat3,my_files))
print(re.findall(my_pat4,my_files))

my_pat5="\W"   #matches any character not part of \w
my_pat6="\W\W"
print(re.findall(my_pat5,my_files))
print(re.findall(my_pat6,my_files))

my_pat7="\d"  #numeric character
my_pat8="python\d"
my_pat9="\d\d"
print(re.findall(my_pat7,my_files))
print(re.findall(my_pat8,my_files))

print(re.findall(my_pat9,my_files))

my_pat10="."  #all characters except new line \ includeing  space
print(re.findall(my_pat10,my_files))
