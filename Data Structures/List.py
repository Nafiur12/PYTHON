#Find The values in a list which is greater than a user input value.
list = input("Enter a list of numbers separated by commas: ").split(",")
num = int(input("Enter a number to compare: "))

# convert list of strings to list of floats
list = [int(i) for i in list]

# create a new list with only numbers greater than num
greater_nums = [i for i in list if i > num]

# print the result
print("Numbers greater than", num, "in the list are:", greater_nums)
