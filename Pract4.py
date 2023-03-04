#To demonstrate transposition cypher 
#Write a program to implement columnar transposition cypher

#Enter the plaintext: The quick brown fox jumps over the lazy dog
#Enter the key: SECRET
#Ciphertext: HIUTCFKSROJNPTWQEZXBVGMDLAYE O  U  .


import math


def encrypt_transposition_columnar(plaintext, key):
  # Remove any spaces in the plaintext and convert to uppercase
  plaintext = plaintext.replace(' ', '').upper()

  # Calculate the number of columns in the table
  num_cols = len(key)

  # Calculate the number of rows in the table
  num_rows = math.ceil(len(plaintext) / num_cols)

  # Add padding to the plaintext if necessary
  num_padding = num_rows * num_cols - len(plaintext)
  plaintext += 'X' * num_padding

  # Create a table with the plaintext and the key
  table = [
    list(plaintext[i:i + num_cols]) for i in range(0, len(plaintext), num_cols)
  ]
  table[0] = [key[i] for i in range(num_cols)]

  # Sort the key and rearrange the columns accordingly
  sorted_key = sorted(key)
  sorted_table = [[0] * num_cols for _ in range(num_rows)]
  for col in range(num_cols):
    index = key.index(sorted_key[col])
    for row in range(num_rows):
      sorted_table[row][col] = table[row][index]

  # Flatten the sorted table to produce the ciphertext
  ciphertext = ''
  for row in sorted_table:
    ciphertext += ''.join(row)

  return ciphertext


# Get the plaintext and key from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encrypt the plaintext
ciphertext = encrypt_transposition_columnar(plaintext, key)
print("Ciphertext:", ciphertext)
