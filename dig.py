num=int(input("ENTER A THREE-DIGIT NUMBER"))
a=num%10
num//=10
b=num%10
num//=10
sum=int(a+b+num)
print("SUM OF THE DIGITS=",sum)
