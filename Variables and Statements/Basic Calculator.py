print("~~~~~MINI CALCULATOR~~~~~")
num1 = float(input("Enter the First Number here :  " ))
num2 = float(input("Enter the Second Number here :  " ))

print("Press 1 For Addition")
print("Press 2 For Subtraction")
print("Press 3 For Multiplication")
print("Press 4 For Division")

choice = int(input("Enter your choice from 1-4: "))
if choice == 1:
    print(f"{num1} + {num2} = {num1+num2}")
elif choice==2:
    print(f"{num1} - {num2} = {num1-num2}")
elif choice==3:
    print(f"{num1} * {num2} = {num1*num2}")
elif choice==4:
     print(f"{num1} / {num2} = {num1/num2}"12)
else:
     print ("Invalid Input")
