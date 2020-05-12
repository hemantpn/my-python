#!/home/ec2-user/my_app/env/bin/python
'''Encapsulation: Strict to use method and variable outside of class,whenever we define a method and variabe inside a class like __ , can't access outside of class'''
class Person(object):
	def assing_name_and_age(self,name,age):
		self.name=name
		self.__age=age     #can't use this variable in another class
		self.__display()
		return None
	def __display(self):      #can't use this method(function) in another class
		print(self.name,self.__age)
		return None

per1=Person()
per1.assing_name_and_age('John',32)

#per1.__display() #will through a error
#print(per1.name)
#print(per1.__age)  #will through a error
