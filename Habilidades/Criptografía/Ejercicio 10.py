import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Creamos los aleatorios para cifrar los datos sensibles
clave = get_random_bytes(16)
nonce = get_random_bytes(16)
datos_asociados = bytes('','utf-8')
datos_confidenciales = b'{"idUsuario":1,"tarjeta":4231212345676891}'

cipher = AES.new(key=clave, mode=AES.MODE_GCM, nonce=nonce)
cipher.update(datos_asociados)

texto_cifrado, tag = cipher.encrypt_and_digest(datos_confidenciales)

texto_cifrado_b64 = b64encode(texto_cifrado).decode('utf-8')
nonce_b64 = b64encode(nonce).decode('utf-8')
tag_b64 = b64encode(tag).decode('utf-8')
datos_asociados_b64 = b64encode(datos_asociados).decode('utf-8')

texto_cifrado_json = json.dumps({'texto cifrado':texto_cifrado_b64,'nonce':nonce_b64,'tag':tag_b64,'datos asociados':datos_asociados_b64})
print(texto_cifrado_json)

# Validamos descifrando el mensaje
decipher = AES.new(key=clave, mode=AES.MODE_GCM, nonce=nonce)
decipher.update(datos_asociados)
texto_descifrado = decipher.decrypt_and_verify(texto_cifrado,tag)

print('=====Validación=====')
print('Validamos descifrando:',texto_descifrado)

# Generamos la firma RSA para el mensaje confidencial
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

# Par de claves
keyPair = RSA.generate(2048) 

# Publica
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
# print(pubKeyPEM.decode('utf8'))
# print("--------------------------------------------------")

# Privada
privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('utf8'))
# print("--------------------------------------------------")

mensaje = bytes(texto_cifrado_json,'utf-8')
cipher_RSA = PKCS1_OAEP.new(pubKey,SHA256)
text_cifrado = cipher_RSA.encrypt(mensaje)

print("Cifrado RSA:", text_cifrado.hex())
print("--------------------------------------------------")

# Validamos descifrando el mensaje
decryptor = PKCS1_OAEP.new(keyPair,SHA256)
descifrado_RSA= decryptor.decrypt(text_cifrado)
print("Descifrado RSA: ", descifrado_RSA)