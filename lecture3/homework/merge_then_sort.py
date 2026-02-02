list1=[3,5,1,2,8]
list2=[7,11,23,5,2,9]

merged_list=[]

for val in list1:
    merged_list.append(val)

for val in list2:
    merged_list.append(val)

merged_list.sort(reverse=True) # decreasing order
print(merged_list)