#Write a Python program to create a dictionary from a string.

string = input("Enter a string: ")

# Create an empty dictionary
dictionary = {}

# Loop through each character in the string
for char in string:

    # Check if the character already exists in the dictionary
    if char in dictionary:

        # If it exists, increment the count by 1
        dictionary[char] += 1

    else:

        # If it doesn't exist, add it to the dictionary with a count of 1
        dictionary[char] = 1

# Print the resulting dictionary
print(dictionary)
