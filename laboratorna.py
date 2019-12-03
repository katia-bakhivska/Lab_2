text = str(input("Enter text: "))
aoption = "a- count words "
boption = "b - sort in alphabet "
print(aoption)
print(boption)
myop = input("Choose option: ")
text=text.lower()
if myop =="a":
    result = len(text.split())
    print("Text consist of "+str(result))
else:
    if myop == "b":
        words = text.split()
        words.sort()
        print("The sorted words are: ")
        for word in words:
            print(word)
    else:
        if myop!="a" or myop!="b":
            print("false")