def convert(x):
    if isinstance(x, list):
        return [convert(element) for element in x]
    elif isinstance(x, str):
        string_list = x.strip('()').split(',')
        return [int(s) for s in string_list]
    else:
        return x
        
input_list = [[['(0,1,2)', '(3,4,5)'], ['(5,6,7)', '(9,4,2)']]]
output_list = convert(input_list)
print(output_list)
