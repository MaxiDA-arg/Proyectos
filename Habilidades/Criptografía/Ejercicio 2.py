import  jks
import os

#Obtenemos el path
path = os.path.dirname(r"C:\Users\Usuario\Desktop\Formaciones\Ciberseguridad\Criptografia\KeyStorePracticas")
keystore = path + "\\KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        key = sk.key

print("La clave es: ",key.hex())

#Desciframos AES/CBC/PKCS7
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

msg_codificado = b64decode('TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=')
clave = bytes.fromhex('a2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72')
iv = bytes.fromhex('00000000000000000000000000000000')

cipher = AES.new(clave, AES.MODE_CBC, iv)
msg_dec_bytes = cipher.decrypt(msg_codificado)
msg_dec_claro = unpad(msg_dec_bytes, AES.block_size, style= 'pkcs7')
msd_dec_padx923 = unpad(msg_dec_bytes, AES.block_size, style= 'x923')

# Contamos padding
padding = len(msg_dec_bytes) - len(msg_dec_claro)


print("Mensaje claro con padding: ",msg_dec_bytes.decode('utf-8'))
print("Mensaje claro sin padding: ",msg_dec_claro.decode('utf-8'))

# Pintamos el mensaje cifrado en Hex para identificar el último par de digitos y conocer la cantidad de padding
print("Mensaje cifrado HEX con padding: ",msg_dec_bytes.hex())
# Simplemente validamos la observación anterior
print("La cantidad de padding agregado en el mensaje es: ", padding)

#Pintamos el mensaje descifrado con padding x923
print("Mensaje claro padding x923: ",msd_dec_padx923.decode('utf-8'))