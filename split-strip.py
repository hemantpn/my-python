#!/home/ec2-user/my_app/env/bin/python
y="python"
x='python is easy'
z="   scripting"


print(z)
print(z.strip())   #it'll remove space

print(y.strip('n'))
print(y.strip('p'))   #it can remove only starting word and last
print(x.strip('easy'))

print("=========left-right strip============")

x="pythonyy"
y="pppythonnnn"
z="       ppythonppp"

print(z.strip(''))
print(y.lstrip('p'))
print(y.rstrip('n'))
print(x.strip('y'))

print(x.strip('y').strip('n'))


print("=========split: output will be in List============")

x="python is easy"
y="python is easy. it is very imp"

print(x.split())
print(y.split('is'))
