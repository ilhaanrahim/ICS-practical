# Practical 8

a = int(input('Enter the value of coefficient a: '))
b = int(input('Enter the value of coefficient b: '))
x = int(input('Enter the x coordinate of the point '))
y = int(input('Enter the y coordinate of the point '))

value = y**2 - (x**3 + a + x + b)

print(f'The value of the elliptic curve equation at point ({x}, {y}) is : {value}')
