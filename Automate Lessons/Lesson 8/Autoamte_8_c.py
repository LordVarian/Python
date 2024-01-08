print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print('     '.isspace())
print('hello world'.isspace())
print('hello world'[5].isspace())
print('This Is Title Case'.istitle())
print('hello world'.title())

print('Hello World'.startswith('Hello'))
print('Hello World'.startswith('H'))
print('Hello World'.startswith('ello'))
print('Hello World'.endswith('World'))

print(','.join(["cat", "dog", "mouse"]))
print(''.join(["cat", "dog", "mouse"]))
print('\n\n'.join(["cat", "dog", "mouse"]))

print('My name is Simon'.split())
print('My name is Simon'.split('m'))

rjust = 'Hello'.rjust(10)
print(rjust)
print(len(rjust))
ljust = 'Hello'.ljust(20)
print(ljust)
print(len(ljust))
ljuststar = 'Hello'.ljust(20,'*')
print(ljuststar)
center = 'Hello'.center(20,'=')
print(center)
strip = ljust.strip()
print(strip)
print('     x     '.lstrip())
print('     x     '.rstrip())
print('SpamSpamBaconSpamEggsSpamSpam'.strip('Spam'))

lam = 'Hello there'
print(lam.replace('o', 'xyz'))

import pyperclip
pyperclip.copy('Hello!!!!!!!!!')
print(pyperclip.paste())