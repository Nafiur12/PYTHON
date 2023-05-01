# Use of Filter Function Sorting Even & Odd
user_input= input("Enter a list of integers separated by spaces: ")
user_list= list(map(int,user_input.split()))

Odd= list(filter(lambda x: x%2==0,user_list))
Even= list(filter(lambda x: x%2!=0,user_list))
print ("User input list", user_list)
print ("Even Numbers of the list", Odd)
print ("Odd Numbers of the list", Even)