#!/home/ec2-user/my_app/env/bin/python
''' Condition is if we put any number in caps and small, output will come in title, or no error'''

friend=input("enter ur friend name:  ")
friends=["b",'C','D',"E",'f']
friend_lower=[name.lower() for name in friends]
if friend in friends:
   print (friend)


if friend.lower() in friend_lower:
   print(friend)
