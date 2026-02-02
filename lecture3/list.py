marks=[43,56,90,89,98,37,"prahsnat",99.99] # mutable and contain multiple type of values

print(len(marks))
print(marks)
print(marks[0])
print(marks[:2])


# list methods
marks.append(2000)
marks.insert(1,1000)

nums=[2,3,1,7,6,4]
nums.sort()
nums.reverse()

for val in nums :
    print(val,end=" ")
print(nums)