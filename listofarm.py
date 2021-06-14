num=100
while num<1000:
     num1=num
     a=num%10
     num//=10
     b=num%10
     num//=10
     c=num
     num=(c*100)+(b*10)+a
     if ((a**3)+(b**3)+(c**3)==num1):
          print(num)
     num+=1
