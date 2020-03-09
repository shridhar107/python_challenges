# Python CHALLENGE
'''
Modify function 'get_result_str' such that it provides output string for given input string
Example-1 
    Input:  'aaa'
    Output: 'a3'
Example-2:
    Input:  'aaaabbbbaaacccccc'
    Output: 'a4b4a3c6'
'''

def get_result_str(input_string):
    # print(input_string)
    prev_char = output_string = ''
    count_char = 1
    for char_ in list(input_string):
        if prev_char != char_:
            if len(output_string) != 0: output_string += str(count_char)
            output_string += char_
            count_char = 1
        else:
            count_char += 1
        prev_char = char_
    output_string += str(count_char)
    # print(output_string)
    return output_string

def run_test_func():
    print({True:'SUCCESS', False:'FAIL'} [get_result_str('aaa') == 'a3'])
    print({True:'SUCCESS', False:'FAIL'} [get_result_str('abababab') == 'a1b1a1b1a1b1a1b1'])
    print({True:'SUCCESS', False:'FAIL'} [get_result_str('aaaabbbbaaacccccc') == 'a4b4a3c6'])

if __name__ == '__main__':
    run_test_func()
