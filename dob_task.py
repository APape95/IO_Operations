# Write a program that reads the data from the text file provided (DOB.txt).
# And prints out in two different sections in the format displayed below.

# Name
# Orville Wright
# Rogelio Holloway
# Marjorie Figueroa

# Birthdate
# 21 July 1988
# 13 September 1988
# 9 October 1988
# ect...

# Open the file.
file1 = open("DOB.txt")
# Printing the heaading for the first section of data.
print("Name")
# Loop for as many lines in the data and split then into words.
# Print the first two words as these are the first and last names.
for line in file1:
    words = line.split()
    print(words[0:2])
# Print a blank space to leave a line before next set of data.
print("")
# Closing the file once first data taken.
file1.close

# Open the file this time printing after 2nd word to end to show the DOB
file1 = open("DOB.txt")
print("Birthdates")
for line in file1:
    words = line.split()    
    print(words[2:])