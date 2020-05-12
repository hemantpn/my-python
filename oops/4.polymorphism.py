#!/home/ec2-user/my_app/env/bin/python
'''polymorphism: use same name of method in other class, it's ike overriding
inheritanse: can use one class methods in diff class '''
class Tomcat(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 
	def display(self):
		print("This is from tocmat class")
		print(self.home)
		print(self.version)
		return None 
class Apache(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 
	def display(self):
		print("This is from apache class")
		print(self.home)
		print(self.version)
		return None 

tom_ob=Tomcat('/home/tomcat9','7.6')
apa_ob=Apache("/etc/httpd",'2.4')

tom_ob.display()
apa_ob.display()
