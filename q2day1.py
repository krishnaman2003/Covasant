D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new': 3}

# Union of keys (value does not matter)
D_UNION = {key: D1.get(key, D2.get(key)) for key in set(D1) | set(D2)}

# Intersection of keys (value does not matter)
D_INTERSECTION = {key: D1[key] for key in set(D1) & set(D2)}

# Difference: D1 - D2 (keys in D1 but not in D2)
D_DIFFERENCE = {key: D1[key] for key in set(D1) - set(D2)}

# Merge: values are added for the same keys
D_MERGE = {key: D1.get(key, 0) + D2.get(key, 0) for key in set(D1) | set(D2)}

# Print the results
print("D_UNION =", D_UNION)
print("D_INTERSECTION =", D_INTERSECTION)
print("D1 - D2 =", D_DIFFERENCE)
print("D_MERGE =", D_MERGE)