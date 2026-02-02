# tuples are same as list only difference is that tuples are immutable like strings

marks=(2,3,3,3,2,4,23,10,4,23)
# marks[0]=8  -- give error bcz tuples are immutable
print(marks)
print(marks[:])
first_occur=marks.index(23)
print(first_occur)

total=marks.count(23)
print(total)

# nums=(1) -- not a valid declaration for single tuple it act as type of val in () parenthesis

nums=(1,)

print(type(nums))