
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):    
    c=a*b
    return c
def div(a,b):    
    c=a/b
    return c
def main():
    print("Enter first number===>")
    value1=int(input())
    print("Enter second number===>")
    value2=int(input())
    c=add(value1,value2)
    c2=sub(value1,value2)
    c3=mul(value1,value2)
    c4=div(value1,value2)
    print("Result of addition of {} and {} is==>{}".format(value1,value2,c))
    print("Result of subtraction of {} and {} is==>{}".format(value1,value2,c2))
    print("Result of multiplicaiton of {} and {} is==>{}".format(value1,value2,c3))
    print("Result of devision of {} and {} is==>{}".format(value1,value2,c4))
if __name__=="__main__":
    main()