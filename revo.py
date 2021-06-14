num=int(input("ENTER A 3-DIGIT NUMBER"))
i=1

a=num%10
num//=10
b=num%10
num//=10
rev=(a*100)+(b*10)+num
print(rev)
