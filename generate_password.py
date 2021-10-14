import secrets
import string

def generate_password(length_of_password, include_symbols, include_numbers, include_lowercase_characters, include_uppercase_characters, exclude_similar_characters):
    all_used_characters = ""

    if include_symbols:
        all_used_characters += string.punctuation
    if include_numbers:
        all_used_characters += string.digits
    if include_lowercase_characters:
        all_used_characters += string.ascii_lowercase
    if include_uppercase_characters:
        all_used_characters += string.ascii_uppercase
    if exclude_similar_characters is False:
        similar_characters = "iIlLoO0"
        for characters in similar_characters:
            all_used_characters = all_used_characters.replace(characters, "")

    # Generate password string
    return "".join(secrets.choice(all_used_characters) for _ in range(length_of_password))
    