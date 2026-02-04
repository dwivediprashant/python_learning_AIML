f=open("./sample.txt","w")

# write : overwrite the file  and new changes only persist
f.write("I am new content...\n The file is overwritten now\n Hello I am new content")

f.close()