class Father:
    first_name="Adhish"
    last_name="Dwivedi"

class Son(Father):
    first_name="Prashant"

s1=Son()
print(s1.last_name) # son inheriting last name from parent(father)