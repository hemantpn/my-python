#!/home/ec2-user/my_app/env/bin/python
#!/home/ec2-user/my_app/env/bin/pip3
import json
import os
#self.server_name = os.environ['SERVER_NAME']

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open('/home/ec2-user/ansible-environments/aws/psdev/inventory/group_vars/all', 'r') as f:
    cont = yaml.load(f.read(), Loader=Loader)

print (cont)
print(type(cont))
print(cont['abc'])
print(type(cont['abc']))
#file="all"
#fo=open(file,'r')
#print(type(fo.read()))
#
#fo.close()
print(cont.get('abc'))
