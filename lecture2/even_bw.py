def printEven(lower_limit,upper_limit):
    i=lower_limit
    while i in range(lower_limit,upper_limit+1):
        if i%2==0:
            print(i, end="  ")
        i+=1

lower_limit=int(input("Enter lower limit : "))
upper_limit=int(input("Enter upper limit : "))

printEven(lower_limit,upper_limit)