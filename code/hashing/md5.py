# Muestra del algoritmo de hasheo MD5
# Se demostró que es inseguro desde 2005 y no se debería usar en desarrollos
# nuevos y reemplazarse de cualquier desarrollo que esté en mantenimiento.

# Encontrar una colisión de MD5 toma segundos, por lo que es demasiado riesgoso utilizarlo
# como mecanismo de seguridad o de revisión de datos

import hashlib

m1 = b''  # Las funciones de hasheo sólo soportan cadenas binarias
m2 = b'a'
m3 = b'b'
print(m1, hashlib.md5(m1).hexdigest())
print(m2, hashlib.md5(m2).hexdigest())
print(m3, hashlib.md5(m3).hexdigest())

h = hashlib.md5(m1).hexdigest()
