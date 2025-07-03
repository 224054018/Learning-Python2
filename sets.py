#sets: Unbothered collection of unique elements, unlike lists or tuples, sets do not allow duplicates use
# sets are useful when you  want to perfom operations like union intersection and the difference between 
# collections of elements... Are un ordered but imutable can add and remove  but don't allow for duplicates
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union
union_set = set1.union(set2)
print(union_set)

#intersection
inter_set = set1.intersection(set2)
print(inter_set)

#difference
diff_set = set1.difference(set2)
print(diff_set)

#Sets are used for when you need to work with collections of unique elements to perform operations like finding 
# intersections, differences, or unions between sets some common use sets to remove duplicates from a list or 
# collection checking membership efficient and others