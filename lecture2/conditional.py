age=int(input("Enter your age  : "))

if (age <=0):
    print("not a valid age")
elif (age<13) :
    print("child")
elif (age <=18) :
    print("teenager")
else :
    print("adult")