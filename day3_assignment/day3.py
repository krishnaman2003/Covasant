"""
flatten(lst)        Flattens the list 
                    ie input = [1,2,3, [1,2,3,[3,4],2]]
                    output = [1,2,3,1,2,3,3,4,2]
Question-13              
convert(x)          Converts like below 
                    input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
                    output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
"""

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
