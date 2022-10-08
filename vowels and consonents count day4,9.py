def vowelsconsonents(string):
    vowels=[each for each in string if each in "aeiouAEIOU"]
    print("noof vowels:",vowels)
    consonents=[each for each in string if each not in "aeiouAEIOU"]
    print("noof consonents:",consonents)
string=input("enter any string:")
vowelsconsonents(string)
