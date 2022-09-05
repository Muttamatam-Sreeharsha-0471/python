c=int(input("enter your marks in c:"))
cpp=int(input("enter your marks in cpp:"))
python=int(input("enter your marks in python:"))
java=int(input("enter your marks in java:"))

avg_marks=(c+cpp+python+java)/4;

if(avg_marks>=90):
    print("Your Grade is S.")
elif(avg_marks<90 and avg_marks>=80):
    print("Your Grade is A.")
elif(avg_marks<80 and avg_marks>=70):
    print("Your Grade is B.")
elif(avg_marks<70 and avg_marks>=60):
    print("Your Grade is C.")
elif(avg_marks<60 and avg_marks>=50):
    print("Your Grade is D.")
elif(avg_marks<50 and avg_marks>=40):
    print("Your Grade is E.")
else:
    print("You Are Fail.")

print("Your average marks is:",avg_marks)
