from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange']
countfruits = Counter(fruits)
print("Initial Count:")
print(countfruits)

print("Most common fruit:")
print(countfruits.most_common(1))
countfruits.update({'banana':1, 'pear':2})
print("Updated Count:")
print(countfruits)