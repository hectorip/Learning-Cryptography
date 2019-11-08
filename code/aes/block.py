from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  # didn't even know this library existed
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as h

from os import urandom

print(h(urandom(5)))

