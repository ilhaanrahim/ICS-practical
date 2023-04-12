# P9 - md5 hash

# Python 3 code to demonstrate the
# working of MD5 (byte - byte)

import hashlib

# encoding GeeksforGeeks using md5 hash
# function
print("Enter plain-text to be hashed: ")
inp = input().encode("utf-8")
result = hashlib.md5(inp)

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
