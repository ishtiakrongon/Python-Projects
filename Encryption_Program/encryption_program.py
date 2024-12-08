import random
import string

# Generate character set and key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars[:]
random.shuffle(key)


def encrypt(plain_text: str) -> str:
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index_msg = chars.index(letter)
            cipher_text += key[index_msg]
        else:
            # Handle unsupported characters
            cipher_text += letter
    return cipher_text


def decrypt(cipher_text: str) -> str:
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index_msg = key.index(letter)
            plain_text += chars[index_msg]
        else:
            # Handle unsupported characters
            plain_text += letter
    return plain_text


def main():
    plain_text = input("Enter a message to encrypt: ")
    encrypted_message = encrypt(plain_text)
    print(f"Original Message: {plain_text}")
    print(f"Encrypted Message: {encrypted_message}")

    # Optional: Prompt for decryption
    decrypt_option = input("\nDo you want to decrypt a message? (yes/no): ").strip().lower()
    if decrypt_option == "yes":
        encrypted_input = input("Enter the message to decrypt: ")
        decrypted_message = decrypt(encrypted_input)
        print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
