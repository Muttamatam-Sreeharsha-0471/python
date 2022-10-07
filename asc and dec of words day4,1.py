string=int(input("enter the number of words:"))
b=[]
for i in range(0,string):
    c=input("enter the word:")
    b.append(c)
print("list of words are:",b)
print("Ascending order:")
b.sort()
print(b)
c=b
print("decending order:")
c.reverse()
print(c)
