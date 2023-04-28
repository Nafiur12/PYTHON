from math import *

Voltage= float (input("Enter The value of Voltage (in voltmetre)=  "))
x= float (input("Enter The value of Voltage Phase angle=  "))
Current= float (input("Enter The value of Current (in ampere}=  "))
y= float (input("Enter The value of Current Phase angle=  "))
ang= (x-y)*(3.1416/180)
P= (Voltage*Current)*cos(ang);
Q= (Voltage*Current)*sin(ang);
S= Voltage*Current;
F= cos(ang);
print("The Real power is", P ,"Watt");
print("The Reactive power is",  Q , "Var")
print("The Apparent power is", S , "VA")
print("The Power Factor is", F)
if y>x :
    print("The Power Factor is leading")
else:
    print("The Power Factor is lagging")
