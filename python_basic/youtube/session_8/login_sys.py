import random, json

def log():
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        return False

    # Check Username & Password
    x = input("Enter username: ")
    if x in users_data and input("Enter password: ") == users_data[x]:
        # Generate 2FA Code
        s = random.randrange(1000, 10000)
        print(f"Verification code: {s}")
        if int(input("Enter code: ")) == s:
            return True
    return False
