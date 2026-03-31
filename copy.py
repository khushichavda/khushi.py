#copy content from one file to anoter
#read  from source file
src=open("1.txt","r")
data=src.read()
src.close()

dst=open("2.txt","w")
dst.write(data)
dst.close()
print("file copied successfully")
