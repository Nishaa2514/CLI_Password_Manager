from storage import (
    add_password,
    view_passwords,
    delete_password
)

from encryption import (
    encrypt_password,
    decrypt_password
)



def display_menu():

    while True:

        print("\n======================")
        print(" CLI PASSWORD MANAGER ")
        print("======================")

        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")


        choice = input("\nEnter your choice: ")


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

            website = input(
                "Enter website to delete: "
            )

            delete_password(website)



        elif choice == "4":

            print(
                "Exiting Password Manager..."
            )

            break



        else:

            print(
                "Invalid choice"
            )