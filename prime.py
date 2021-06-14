num=int(input("ENTER A NUMBER"))
i=1
c=0
while i<(num/2):
     if(num%i==0):
          c+=1
     i+=1
if(c==1):
     print("ITS A PRIME NUMBER")
else:
     print("ITS NOT A PRIME NUMBER")
     
     
