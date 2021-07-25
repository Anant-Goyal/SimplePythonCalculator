
# This is my first project....
# I am making this project by watching a yt Video LOL....


def add(a,b):
    result=a+b
    print(result)

def sub(a,b):
    result=a-b
    print(result)

def mul(a,b):
    result=a*b
    print=(result)

def div(a,b):
    result=a/b
    print(result)

a=int(input("Please Enter The First Number"))
b=int(input("Please Enter the Second number"))

op=input("Enter the Operator (It means what you want to do + - * / ): ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)

else:
    print("Invalid Operator")

        #MadeByAnant

