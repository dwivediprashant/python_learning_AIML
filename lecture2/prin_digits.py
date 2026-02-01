num=int(input("Enter a number : "))

def print_digit(num):
    while num > 0:
        rem=int(num%10)
        print(rem, end=" ")
        num=int(num/10)

print_digit(num)