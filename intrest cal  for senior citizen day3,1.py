Principle_amount=int(input("enter the principle amount:"))
Time_period=int(input("enter number of years:"))
r=str(input("Is customer senior citizen (y/n):"))

if(r=='y'):
    SimpleIntrest1=Principle_amount*Time_period*12/100
    print("intrest is:",SimpleIntrest1)
else:
    SimpleIntrest2=Principle_amount*Time_period*10/100
    print("intrest is:",SimpleIntrest2)
