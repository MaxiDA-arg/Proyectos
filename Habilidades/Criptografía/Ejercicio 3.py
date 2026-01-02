import  jks
import os
from Crypto.Cipher import ChaCha20
from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode

# #Obtenemos el path
path = os.path.dirname(r"C:\Users\Usuario\Desktop\Formaciones\Ciberseguridad\Criptografia\KeyStorePracticas")
keystore = path + "\KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-chacha20-256":
        key = sk.key

print("La clave es: ",key.hex())

# Ciframos en Chacha20
msj_claro = bytes('KeepCoding te enseña a codificar y a cifrar', 'utf-8')
clave = bytes.fromhex('af9df30474898787a45605ccb9b936d33b780d03cabc81719d52383480dc3120')
nonce = b64decode('9Yccn/f5nJJhAt2S')

cipher = ChaCha20.new(key=clave, nonce=nonce)
msj_cifrado = cipher.encrypt(msj_claro)

print('Mensaje cifrado en Hex: ', msj_cifrado.hex())
print('Mensaje cifrado en base64: ', b64encode(msj_cifrado).decode('utf-8'))

# Propuesta de cifrado en Chacha20poly1035
msj_claro = bytes('KeepCoding te enseña a codificar y a cifrar', 'utf-8')
clave = bytes.fromhex('af9df30474898787a45605ccb9b936d33b780d03cabc81719d52383480dc3120')
nonce = b64decode('9Yccn/f5nJJhAt2S')
datos_asociados = bytes('Validamos con este texto', 'utf-8')

# Cifrado
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce)
cipher.update(datos_asociados)
msj_cifrado_poly, tag = cipher.encrypt_and_digest(msj_claro)

print('Mensaje cifrado en Chacha20poly1035 en Hex: ', msj_cifrado_poly.hex())
print('Mensaje cifrado en Chacha20poly1035 en base64: ', b64encode(msj_cifrado_poly).decode('utf-8'))
print('tag base64: ', b64encode(tag).decode('utf-8'))

# Descifrando / validamos cifrado correcto
decipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce)
decipher.update(datos_asociados)
msj_descifrado_poly = decipher.decrypt_and_verify(msj_cifrado_poly, tag)

print('Mensaje descifado en Chacha20poly1035: ', msj_descifrado_poly.decode('utf-8'))
