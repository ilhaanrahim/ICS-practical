import math


def generate_key_pair(p, q):
  n = p * q
  phi_n = (p - 1) * (q - 1)
  e = 2

  while math.gcd(e, phi_n) != 1:
    e += 1

  d = pow(e, -1, phi_n)

  return ((e, n), (d, n))


def encrypt(plaintext, public_key):
  e, n = public_key
  ciphertext = [pow(ord(char), e, n) for char in plaintext]
  return ciphertext


if __name__ == '__main__':
  p = int(input("Enter a prime number (p): "))
  q = int(input("Enter another prime number (q): "))
  plaintext = input("Enter the plaintext to be encrypted: ")

  public_key, _ = generate_key_pair(p, q)
  ciphertext = encrypt(plaintext, public_key)

  print("Public Key: ", public_key)
  print("Plaintext: ", plaintext)
  print("Encrypted Text: ", ciphertext)
