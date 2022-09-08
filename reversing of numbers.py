try:
    n=int(input("enter any number:"))
    org=n
    sum=0
    while(n>0):
        a=n%10
        sum=sum*10+a
        n=n//10
    print("reverse of the numbers is:",sum)    
except ValueError:
    print("enter the input as integer values only.")
