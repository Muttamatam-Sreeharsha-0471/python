def recur_factorial(n):
    if(n==1):
        return n
    else:
        return n*recur_factorial(n-1)

num=int(input("enter any number to find factorial:"))

if(num<0):
    print("please enter the positive number.")
elif(num==0):
    print("factorial for 0 is 1.")
else:
    print("the factorial of",num,"is",recur_factorial(num))
