num=int(input("Enter a number : "))

# if (num % 2==0):
#     print(f"{num} is even number.")
# else :
#     print(f"{num} is odd number.")

# without modulo --------------- can be extended for negative inputs as well

copy=num

if (num <0 ):
    while(copy!=1 and copy!=0) :
        copy+=2
else :
    while(copy!=1 and copy!=0) :
        copy-=2


if(copy==0) :
    print(f"{num} is even number.")
else :
    print(f"{num} is odd number.")