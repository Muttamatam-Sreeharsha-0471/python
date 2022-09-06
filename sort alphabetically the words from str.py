string=str(input("enter any sentance:"))
words=[word.lower() for word in string.split()]
words.sort()
print("the sorted words are:")
for word in words:
    print(word)
