from generate_password import generate_password
from utils.check_input import check_input

def app():
    # Defaults: Pattern, Message, Error Message
    default_pattern = "^(Y|n)$"
    default_message = "Do you want to include symbols? (e.g. @#$%!) [Y/n]: "
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

    include_symbols = check_input(default_pattern, default_message, default_error_message)
    include_numbers = check_input(default_pattern, default_message, default_error_message)
    include_lowercase_characters = check_input(default_pattern, default_message, default_error_message)
    include_uppercase_characters = check_input(default_pattern, default_message, default_error_message)
    exclude_similar_characters = check_input(default_pattern, default_message, default_error_message)

    generate_password(length_of_password, include_symbols, include_numbers, include_lowercase_characters, include_uppercase_characters, exclude_similar_characters)

app()
