queue=[]
def push(queue,val):
     if len(queue)<5:
          queue.append(val)
     else:
          print("Overflow")
def show(queue):
     print(queue)

def pop(queue):
     if len(queue)>0:
          queue.pop(0)     
     else:
          print("Underflow")
while True:
     ch=int(input("1PUSH\n2SHOW\n3POP\n4QUIT\nEnter Choice :"))
     if(ch==1):
          n=int(input("Enter a number"))
          push(queue,n)

     elif(ch==2):
          show(queue)
     elif(ch==3):
          pop(queue)
     else:
          break

