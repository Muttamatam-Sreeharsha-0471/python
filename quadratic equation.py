import cmath

a=int(input("enter the a value:"));
b=int(input("enter the b value:"));
c=int(input("enter the c value:"));

d=(b**2) - (4*a*c)

solution1=(-b-cmath.sqrt(d))/(2*a)
solution2=(-b+cmath.sqrt(d))/(2*a)

print("the two solution are :-")
print(solution1)
print(solution2)
