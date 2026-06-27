from auth import *
from encryption import *
from storage import *

print("========== TESTING ==========")

print("\nTesting Encryption")

generate_key()

password = "hello123"

encrypted = encrypt_password(password)

decrypted = decrypt_password(encrypted)

if password == decrypted:
    print("Encryption Test Passed")
else:
    print("Encryption Test Failed")


print("\nTesting Storage")

add_password("Instagram", encrypted.decode())

view_passwords()

delete_password("Instagram")

print("Storage Test Completed")