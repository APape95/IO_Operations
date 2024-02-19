# Write a program that allows a user to register students for an exam venue.
# First ask the user how many students are registering.
# Create a for loop that runs for that number of students.
# Each time the loop runs the program should ask the user to enter student ID.
# Write each student ID number to a text file called reg.form.txt
# Include a dotted line after each student ID.
# This doc will be used as an attendence registar.

# Open the file we are going to write to.
file1 = open("reg_form.txt", "w")
# Get the input from the user for how many students.
num_students = int(input("How many students are registering?"))
# Loop until the number of students is 0.
while num_students > 0:
    # Every time it loops take 1 off the number of students.
    num_students = num_students - 1
    # Get the info off the user for student ID.
    # Write this to the file with a new line after
    # Writing a line of **** after each ID so student can sign.
    student_ID = input("Please enter student ID")
    file1.write(f"{student_ID}\n")
    file1.write("*******************\n")
file1.close()