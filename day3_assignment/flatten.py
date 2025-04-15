def flatten(lst):
  flatten_lst = []
  for item in lst:
    if type(item) is list:
      flatten_lst.extend(flatten(item))
    else:
      flatten_lst.append(item)
  return flatten_lst

input = [1,2,3, [1,2,3,[3,4],2]]
output = flatten(input)
print(f"Output: {output}")