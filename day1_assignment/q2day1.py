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