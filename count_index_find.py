#!/home/ec2-user/my_app/env/bin/python
x= "this is python and it is very popular language"

print(x.count("is"))   #to check how-many times
print(x.count("p"))
print(x.count("i"))


print(x.index('i'))  #for index  we can find , find is better option it won't show any errro if number not exist

print(x.index('i',2))
print(x.index('i',3))
print(x.index('i',6))
print(x.index('i',20))
'''print(x.index('i',23))'''


print(x.find('i',6))     #if wornd doesn't exist aftert the indea it shows negatiove value not error
print(x.find('i',20))
print(x.find('i',23))

y= "python version is 3.7"
print(y.find('python'))
print(y.find('version')) #it'll show index of first word v, 
print(y.find('jave'))  #instead of error will show -1
