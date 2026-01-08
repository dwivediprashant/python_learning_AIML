#  fnx definition
def largest_of_three(x,y,z):
    if x > y :
        if x > z :
            print("largest : " , x)
        else :
            print("largest : " , z)
    else :
        if y > z :
            print("largest : " , y)
        else:  
            print("largest : " , z)

# fnx call
largest_of_three(2,2,4)