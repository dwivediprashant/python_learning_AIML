num=int(input("Enter a non negative number : "))

if num < 0 :
    print("negative numbers have not factorial value.")

else :
    fact=1
    i=1
    while i <=num :
        fact*=i
        i+=1
    print(f"Fcatorial of {num} is : {fact}")

