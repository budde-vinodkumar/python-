
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.add(10)

set1.update([7, 8])
set1.remove(2)
set1.discard(100)
set1.pop()
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

difference_set = set1.difference(set2)

symmetric_diff_set = set1.symmetric_difference(set2)        
is_subset = {3, 4}.issubset(set1)
is_superset = set1.issuperset({1, 7})
set_copy = set1.copy()
set_copy.clear()
print(set1)
print(union_set)
print(intersection_set)
print(difference_set)
print(symmetric_diff_set)
print(is_subset)
print(is_superset)
