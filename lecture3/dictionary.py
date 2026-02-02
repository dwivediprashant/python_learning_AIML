info={
    "name":"prashant",
    "subjects":["hindi","eng","sicence","maths"],
    "marks":[98,45,67,89,36],
    "age":22,
    "jee-score":83.12
}

#  access values by keys
print(info["name"]) # for non exixting key in dictionary this give error
print(info.get("cgpa"))  # for non exixting key in dictionary this give None type value

# keys 
print(info.keys())
# values 
print(info.values())
# key : value pairs
print(info.items())

## update values

info.update({
    "age":20, # existing key will be updated with new val
    "city":"bhopal"  # non existing key will add on dict
})

print(info)