n=int(input("Enter a number : "))

count_digit=0

while n>0:
    count_digit+=1
    n//=10

print(count_digit)