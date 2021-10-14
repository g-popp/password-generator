from generate_password import generate_password

def app():
    print("---Generate a random password---")
    length_of_password = input("Enter the length of your password: ")
    include_symbols = input("Do you want to include symbols? (e.g. @#$%!) [Y/n]: ")
    include_numbers = input("Do you want to include numbers? (e.g. 123456) [Y/n]: ")
    include_lowercase_characters = input("Do you want to include lowercase characters? (e.g. abcdefg) [Y/n]: ")
    include_uppercase_characters = input("Do you want to include uppercase characters? (e.g. ABCDEFG) [Y/n]: ")
    exclude_similar_characters = input("Do you want to exclude similar characters? (e.g. i, l, I, 1, L, o, O, 0) [Y/n]: ")

    generate_password(length_of_password, include_symbols, include_numbers, include_lowercase_characters, include_uppercase_characters, exclude_similar_characters)

app()
