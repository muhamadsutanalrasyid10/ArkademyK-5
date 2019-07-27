import re

def is_username_valid(username):
    usernameregex = re.compile(
        r'^[^0-9!@#\$%\^\&\*\)\(\+\=\.\_\-][0-9a-zA-Z!@#\$%\^\&\*\)\(\+\=\.\_\-]{5,9}$')
    match = usernameregex.search(username)
    if match:
        return True
    else:
        return False

def is_password_valid(password):
    passwordregex = re.compile(
        r'^(?=.*[=]+.*)(?=.*[0-9]+.*)(?=.*[A-Z]+.*)(?=.*[!@#\$%\^\&\*\)\(\+\=\.\_\-]+.*)[0-9a-zA-Z!@#\$%\^\&*\)\(\+\=\.\_\-]{8,}$')
    match = passwordregex.search(password)
    if match:
        return True
    else:
        return False

def main():

    print(is_username_valid('Xrutaf888'))
    print(is_username_valid('1Diana'))
    print(is_password_valid('passW0rd='))
    print(is_password_valid('C0d3YourFuture!#'))

if __name__ == '__main__':
    main()