def encrypt_message(message):
    ascii_codes = [bin(ord(char))[2:].zfill(8) for char in message]
    print("8-bit ASCII codes:", ascii_codes)
    
    encrypted_message = ""
    for ascii_code in ascii_codes:
        first_four_bits = ascii_code[:4]
        last_four_bits = ascii_code[-4:]
        swapped = last_four_bits + first_four_bits
        encrypted_message += hex(int(swapped, 2))[2:]
        print("Encrypted character:", encrypted_message[-2:])
    return encrypted_message

message = input("Enter message to encrypt: ")
print("Encrypted message:", encrypt_message(message))
