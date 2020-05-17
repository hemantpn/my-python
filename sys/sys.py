#!/home/ec2-user/my_app/env/bin/python
import sys
import datetime
'''
sys.exit()  : used to exit from scripting
sys.argv()  : used to pass some agrs ,by default index 0 is for script name
if we want some string action with argv use in ""   like:   ./scriptname "args"  action    , action like lower , upper any string action
'''

def main():
 try: 
  data="hi"
  print(sys.argv)   # comand  ./scriptname  args    ./sys.py hi jds lad 45 645
  print(len(sys.argv))
 except Exception as e:
  print(e)
  return None

if __name__=="__main__":  
    main()
#print("=================================")
#def main1():
# try:
#  user_str=sys.argv[1]
#  user_act=sys.argv[2]
#  
#  print(len(sys.argv)) 
#  if len(sys.argv) !=3
#   sys.exit()
#   if user_act =="lower":  #command ./sys.py "Hi jds laaadeQWER5 645" upper    , argv should be in string format
#    print(user_str.lower())
#
#   elif user_act =="upper":
#    print(user_str.upper())
#
#   elif user_act =="title":
#    print(user_str.title())
#
#  #else:
#   # sys.exit()
# except Exception as e:
#    print(e)
#    return None
#if __name__=="__main__":
#    main1()  
