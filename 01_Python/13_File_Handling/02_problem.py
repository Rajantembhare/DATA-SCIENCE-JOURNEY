file=open("data.txt","w")
file.write("the data about the student marks:")
file.write("student name:1.Rajan tembhare:35,2.sahil dahare:25,3.abhijit zingare:02")
file.close()


file=open("data.txt","r")
read=file.read()
print(read)
