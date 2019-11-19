# El concurso para ganar el título de Secure Hashing Algorithm 3
# fue ganado por un algoritmo llamado Keccak

from hashlib import sha3_512, sha512

p = b'hello_crypto'

c_1 = sha512(p).hexdigest()
c_3 = sha3_512(p).hexdigest()

print('SHA512: {}'.format(c_1))
print('SHA3 512 (Keccak): {}'.format(c_3))\

