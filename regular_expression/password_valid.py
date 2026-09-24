import re

pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$")
string = input("enter the string")

a = pattern.search(string)
print(a)





def is_valid_password(password):
    # Define the regular expression for password validation
    # At least 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    regex = re.compile(pattern)

    if regex.match(password):
        return True
    else:
        return False

password = "Sujay"
if is_valid_password(password):
    print("Password is valid!")
else:
    print("Password is invalid,follow the password requirements.")
