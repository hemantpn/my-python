#!/home/ec2-user/my_app/env/bin/python
def add(x=2,y=2): #default variable also write as add(x,y=2) if same value
    print(x+y)
    return None

add()
add(4,5)
add(10,23)

print("=================exm2===================")

def my_sql_user(user="root"):
    try:
      print(f"working with {user}")
      return None
    except Exception as e:
      print(e)

my_sql_user()
my_sql_user("hemant")
