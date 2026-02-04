f=open("./sample.txt","r") # f is file object reference/pointer
data=f.read()
print(data)
print("--Line read--")
line1=f.readline() # here we can see no data will print bcz f pointer has been moved to end as we did f.read() then we r trying to raed line but no line remain to read
print("Line : ",line1)
f.close()