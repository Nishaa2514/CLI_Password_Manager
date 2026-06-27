
from encryption import *


password = "12345"

encrypted = encrypt_password(password)

print("Original:", password)

print("Encrypted:", encrypted)


decrypted = decrypt_password(encrypted)

print("Decrypted:", decrypted)


if password == decrypted:
    print("Encryption Test Passed")
else:
    print("Test Failed")

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
print("\nTesting encryption with another password")

password2 = "newpassword123"

encrypted2 = encrypt_password(password2)

decrypted2 = decrypt_password(encrypted2)

print("Original:", password2)
print("Decrypted:", decrypted2)

if password2 == decrypted2:
    print("Second Encryption Test Passed")
else:
    print("Second Test Failed")
 b410f88ddbd5cc4326be46ae99ecf77e066b5855
