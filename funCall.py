
from additionUsingFun import add,sub,mul,div
print("Enter the first number===>")
fn=int(input())
print("Enter the second number===>")
sn=int(input())
c=add(fn,sn)
c2=sub(fn,sn)
c3=mul(fn,sn)
c4=div(fn,sn)
print("Result after adding {} and {} is {}".format(fn,sn,c))
print("Result after subtracting {} and {} is {}".format(fn,sn,c2))
print("Result after multiplying {} and {} is {}".format(fn,sn,c3))
print("Result after devision {} and {} is {}".format(fn,sn,c4))