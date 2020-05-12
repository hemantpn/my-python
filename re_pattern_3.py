#!/home/ec2-user/my_app/env/bin/python
import re

my_files=("it is python3, itlearn a 342learn65 islearn veryit learn  easy to learnit")

my_pat1= "^is"
my_pat2="^i[st]"    #it'll check only from starting
print(re.findall(my_pat1,my_files))   #will create a list
print(re.findall(my_pat2,my_files))

my_pat3="learn$"  # $ to find end word of the string
#my_pat4="\w\w\w"
print(re.findall(my_pat3,my_files))

my_pat4="\\blearn"  # \b use for backspace, so we use \\b else we can use r in my_pat5 , now it'' pick only two learn which have space begining of learn will includ starting and last both have space 
print(re.findall(my_pat4,my_files))
my_pat5=r"learn\b"   
my_pat6=r"\blearn\b"
print(re.findall(my_pat5,my_files))
print(re.findall(my_pat6,my_files))
#
my_pat7=r"\Blearn\B"  #it'll pick learn with space in the begining and ending
print(re.findall(my_pat7,my_files))

my_pat8="\\bit"
print(re.findall(my_pat8,my_files))
my_pat9="\\bit\\b"
print(re.findall(my_pat9,my_files))
my_pat10="it\\b"
print(re.findall(my_pat10,my_files))
#\t,\n,\r respectively find tab find \n , ross-string
