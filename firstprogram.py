 


print("Hello, World!")
from collections import defaultdict

inventory = defaultdict(int)
inventory['apple1'] = 0
inventory['apple'] += 5
inventory['banana'] += 3
inventory['orange'] += 2
inventory['apple1'] += 10
inventory["ccc"] += "7"

print(inventory)