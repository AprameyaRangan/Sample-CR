# Function to calculate the average grade for each student
def calculate_average(grades):
    return sum(grades) / len(grades)

# List to store student information
students = []

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Collect data for each student
for _ in range(num_students):
    # Get the student's name
    name = input("Enter the student's name: ")
    
    # Get the student's grades as a list of integers
    grades_input = input(f"Enter the grades for {name} (separate by spaces): ")
    grades = list(map(int, grades_input.split()))  # Convert input to list of integers
    
    # Add the student's data to the list
    students.append({"name": name, "grades": grades})

# Open a file to write the results
with open("student_averages.txt", "w") as file:
    # Loop through each student in the list
    for student in students:
        # Calculate the average grade
        average_grade = calculate_average(student["grades"])
        # Write the student's name and average grade to the file
        file.write(f"{student['name']}: {average_grade:.2f}\n")

print("Student averages have been written to 'student_averages.txt'")
