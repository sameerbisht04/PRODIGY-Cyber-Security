import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[!@#$%^&*()-+]", password) is None

    errors = {
        "Length Error": length_error,
        "Digit Error": digit_error,
        "Uppercase Error": uppercase_error,
        "Lowercase Error": lowercase_error,
        "Special Character Error": special_char_error
