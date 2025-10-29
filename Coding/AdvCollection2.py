from collections import defaultdict

# inventory = defaultdict(int)
# inventory['apple'] += 5
# inventory['banana'] += 3

# grouped = defaultdict(list)
# data = [('A', 1), ('B', 2), ('A', 3), ('B', 4), ('A', 5)]
# for k, v in data:
#     grouped[k].append(v)
# print(grouped)

from collections import ChainMap
defaults = {'theme': 'light', 'language': 'English'}
user = {'theme': 'dark'}

settings = ChainMap(user, defaults)
print(settings['theme'])
print(settings['language'])
admin = {'access': 'admin'}
combined = settings.new_child(admin)
print(combined)
