# sets : collection of unique elements and elements in sets must be immutable in nature
# sets are mutable itself but elemnts inside it must be immutable means list + dictionary can not be part of sets
# sets are unordered means no indexing possible in sets


# declaration

# my_set={"hello",34,21,3,14,[45,56,47]} # give error bcz list is ele of set and list is mutable in nature

my_set={34,23,"prashant",3.14,99,99} ## duplicate values can be put inside set but it will be treated as one/single

print(my_set)

# empty_set={} # this is not a valid declaration of empty set bcz its a dict

# print(type(empty_set)) # dictionary type

empty_set=set() # this creatre empty set


# sets methods

s1={1,5,3,4,10,9}
s2={2,5,4,9}


union_set=s1.union(s2)
intersect_set=s1.intersection(s2)
print(intersect_set)
print(union_set)


s1.add(20) # to add val in set
s1.remove(9) # give error for non existing val in set
pop_ele=s1.pop() # remove random val from  set
print(pop_ele)
print(s1)