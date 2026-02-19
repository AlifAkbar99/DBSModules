# upper() 
kata = 'dicoding'
kata = kata.upper()
print(kata)

print()
# lower()
kata = 'DICODING'
kata = kata.lower()
print(kata)

print()
# rstrip()
print('Dicoding     '.rstrip())

print()
# lstrip()
print('     Dicoding'.lstrip())

print()
# strip()
print('     Dicoding      '.strip())
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code'))

print()
# startswith
print('Dicoding Indonesia'.startswith("Dicoding"))

print()
#endswith
print('Dicoding Indonesia'.endswith("Dicoding"))

print()
# join()
print(" ".join(['Dicoding', 'Indonesia', '!']))
print("123".join(['Dicoding', 'Indonesia']))

print()
# split()
print('Dicoding Indonesia !'.split())
print('''Halo, aku ikan, 
      aku suka sekali menyelam
      aku tinggal di laut'''.split('\n'))

print()
# replace()
string = 'ayo belajar coding di dicoding'
print(string.replace('coding', 'pemrograman'))

print()
# isupper()
kata = 'DICODING'
print(kata.isupper())

print()
# islower()
kata = 'dicoding'
print(kata.islower())

print()
# isalpha()
kata = 'dicoding'
print(kata.isalpha())

print()
# isalnum()
kata = 'dicoding123'
print(kata.isalnum())

print()
# isdecimal()
print('123'.isdecimal())

print()
# isspace()
print('     '.isspace())

print()
# istile()
print('Dicoding Indonesia'.istitle())