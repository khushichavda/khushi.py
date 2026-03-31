#write()-write a single string
f=open("1.txt","w")
f.write("hello student\n")
f.write("welcome to python file handling.\n")
f.write("learning is fun.\n")
f.close()

#example 2
f=open("1.txt","w")
f.write("new content only.\n")
f.close()

#writelines()-write multiple lines
f=open("1.txt","w")
line=[
    "python progaraming\n"
    "file handling\n"
    "error handling\n"
    "exception handing\n"
]
f.writelines(line)
f.close()