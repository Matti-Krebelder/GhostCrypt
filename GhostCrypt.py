from cryptography.fernet import Fernet
import os
import secrets

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(key, filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(filename + '.encrypted', 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename[:-10], 'wb') as f:
        f.write(decrypted_data)

def main():
    choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n")
    if choice == '1':
        key = generate_key()
        save_key(key, 'secret.key')
        file_to_encrypt = input("Enter the filename to encrypt: ")
        if os.path.exists(file_to_encrypt):
            if not os.path.exists(file_to_encrypt + '.encrypted'):
                encrypt_file(key, file_to_encrypt)
                print("File encrypted successfully.")
            else:
                print("Encrypted file already exists. Choose a different file.")
        else:
            print("File does not exist.")
    elif choice == '2':
        key_file = input("Enter the path to the key file: ")
        if os.path.exists(key_file):
            key = load_key(key_file)
            file_to_decrypt = input("Enter the filename to decrypt: ")
            if os.path.exists(file_to_decrypt) and file_to_decrypt.endswith('.encrypted'):
                decrypt_file(key, file_to_decrypt)
                print("File decrypted successfully.")
            else:
                print("Invalid file or file is not encrypted.")
        else:
            print("Key file does not exist.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
