#To demostrate transpositon cipher:
#Write a program to implement rail fence cypher (row tranposition cypher)

def main():

  plain_text = input("Enter the plain text: ")
  layers = int(input("Enter the number of key: "))
  cipher_text = encrypt(layers, plain_text)
  print("Encrypted text: " + cipher_text)


def encrypt(layers, plain_text):

  plain_text = plain_text.replace(" ", "")
  plain_text = plain_text.upper()
  rail = [""] * layers
  layer = 0
  for character in plain_text:

    rail[layer] += character
    if layer >= layers - 1:

      layer = 0

    else:

      layer += 1
  cipher = "".join(rail)
  return cipher


if __name__ == '__main__':
  main()
