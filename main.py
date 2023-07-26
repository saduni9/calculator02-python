def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)

def power(a,b):
   return a**b

def remainder(a,b):
   return a%b

def select_op(choice, history):
    if (choice == '#'):
        print("Done. Terminating")
        exit()
    elif (choice == '$'):
        return main()
    elif (choice in ('+','-','*','/','^','%')):
        while (True):
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return main()
            if num1s.endswith('#'):
                print("Done. Terminating")
                exit()
            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        while (True):
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return main()
            if num2s.endswith('#'):
                print("Done. Terminating")
                exit()
            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        if choice == '+':
            result = add(num1, num2)
            msg="{0} {1} {2} = {3}".format(str(num1), str(choice), str(num2), str(result))
            print(msg)
            history.append(msg)
        elif choice == '-':
            result = subtract(num1, num2)
            msg="{0} {1} {2} = {3}".format(str(num1), str(choice), str(num2), str(result))
            print(msg)
            history.append(msg)
        elif choice == '*':
            result = multiply(num1, num2)
            msg="{0} {1} {2} = {3}".format(str(num1), str(choice), str(num2), str(result))
            print(msg)
            history.append(msg)
        elif choice == '/':
            result =  divide(num1, num2)
            msg="{0} {1} {2} = {3}".format(str(num1), str(choice), str(num2), str(result))
            print(msg)
            history.append(msg)
        elif choice == '^':
            result = power(num1, num2)
            msg="{0} {1} {2} = {3}".format(str(num1), str(choice), str(num2), str(result))
            print(msg)
            history.append(msg)
        elif choice == '%':
            result = remainder(num1, num2)
            msg="{0} {1} {2} = {3}".format(str(num1), str(choice), str(num2), str(result))
            print(msg)
            history.append(msg)
        else:
            print("Something Went Wrong")
    elif choice=='?':
        if len(history) ==0:
            print("No past calculations to show")
        else:
            b="\n".join(history)
            print(b)
    else:
        print("Unrecognized operation")
        return main()

def main():
    history = []
    while True:
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")
        print("8.History  : ? ")

        # take input from the user
        choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
        print(choice)
        select_op(choice, history)
