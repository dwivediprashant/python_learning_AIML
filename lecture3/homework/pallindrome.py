string=input("Enter a string : ")

ptr1=0
ptr2=len(string)-1
isPallindrome=True
while ptr1<=ptr2:
    if(string[ptr1]!=string[ptr2]):
        isPallindrome=False
        print(f"{string} is not a pallindrome.")
        break
    ptr1+=1
    ptr2-=1

if isPallindrome:
    print(f"{string} is pallindrome.")

