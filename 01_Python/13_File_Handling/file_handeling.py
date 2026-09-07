#What is File Handling?
#File handling means performing operations on files such as:

#1.Create a file
#2.Open a file

#3.Read data from a file

#4.Write data into a file

#5.Close a file

#Python provides a built-in function open() to work with files.

#File Modes in Python
#When opening a file, you specify a mode:

#"r" → Read (default mode)

#"w" → Write (creates new file or overwrites existing)

#"a" → Append (adds data at the end)

#"x" → Create (fails if file already exists)

#"b" → Binary mode (for images, videos, etc.)

#"t" → Text mode (default)

# Basic Example
#python
# Writing to a file
file = open("example.txt", "w")
file.write("Hello, this is my first file handling program!")
file.close()

# Reading from a file
file = open("example.txt", "r")
content = file.read()
print("File Content:", content)
file.close()

 
# Writing student marks into a file
with open("marks.txt", "w") as f:
    f.write("Rajan: 85\n")
    f.write("Sneha: 90\n")
    f.write("Amit: 78\n")

# Reading student marks from the file
with open("marks.txt", "r") as f:
    data = f.readlines()

print("Student Marks:")
for line in data:
    print(line.strip())
 

 
 