tup=(2,3,5,1,8,4,6,7,10)

even_tup=()
odd_tup=()

# print(type(even_tup))
for val in tup:
    if val%2==0:
        even_tup+=(val,)
    else:
        odd_tup+=(val,)

print(odd_tup)
print(even_tup)