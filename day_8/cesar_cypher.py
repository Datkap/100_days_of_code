from day_8.cesar_cypher_extras import alphabet


def encrypt(text: str, shift: int):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            current_position = alphabet.index(char)
            new_position = (current_position + shift) % len(alphabet)
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text: str, shift: int):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            current_position = alphabet.index(char)
            new_position = (current_position - shift) % len(alphabet)
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += char

    return decrypted_text

def ask_for_shift():
    shift = input("What shift should be used to encode your message?")
    while not shift.isnumeric():
        print("Shift must be a whole number.")
        shift = input("What shift should be used to encode your message?")
    return int(shift)


def cesar_cypher():
    action = input("Would you like to 'encode' or decode' your message?")
    if action == 'encode':
        message = input("What message would you like to encode?").lower()
        shift = ask_for_shift()
        print(f"Encrypted version of your message: {encrypt(message, shift)}")
    elif action == 'decode':
        message = input("What message would you like to decode?").lower()
        shift = ask_for_shift()
        print(f"Decrypted version of your message: {decrypt(message, shift)}")
    else:
        print("Type in 'encode' or 'decode', then your message and shift.")
        cesar_cypher()
