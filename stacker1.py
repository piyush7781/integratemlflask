class Stacking:
     def __init__(self):
          self.stack=[]
     def push(self,val):
          if len(self.stack)<5:
               self.stack.append(val)
          else:
               print("Overflow")
          self.repeat()     
     def show(self):
          print(self.stack)
          self.repeat()
     def pop(self):
          if len(self.stack)>0:
               self.stack.pop()
          else:
               print("Underflow")
          self.repeat()
     def repeat(self):
          ch=int(input("1PUSH\n2SHOW\n3POP\n4QUIT\nEnter Choice :"))
          if ch==1:
               n=int(input("Enter a number"))
               self.push(n)
          elif ch==2:
               self.show()
          elif ch==3:
               self.pop()
          elif ch==4:
               exit()
          else:
               print("Wrong Choice")
               self.repeat()
 
p=Stacking()
p.repeat()
