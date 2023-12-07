def length(current_user):
    if 3 <= len(current_user) <= 16:
        return True
    return False


def is_containing_true_symbols(current_user):
    for character in current_user:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant(current_user):
    for letter in current_user:
        if letter == " ":
            return False
    return True


def username_is_valid(current_user):
    if length(current_user) and is_containing_true_symbols(current_user) and no_redundant(current_user):
        return True
    return False


usernames = input().split(", ")
for current_username in usernames:
    if username_is_valid(current_username):
        print(current_username)