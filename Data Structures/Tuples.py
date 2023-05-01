# Modify a Tuple using list
my_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a list
my_list = list(my_tuple)

# Modify the list
my_list[2] = 30
my_list.append(6)

# Convert the list back to a tuple
my_tuple = tuple(my_list)

# Print the modified tuple
print(my_tuple)
