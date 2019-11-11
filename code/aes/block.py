"""
Demuestra el funcionamiento cifrado de un bloque de AES en modo Electronic Codebook

"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  # didn't even know this library existed
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as h

from os import urandom

# Generting a random key
key = urandom(16)
print("Key: {}".format(h(key).decode('utf-8')))
print("%s" % key)

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

encryptor = cipher.encryptor()

p = b'\x00'*16

c = encryptor.update(p) + encryptor.finalize()

print("%s=%s" % (h(p), h(c)))

decryptor = cipher.decryptor()
p = decryptor.update(c) + decryptor.finalize()
print("%s=%s"% (h(c), h(p)))

