from generate_password import generate_password
from utils.check_input import check_input
from utils.convert_validation_to_bool import convert_validation_to_bool

def app():
    # Defaults: Pattern, Message, Error Message
    default_pattern = "^(Y|n)$"
    default_error_message = "Error! Make sure you only use 'Y' for 'YES' and 'n' for 'No'"

    print("---Generate a random password---")

    # Validate length_of_password
    length_of_password = 0
    while True:
        try:
            length_of_password = abs(int(input("Enter the length of your password: ")))
        except ValueError:
            print("Please enter a postive integer")
            continue
        else:
            break

    # Validate other input parameters
    include_symbols = convert_validation_to_bool(check_input(default_pattern, "Do you want to include symbols? (e.g. @#$%!) [Y/n]: ", default_error_message))
    include_numbers = convert_validation_to_bool(check_input(default_pattern, "Do you want to include numbers? (e.g. 123456) [Y/n]: ", default_error_message))
    include_lowercase_characters = convert_validation_to_bool(check_input(default_pattern, "Do you want to include lowercase characters? (e.g. abcdefg) [Y/n]: ", default_error_message))
    include_uppercase_characters = convert_validation_to_bool(check_input(default_pattern, "Do you want to include uppercase characters? (e.g. ABCDEFG) [Y/n]: ", default_error_message))
    exclude_similar_characters = convert_validation_to_bool(check_input(default_pattern, "Do you want to exclude similar characters? (e.g. i, l, I, 1, L, o, O, 0) [Y/n]: ", default_error_message))

    print(generate_password(length_of_password, include_symbols, include_numbers, include_lowercase_characters, include_uppercase_characters, exclude_similar_characters))

app()
