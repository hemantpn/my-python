#!/home/ec2-user/my_app/env/bin/python
y="python"
x='python is easy'
z="   scripting"
z1="   scripting    "

print(z)
print(z1.strip())   #it'll remove space from starting and end

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

""" Output:
   scripting
scripting
pytho
ython
python is
=========left-right strip============
       ppythonppp
ythonnnn
pppytho
python
pytho
=========split: output will be in List============
['python', 'is', 'easy']
['python ', ' easy. it ', ' very imp']
(env) [ec2-user@hemant-test my-python]$ q
-bash: q: command not found
(env) [ec2-user@hemant-test my-python]$ vi split-strip.py
(env) [ec2-user@hemant-test my-python]$ ./split-strip.py
   scripting
scripting
pytho
ython
python is
=========left-right strip============
       ppythonppp
ythonnnn
pppytho
python
pytho
=========split: output will be in List============
['python', 'is', 'easy']
['python ', ' easy. it ', ' very imp']

"""
