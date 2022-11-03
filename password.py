import random

print('Hi! Welcome to Password Generator')

#The characters are the possible characters that would appear in the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*+'

number_of_passwords = input('Amount of passwords to generate: ')
number_of_passwords = int(number_of_passwords)

length_of_passwords = input('Input your password length: ')
length_of_passwords = int(length_of_passwords)

print('\nYour Passwords Are: ')

for password in range(number_of_passwords):
  passwords = ' '
  for c in range(length_of_passwords):
    passwords += random.choice(characters)
  print(passwords)

# Some changes