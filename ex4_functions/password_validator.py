def is_digit(word: str):
    digit_counter = 0
    for character in word:
        if character.isdigit():
            digit_counter += 1
    return digit_counter


def password_validator(word: str):
    is_valid = []
    if 6 <= len(word) <= 10:
        is_valid.append(True)
    else:
        is_valid.append(False)

    if word.isalnum():
        is_valid.append(True)
    else:
        is_valid.append(False)

    if is_digit(inserted_password) >= 2:
        is_valid.append(True)
    else:
        is_valid.append(False)
    return is_valid


inserted_password = input()
checked_pass = password_validator(inserted_password)
if all(checked_pass):
    print("Password is valid")

if not checked_pass[0]:
    print("Password must be between 6 and 10 characters")

if not checked_pass[1]:
    print("Password must consist only of letters and digits")

if not checked_pass[2]:
    print("Password must have at least 2 digits")