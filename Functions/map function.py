# Making a list of squares of a user input list using map amd lamda function
user_input = input("Enter a list of integers separated by spaces: ")
user_list = list(map(int, user_input.split()))

# Use the map function to create a new list of squares
squares_list = list(map(lambda x: x**2, user_list))

# Print the list of squares
print ("User input list", user_list)
print("List of squares:", squares_list)
