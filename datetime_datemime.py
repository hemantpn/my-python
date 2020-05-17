#!/home/ec2-user/my_app/env/bin/python
import datetime

#import pytz    #python time zone
#"""
#datetime.datetime.now() :output of it , current time, can be use for time convetor
#datetime.datetime.today()  : current time
#"""
print(datetime.datetime.now())
print(datetime.datetime.today())


"""
we can check strftime.org to fetch data in patterns"""

print(datetime.datetime.now().month)     
print(datetime.datetime.today().year)

print(datetime.datetime.now().strftime("%c"))
print(datetime.datetime.now().strftime('%y-%m-%d'))
print(datetime.datetime.now().strftime('%y'))
