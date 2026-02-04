# r and w  : basic read and write mode for file ;write : truncates the file first then write
# a  => [append mode]:  write content in file without overwriting file at the end

#------------Append mode (a)------------------- 
f=open("./sample.txt","a")
f.write("\nAppended content")
f.close()

#-------- x : create file and open for write and it throw error when file already exists------

f=open("./created_file.txt","x")
f.write("hello I am created by mode x")
f.close()

#------ by default file read mode is text (t) ; but some files like vid audio need to be open in bibary (b)

#------------ + :(r+ , w+ , a+) by using + we can perform read & write both opeartion at a time in file--
#---------- but there is difference in pointer location ------
# ---------NOTE : whenever raed operation performed then it returns old content bcz first changes occur in buffer then main disk file committed after f.close()

# in r+ mode pointer location at begining of file ie just before first character

f=open("./sample.txt","r+")
f.write("R+ mode written. \n")
f.close()

# in w+ mode first file is truncated means all content flushed then write happen thereafter u can read as well

f=open("./sample.txt","w+")
f.write("W+ mode written")
data=f.read()
print(data)
f.close()

# in a+ mode content is written from end and read opeartion also can be performed

f=open("./sample.txt","a+")
f.write("a+ mode written content")
data=f.read()
print(data)
f.close()
