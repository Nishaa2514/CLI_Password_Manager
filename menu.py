from storage import add_password, view_passwords, delete_password


def display_menu():
    while True:
        print("\nCLI PASSWORD MANAGER")
        print("====================")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            site = input("Enter site: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            add_password(site, username, password)

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            site = input("Enter site to delete: ")
            delete_password(site)

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice!")