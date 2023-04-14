# P9 - md5 hash

# Python 3 code to demonstrate the
# working of MD5 (byte - byte)

import hashlib

def md5_16byte(message):
    # Create an instance of the MD5 hash object
    md5 = hashlib.md5()

    # Update the hash object with the message
    md5.update(message.encode())

    # Get the hash in hexadecimal format
    hash_hex = md5.hexdigest()

    # Convert the hexadecimal hash to bytes
    hash_bytes = bytes.fromhex(hash_hex)

    # Take the first 16 bytes of the hash
    hash_16byte = hash_bytes[:16]

    # Return the 16-byte hash
    return hash_16byte

# Take user input for the message
message = input("Enter the message to be hashed: ")

# Compute the MD-5 hash in 16-byte format
hash_16byte = md5_16byte(message)

# Print the hash in bytes format
print("MD-5 hash (16-byte):", hash_16byte)

