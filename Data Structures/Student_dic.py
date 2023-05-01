# Initialize an empty dictionary to store the data
students = {}

# Loop through five times to get data for five students
for i in range(5):
    # Get user input for name, roll, and CGPA
    name = input("Enter name of student {}: ".format(i + 1))
    roll = input("Enter roll number of student {}: ".format(i + 1))
    cgpa = float(input("Enter CGPA of student {}: ".format(i + 1)))

    # Create a nested dictionary to store the data for this student
    student_data = {'name': name, 'roll': roll, 'cgpa': cgpa}

    # Add the student data to the main dictionary using the number as the key
    students[i+1] = student_data

# Print the final dictionary
print(students)
