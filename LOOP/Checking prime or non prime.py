#Checking Prime or Non Prime
n= int(input("Enter the Number you want to check: "))

i=2
count=0
while i<n :
    if n%i==0:
        count+=1
        break
    i+=1
if count ==1 :
    print(n,"is not Prime" )
else:
    print(n,"is Prime")