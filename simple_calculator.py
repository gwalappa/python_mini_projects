##simple calculator##
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ZeroDivisionError( "error: division by zero is not allowed")
    return a/b
    
while True:
    print("-- simple calculator --")
    print("1.add")
    print("2.substract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")

    chioce=input("enter your choice(1-5): ")

    if chioce=="5":
        print("...thank you for using the calculator...")
        break

    if chioce not in {"1","2","3","4"}:
        print("invalid choice! please select between (1-5)")
        continue

    try:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))

        if chioce=="1":
            print(f"{a}+{b}={add(a,b)}")

        elif chioce=="2":
            print(f"{a}-{b}={substract(a,b)}")

        elif chioce=="3":
            print(f"{a}*{b}={multiply(a,b)}")

        elif chioce=="4":
            print(f"{a}/{b}={divide(a,b)}")

    except ValueError:
        print("invalid input! please enter a number")

    except ZeroDivisionError as e:
        print("ERROR:",e)
            
            




    