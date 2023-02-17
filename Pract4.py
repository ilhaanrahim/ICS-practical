#To demonstrate transposition cypher 
#Write a program to implement columnar transposition cypher
import math

def encrypt(plaintext, key):
  # Check if key is valid
  if not set(key) == set(str(i) for i in range(1, len(key) + 1)):
    print("Error: Invalid key.")
    return ""
  ciphertext = ""
  # Remove spaces from plaintext
  plaintext = plaintext.replace(" ", "")
  # Calculate number of rows needed for the grid
  rows = math.ceil(len(plaintext) / len(key))
  # Fill grid with plaintext
  grid = [[""] * len(key) for _ in range(rows)]
  i = 0
  for row in range(rows):
    for col in range(len(key)):
      if i < len(plaintext):
        grid[row][col] = plaintext[i]
        i += 1
  # Create ciphertext by reading columns in order of the key
  for col in range(len(key)):
    index = key.index(str(col + 1))
    for row in range(rows):
      ciphertext += grid[row][index]
  return ciphertext

plaintext = input("Enter plaintext: ")
key = input("Enter key: ")
ciphertext = encrypt(plaintext, key)
print("Ciphertext: " + ciphertext)
