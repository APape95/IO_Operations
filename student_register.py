# Write a program that allows a user to register students for an exam venue.
# First ask the user how many students are registering.
# Create a for loop that runs for that number of students.
# Each time the loop runs the program should ask the user to enter student ID.
# Write each student ID number to a text file called reg.form.txt
# Include a dotted line after each student ID. 
# This doc will be used as an attendence registar, which the students will sign.

file1 = open("reg_form.txt", "w")
num_students = int(input("How many students are registering?"))
while num_students > 0:
    num_students = num_students - 1
    student_ID = input("Please enter student ID")
    file1.write(f"{student_ID}\n")
    file1.write("************\n")