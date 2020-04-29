#!/home/ec2-user/my_app/env/bin/python
def get_addition(p,q):   #parameter and positional arguments
    result=p+q
    print(f'your result is: {result}')
    return result   #returing value of result as get_addition(a,b) and storing in result1

def main():
   try:
        a=eval(input("enter a value of a: "))
        b=eval(input("enter a value of b: "))
        result1=get_addition(a,b)     #arguments
        print(f'add of {a} and {b}: {result1}')
  #  print(f'add of {p} and {q}: {result1}')
        return None
   except Exception as e:
        print(e)
main()

print("======================exm2:=================")

def fn_out1(x):
    output=x*10
    return output
#0r we can use as  return x*10

def main1():
    try:
        value=eval(input("enter a value: "))
        final_val=fn_out1(value)
        print("final value is :",final_val)
        return None
    except Exception as e:
        print(e)
    finally:
        print("hi-hello-hi-hello")

main1()
