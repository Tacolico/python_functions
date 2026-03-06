import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + "@#$%@$!%*?&"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
print("Generated Password:", generate_password())
