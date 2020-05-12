#!/home/ec2-user/my_app/env/bin/python
class Emp(object):
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		return None
	def display(self):
		print(f"The name is: {self.name}\nThe salary is: {self.salary}")
		return None		


emp1=Emp('Ramu',56000)
emp2=Emp("Naren",90000)

'''emp1.def __init__('Ramu',56000)  #No need to define like this , if we use init,   in case we don't use then we have to define like this'''

emp1.display()
#emp2.display()
