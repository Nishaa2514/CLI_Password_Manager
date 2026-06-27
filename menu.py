[10:20 pm, 27/06/2026] Sharan: from auth import *
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
[10:31 pm, 27/06/2026] Sharan: from menu import display_menu

if _name_ == "_main_":
    display_menu()
[10:35 pm, 27/06/2026] Sharan: from storage import (
    add_password,
    view_passwords,
    delete_password
)

from encryption import (
    encrypt_password
)


def display_menu():

    while True:

        print("\n===================")
        print("CLI PASSWORD MANAGER")
        print("===================")

        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice: ")


        if choice == "1":

            website = input("Enter website: ")
            password = input("Enter password: ")

            encrypted = encrypt_password(password)

            add_password(
                website,
                encrypted.decode()
            )


        elif choice == "2":

            view_passwords()


        elif choice == "3":

            website = input("Enter website: ")

            delete_password(website)


        elif choice == "4":

            print("Exiting...")
            break


        else:

            print("Invalid choice")