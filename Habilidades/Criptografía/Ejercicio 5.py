import hashlib

# Identificamos el tipo de algoritmo
m_256 = hashlib.sha3_256()
m_256.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("sha3_256: " + m_256.digest().hex())

m_512 = hashlib.sha512()
m_512.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("sha256_512: " + m_512.digest().hex())

# Ciframos los texto con el mismo algoritmo sumando "solo" en el texto 2
m1 = hashlib.sha3_256()
m1.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("Texto cifrado 1: " + m1.digest().hex())

m2 = hashlib.sha3_256()
m2.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.", "utf8"))
print("Texto cifrado 1: " + m2.digest().hex()) 