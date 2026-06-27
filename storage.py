import json


FILE_NAME = "passwords.json"



def load_passwords():

    try:

        with open(FILE_NAME, "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return {}




def save_passwords(data):

    with open(FILE_NAME, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )




def add_password(site, password):

    passwords = load_passwords()

    passwords[site] = password

    save_passwords(passwords)

    print("Password saved successfully")




def view_passwords():

    passwords = load_passwords()


    if len(passwords) == 0:

        print("No passwords stored")

    else:

        for site, password in passwords.items():

            print(
                "Website:",
                site
            )

            print(
                "Password:",
                password
            )




def delete_password(site):

    passwords = load_passwords()


    if site in passwords:

        del passwords[site]

        save_passwords(passwords)

        print("Password deleted successfully")


    else:

        print("Website not found")