from cryptography.fernet import Fernet
import os


def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()

        with open("key.key", "wb") as file:
            file.write(key)


def load_key():
    generate_key()

    with open("key.key", "rb") as file:
        return file.read()


def encrypt_password(password):
    key = load_key()

    fernet = Fernet(key)

    encrypted = fernet.encrypt(password.encode())

    return encrypted


def decrypt_password(encrypted_password):
    key = load_key()

    fernet = Fernet(key)

    decrypted = fernet.decrypt(
        encrypted_password.encode()
    )

    return decrypted.decode()