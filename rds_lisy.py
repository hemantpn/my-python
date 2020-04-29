#!/home/ec2-user/my_app/env/bin/python
mylines = []                             # Declare an empty list named mylines.
with open ('/home/ec2-user/ansible-environments/aws/psdev/inventory/hosts', 'rt') as myfile: # Open lorem.txt for reading text data.
    for myline in myfile:                # For each line, stored as myline,
        mylines.append(myline)           # add its contents to mylines.
#print(len(mylines))                           # Print the list.
#print(mylines)
#
#x=print(mylines.index('[ems_db]\n'))
#y=print(type(x))
#z=int(x)


 #   for each in mylines['[ems_db]\n']
 #       print(each)


#x=(("").join(mylines))
#print(x)
#print(mylines[6])

y=(mylines.index("[ems_db]\n"))
z=(type(y))

a=y+1
print(mylines[a].strip())


#print(x.index("ems_db"))
