#!/home/ec2-user/my_app/env/bin/python
import subprocess
import re

my_files=("hi this is python, it is very easy to learn")

print(my_files.split())   #will create a list

print(my_files.splitlines())

print(re.split("i[st]",my_files))
