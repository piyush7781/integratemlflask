num=int(input("ENTER A 3-DIGIT NUMBER"))
num1=num
a=num%10
num//=10
b=num%10
num//=10
if num1==((a**3)+(b**3)+(num**3)):
     print("YES,ITS AN ARMSTRONG NUMBER")
else:
     print("NO,IT IS NOT AN ARMSTRONG NUMBER")
     
