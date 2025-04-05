D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new': 3}
D_UNION = D1.copy()  # Start with all keys from D1.
for key, value in D2.items():
    if key not in D_UNION:
        D_UNION[key] = value

D_INTERSECTION = {key: D1[key] for key in D1 if key in D2}
D_DIFFERENCE = {key: D1[key] for key in D1 if key not in D2}
D_MERGE = {}
for key in set(D1) | set(D2):
    D_MERGE[key] = D1.get(key, 0) + D2.get(key, 0)

print("D_UNION =", D_UNION)
print("D_INTERSECTION =", D_INTERSECTION)
print("D1 - D2 =", D_DIFFERENCE)
print("D_MERGE =", D_MERGE)
