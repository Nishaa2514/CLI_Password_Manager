import hashlib
MASTER_PASSWORD = "admin123"

def authenticate_user(password):
    return password == MASTER_PASSWORD


def create_master_password():

    password = input("Create Master Password: ")

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()


    with open("master.txt", "w") as file:
        file.write(hashed_password)


    print("Master password created successfully")



def verify_password():

    password = input("Enter Master Password: ")


    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()


    try:

        with open("master.txt", "r") as file:
            stored_password = file.read()


        if hashed_password == stored_password:

            return True

        else:

            return False


    except FileNotFoundError:

        return False