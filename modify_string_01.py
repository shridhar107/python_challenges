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

import json

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
    test_cases = {
        "tests": [
            {
                "test_string": "aaa",
                "output_string": "a3"
            },
            {
                "test_string": "abababab",
                "output_string": "a1b1a1b1a1b1a1b1"
            },
            {
                "test_string": "aaaabbbbaaacccccc",
                "output_string": "a4b4a3c6"
            }
        ]
    }

    for test_item in test_cases["tests"]:
        if get_result_str(test_item['test_string']) == test_item['output_string']:
            print('SUCCESS')
        else:
            print('FAIL')

if __name__ == '__main__':
    run_test_func()
