#!/home/ec2-user/my_app/env/bin/python
import getpass

"""
getpass() : prompts the user for a password without echoing, the getpass module provides a secure way to handle the password prompts where programs interact with the user via the terminal

getuser() : Function displays login name of the user. This function checks the environment variables LOGNAME , USER , LNAME and USERNAME in Order and resturn the value of the first non-empty-string
"""

x = getpass.getpass()   # by default the output prompt as a password
print(x)

y = getpass.getpass(prompt="please enter your password: ")   #the output prompt please enter your password
print(y)

print("output comes automatically")

z=getpass.getuser()  #first it finds LOGNAME , USER , LNAME and USERNAME in Order
print(z)
