# p10 - extended euclidean
def extended_ea(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    gcd, x, y = extended_ea(b % a, a)
    return (gcd, y - (b // a) * x, x)


a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

gcd, x, y = extended_ea(a, b)

print(f"The GCD of {a} and {b} is {gcd}.")
print(f"Coefficients x and y are: {x} and {y}")

