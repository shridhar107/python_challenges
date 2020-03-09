# Python CHALLENGE
'''
Modify the given string

Examples:
    Example-1 
        Input:
            aaa
        Output:
            a3
    Example-2:
        Input:
            aaaabbbbaaacccccc
        Output:
            a4b4a3c6

Modify funnction 'get_result_str' such that it provides output string for given input string
'''

def get_result_str(test_string):
    # print(test_string)
    output_string_list = ''
    count_char = 1
    prev_char = ''
    for item in list(test_string):
        if prev_char != item:
            if len(output_string_list) != 0:
                output_string_list += str(count_char)
            output_string_list += item
            count_char = 1
        else:
            count_char += 1
        prev_char = item
    output_string_list += str(count_char)
    # print(output_string_list)
    return output_string_list

def run_test_func():
    a, b = 'SUCCESS', 'FAIL'
    print({True:a , False:b } [get_result_str('aaa') == 'a3'])
    print({True:a , False:b } [get_result_str('abababab') == 'a1b1a1b1a1b1a1b1'])
    print({True:a , False:b } [get_result_str('aaaabbbbaaacccccc') == 'a4b4a3c6'])


if __name__ == '__main__':
    run_test_func()
