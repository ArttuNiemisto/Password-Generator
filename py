import random

print('Tervetuloa salasana generaattoriin')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('Salasanojen lukumäärä: ')
number =int(number)

lenght = input('Anna sinun salasanasi pituus: ')
lenght = int(lenght)

print('\nTässä sinun salasanasi:')

for sal in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
