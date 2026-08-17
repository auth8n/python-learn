#Creating sets
numbers = {1,2,3}
empty_set = set()

#Add or remove elements
numbers.add(4)

try:
    numbers.remove(5)
except(KeyError):
    print("Value does not exist")

numbers.discard(5)

#Set operations
set_a = {1,2,3,4,5}
set_b = {2,4,5,6,7,8}

#Union, intersection, difference, symmetric difference
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))

print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))
print(set_a.isdisjoint(set_b))