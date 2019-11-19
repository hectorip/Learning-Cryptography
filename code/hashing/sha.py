# SHA significa Secure Hashing Algorithm

from hashlib import sha1
import secrets


p = b'a'
c = sha1(p + secrets.token_bytes(10))
c2 = sha1(p + secrets.token_bytes(10))
print(c.hexdigest())
print(c2.hexdigest())