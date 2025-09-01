class simplecal():
   def add(self,a,b):
    print(a+b)

   def sub(self,a,b):
    print(a-b)

   def mul(self,a,b):
    print(a*b)

   def div(self,a,b):
    print(a/b)

   def mod(self,a,b):
    print(a%b)

   def flrdiv(self,a,b):
    print(a//b)

   def exp(self,a,b):
    print(a**b)
    
   def describe(self):
    print("model number",self.model_no)
    print("made in",self.made_in)
    print("color",self.color)
    print("discount",self.discount)

cal1=simplecal()
cal2=simplecal()

cal1.model_no="0001"
cal1.made_in="India"
cal1.color="Blue"
cal1.discount="10%"

cal2.model_no="0002"
cal2.made_in="America"
cal2.color="Red"
cal2.discount="15%"

cal1.add(20,30)
cal1.sub(12,13)
cal1.mul(23,44)
cal1.div(2,3)
cal1.mod(29,7)
cal1.flrdiv(10,30)
cal1.exp(20,3)
cal1.describe()


cal2.add(2,3)
cal2.sub(12,15)
cal2.mul(23,5)
cal2.div(20,30)
cal2.mod(20,7)
cal2.flrdiv(10,12)
cal2.exp(12,3)
cal2.describe()

