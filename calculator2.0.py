print("Welcome to the Python Calculator 2.0!")
m=input("Please Enter Your Name: ")
print("Hello",m.title(),"!!!")
print("Syntax for program: ")
print("1= addition\n2= substraction\n3= multiplication\n4= division\n5=exponential")
print("Program may crash for high values")
i=1
while (i>0):
     a=float(input("Enter a number: "))
     n=int(input("Enter the operation you want to perform: "))
     h=float(input("Enter a number: "))
     if (n==1):
         print("Addition")
         z=a+h
         print(z)
     if(n==2):
        print("Substraction")
        z=a-h
        print(z)
     if(n==3):
        print("Multiplication")
        z=a*h
        print(z)
     if(n==4):
         print("Division")
         z=a/h
         print(z)
     if(n==5):
         print("Exponential")
         z=a**h
         print(z)
        