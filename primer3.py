num=int(input("ENTER A NUMBER"))
cnt=0
for i in range(1,num+1):
     if(num%i==0):
          cnt+=1
if(cnt==2):
     print("ITS A PRIME NUMBER")
else:
     print("ITS A COMPOSITE NUMBER")
