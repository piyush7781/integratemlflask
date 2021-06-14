stack=[]
def push(stack,val):
     if len(stack)<5:
          stack.append(val)
     else:
          print("Overflow")
i=1
def show(stack):
     print(stack)

def pop(stack):
     if len(stack)>0:
          stack.pop()
     else:
          print("Underflow")
while True:
     ch=int(input("1PUSH\n2SHOW\n3POP\n4QUIT\nEnter Choice :"))
     if(ch==1):
          n=int(input("Enter a number"))
          push(stack,n)

     elif(ch==2):
          show(stack)
     elif(ch==3):
          pop(stack)
     else:
          break

