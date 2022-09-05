A=int(input("Give a value to A:"))
B=int(input("Give a value to B:"))
C=int(input("Give a value to C:"))

if(A>B and A>C):
    print("The greatest number is:",A)
elif(B>A and B>C):
    print("The greatest number is:",B)
else:
    print("The greatest number is:",C)
