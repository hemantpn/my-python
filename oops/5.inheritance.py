#!/home/ec2-user/my_app/env/bin/python
'''Encapsulation: Strict to use method and variable outside of class,whenever we define a method and variabe inside a class like __ , can't access outside of class'''
'''polymorphism: use same name of method in other class, it's ike overriding
inheritanse: can use one class methods in diff class '''
class Tomcat(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 
	def display(self):
		print(self.home)
		print(self.version)
		return None 
class Apache(Tomcat):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 
tom_ob=Tomcat('/home/tomcat9','7.6')
apa_ob=Apache("/etc/httpd",'2.4')


tom_ob.display()
apa_ob.display()
