import re

def check_input(pattern, message, error_message):
    while True:
        result_parameter = input(message)
        if not re.match(pattern, result_parameter):
            print(error_message)
        else:
            return result_parameter
