#!/home/ec2-user/my_app/env/bin/python
def addition(x,y):
    print(f'add of {x} and {y}: {x+y}')
    return None

def subtractio(x,y):
    print(f"sub of {x} and {y}: {x-y}")
    return None

def main():
    try:
      a=eval(input("value of a: "))
      b=eval(input("value of a: "))
      addition(a,b)
      subtractio(a,b)
      return None
    except Exception as e:
      print(e)

if __name__=='__main__':
    main()
