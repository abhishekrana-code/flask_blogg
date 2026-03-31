import secrets

def my_random():
    return secrets.token_hex(16)

print(my_random())