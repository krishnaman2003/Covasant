"""
Question-2: 
Given:D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
Create below:
# union of keys, #value does not matter
D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
# intersection of keys, #value does not matter
D_INTERSECTION = {'ok': 1}
D1- D2 = {'nok': 2 }
#values are added for same keys
D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3  }
"""

d1 = {'ok': 1, 'nok': 2}
d2 = {'ok': 2, 'new': 3}

d_union = d1.copy()
for key, val in d2.items():
    if key not in d_union:
        d_union[key] = val
print(f"D_UNION = {d_union}")

d_intersection = {key: d1[key] for key in d1 if key in d2}
print(f"D_INTERSECTION = {d_intersection}")

d_difference = {key: d1[key] for key in d1 if key not in d2}
print(f"D1 - D2 = {d_difference}")

d_merge = d1.copy()
for key, val in d2.items():
    d_merge[key] = d_merge.get(key, 0) + val
print(f"D_MERGE = {d_merge}")
print(f"D_MERGE = {d_merge}")
