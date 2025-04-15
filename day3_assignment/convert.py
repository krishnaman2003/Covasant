"""
Question-13              
convert(x)          Converts like below 
                    input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
                    output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
"""

def convert(data):
    if type(data) is list:
        return [convert(item) for item in data]
    elif type(data):
        string_list = data.strip('()').split(',')
        return [int(i) for i in string_list]
    else:
        return data
        
input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
output = convert(input)
print(f"Output: {output}")
