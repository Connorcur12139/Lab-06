##Program to add two numbers

#Menu

first = int(input('Please enter first number: '))
second = int(input('Please enter second number: '))

print('1. Addition')
print('2. Subtraction')
choice = int(input())


if choice == 1:
    print(first + second)
if choice == 2:
    print(first - second)

