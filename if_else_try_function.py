
def f1(x,y):
  result1=x*y
  return result1

def f2(x,y):
  result2=x+y
  return result2

def main():
  try:
    a=eval(input("value of a:"))
    b=eval(input("value of b:"))
    res1=f1(a,b)
    res2=f2(a,b)
    if (a*b)<1000:
      print("product is:",res1)
    else:
      print("addition is:",res2)
  except Exception as e:
    print(e)
main()
