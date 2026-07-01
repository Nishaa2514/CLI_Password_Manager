from auth import authenticate_user
from menu import display_menu

def main():
    print("Welcome to CLI Password Manager")

    password = input("Enter Master Password: ")

    if authenticate_user(password):
        print("Authentication Successful\n")
        display_menu()
    else:
        print("Access Denied")

if __name__ == "__main__":
    main()