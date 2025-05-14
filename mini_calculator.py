a= float(input("enter your first number:"))
operator= input ("enter your operator (+,-,*,/,%,//,**):")
b= float(input("enter your second number:"))

if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b) 
elif operator=="/":
    if (b!=0):
        print(a/b)
    else:
        print("error")
elif operator=="%":
    if(b!=0):
        print(a%b)
    else:
        print("error")
elif operator=="//":
    if(b!=0):
        print(a//b)
    else:
        print("error")
elif operator=="**":
        print(a**b)   
else:
    print("invalid operator")
