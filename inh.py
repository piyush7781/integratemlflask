class First:
     def info(self):
          print("First Class")

class Second(First):
     def info(self):
          super().info()
          print("Second Class")


s=Second()
s.info()
