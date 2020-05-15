#!/home/ec2-user/my_app/env/bin/python
def get_results(value):   #parameter and positional arguments
    result=value+10
    print(f'your result is: {result}')
    return None

def main():
    num=eval(input("enter a number:  "))
    get_results(num)     #arguments
    return None

main()



