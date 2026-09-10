#file ko create karke ,file me content write karke ,usko close kiya hai


file=open("myfile.txt","w")
file.write("rajan:85,sahil:65,shruti:99")
file.close()

#file=open("myfile.txt","w")
#file.write("suraj:55","sameer:69","rinku:89")
#file.close()
file=open("myfile.txt","r")
#content=file.read()
#print("file content",content)
rajan=file.read()
print(rajan)



