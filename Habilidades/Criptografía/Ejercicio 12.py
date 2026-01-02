from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Datos conocidos para cifrar
msj_claro = bytes('He descubierto el error y no volveré a hacerlo mal', 'utf-8')
clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = b64decode('9Yccn/f5nJJhAt2S')
datos_asociados = bytes('','utf-8')

cipher = AES.new(key=clave, mode=AES.MODE_GCM, nonce=nonce)
cipher.update(datos_asociados)
msj_cifrado, tag = cipher.encrypt_and_digest(msj_claro)

print('Texto cifrado en Hex:', msj_cifrado.hex())
print('Texto cifrado en base64:', b64encode(msj_cifrado).decode('utf-8'))
print('Tag:', tag.hex())

# Validamos descifrando la información

cifrado_en_hex = bytes.fromhex('5dcbb6261d0fba29ce39431e9a013b34cbca2a4e04bb2d90149d61f4afd04d65e2abdd9d84bba6eb8307095f5078fbfc16256d')

decipher = AES.new(key=clave, mode=AES.MODE_GCM, nonce=nonce)
decipher.update(datos_asociados)
msj_claro_descifrado = decipher.decrypt_and_verify(cifrado_en_hex,tag)

print('Mensaje validado:', msj_claro_descifrado.decode('utf-8'))