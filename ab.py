#!/home/ec2-user/my_app/env/bin/python
import re
def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
           print(i)
           for j in range(0,k):
               print(end=" ")
          # k = k - 1
          # for j in range(0, i+1):
          #      print("*", end=" ")
          # print("\r")
 
pattern(5)
print('===================')
def pattern(n):
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x += 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")

pattern(5)