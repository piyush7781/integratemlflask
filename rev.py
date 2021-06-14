num=int(input("ENTER A THREE-DIGIT NUMBER"))
a=num%10
num//=10
b=num%10
num//=10
rev=int((a*100)+(b*10)+num)
print("REVERSE OF THE NUMBER=",rev)
