#!/home/ec2-user/my_app/env/bin/python
my_string="python.sql"
try:
 print(my_string.endswith(".sql"))

 print(my_string.startswith("pyt"))

 print(dir(my_string))
except Exception as e:
 print(e)
