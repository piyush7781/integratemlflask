n=int(input("ENTER A NUMBER"))
i=1
sum=0
while n>0:
     i=n%10
     sum+=i
     n//=10
print(sum)     
