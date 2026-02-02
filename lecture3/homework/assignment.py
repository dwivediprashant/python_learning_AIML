# given a list info containing tuples of  name and subject

info=[
    ("prashant","maths"),
    ("sumit","eng"),
    ("adesh","maths"),
    ("hardik","science"),
    ("shivam","bio"),
    ("sikhar","bio"),
    ("shivam","eng"),
    ("prashant","bio"),
    ("sita","eng"),
    ("aman","eng"),
    ("aman","bio"),
    ("prashant","eng"),
]

# q1 : list all unique courses

# sol 1
unique_sub=set()

for val in info :
    unique_sub.add(val[1])

# print(unique_sub)

# sol 2

sub=[]
for val in info:
    if val[1] not in sub :
        sub.append(val[1])

# print(sub)

# q2 : list students enrolled in english

eng_stu=[]

for val in info:
    if val[1]=="eng":
        eng_stu.append(val[0])

# print(eng_stu)

# q3 : create dictionary (student,set of courses)

stu_dict={}
for name,course in info:
    if name not in stu_dict:
        stu_dict.update({
            name:set()
        })
    stu_dict[name].add(course)
print(stu_dict)