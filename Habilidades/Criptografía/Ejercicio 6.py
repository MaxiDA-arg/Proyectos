from Crypto.Hash import HMAC, SHA256
import os
import jks

# Importamos la clave desde Key Storeimport  jks
path = os.path.dirname(r"C:\Users\Usuario\Desktop\Formaciones\Ciberseguridad\Criptografia\KeyStorePracticas")
keystore = path + "\\KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "hmac-sha256":
        key = sk.key

print("La clave es: ",key.hex())

# Generamos el HMAC con los siguientes datos
def getHMAC(key_bytes,data_bytes):
    hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
    return hmac256.hexdigest()

def validateHMAC(key_bytes,data_bytes,hmac):
    hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
    result = "KO"
    try:
        hmac256.hexverify(hmac)
        result = "OK"
    except ValueError:
        result = "KO"
    print("result: " + result)
    return result

clave = bytes.fromhex('a212a51c997e14b4df08d55967641b0677ca31e049e672a4b06861aa4d5826eb')
msj_cod_bytes = bytes('Siempre existe más de una forma de hacerlo, y más de una solución válida.', 'utf-8')

hmac256 = getHMAC(clave, msj_cod_bytes)

print(hmac256)
print(validateHMAC(clave, msj_cod_bytes,hmac256))