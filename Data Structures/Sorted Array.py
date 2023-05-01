# Get user input for array of numbers
arr = input("Enter an array of numbers (separated by spaces): ").split()
arr = [int(num) for num in arr]

# Sort array in ascending order
arr_asc = sorted(arr)

# Sort array in descending order
arr_desc = sorted(arr, reverse=True)

# Print the sorted arrays
print("Array in ascending order", arr_asc)
print("Array in descending order", arr_desc)
