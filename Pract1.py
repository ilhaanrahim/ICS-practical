def generate_key_matrix(key):
  key = key.replace(" ", "").upper()
  key_matrix = []
  for char in key:
    if char not in key_matrix:
      key_matrix.append(char)
  alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  for char in alphabet:
    if char not in key_matrix:
      key_matrix.append(char)
  return [key_matrix[i:i + 5] for i in range(0, 25, 5)]


def get_coords(key_matrix, char):
  for i in range(5):
    for j in range(5):
      if key_matrix[i][j] == char:
        return i, j
  return None


def encrypt_pair(key_matrix, pair):
  a, b = pair
  a_coords = get_coords(key_matrix, a)
  b_coords = get_coords(key_matrix, b)
  if a_coords[0] == b_coords[0]:
    return key_matrix[a_coords[0]][(a_coords[1] + 1) %
                                   5], key_matrix[b_coords[0]][(b_coords[1] +
                                                                1) % 5]
  elif a_coords[1] == b_coords[1]:
    return key_matrix[(a_coords[0] + 1) %
                      5][a_coords[1]], key_matrix[(b_coords[0] + 1) %
                                                  5][b_coords[1]]
  else:
    return key_matrix[a_coords[0]][b_coords[1]], key_matrix[b_coords[0]][
      a_coords[1]]


def encrypt_message(key, message):
  key_matrix = generate_key_matrix(key)
  message = message.replace(" ", "").upper()
  if len(message) % 2 == 1:
    message += "X"
  pairs = [message[i:i + 2] for i in range(0, len(message), 2)]
  encrypted_message = ""
  for pair in pairs:
    a, b = encrypt_pair(key_matrix, pair)
    encrypted_message += a + b
  return encrypted_message


key = input("Enter key: ")

plaintext = input("Enter plaintext: ")
key_matrix = generate_key_matrix(key)
for row in key_matrix:
  print(row)
print("Encrypted message:", encrypt_message(key, plaintext))
