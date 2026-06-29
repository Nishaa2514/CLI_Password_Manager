from cryptography.fernet import Fernet


KEY_FILE = "key.key"


def generate_key():

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)



def load_key():

    with open(KEY_FILE, "rb") as file:
        return file.read()



def encrypt_password(password):

    key = load_key()

    cipher = Fernet(key)

    encrypted_password = cipher.encrypt(
        password.encode()
    )

    return encrypted_password



def decrypt_password(encrypted_password):

    key = load_key()

    cipher = Fernet(key)

    decrypted_password = cipher.decrypt(
        encrypted_password
    )

    return decrypted_password.decode()