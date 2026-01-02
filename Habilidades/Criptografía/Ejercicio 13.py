from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import os
import ed25519


# Importamos la clave privada para firmar
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/clave-rsa-oaep-priv.pem"
keypriv = RSA.importKey(open(path_file_priv).read())

mensaje_bytes = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.","utf-8")
hash = SHA256.new(mensaje_bytes)

signer=PKCS115_SigScheme(keypriv)
firma = signer.sign(hash)
print('------------------------------')

#Importamos la clave publica para validar la firma
fichero_pub = my_path + "/clave-rsa-oaep-publ.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())

firma= bytes.fromhex("a4606c518e0e2b443255e3626f3f23b77b9d5e1e4d6b3dcf90f7e118d6063950a23885c6dece92aa3d6eff2a72886b2552be969e11a4b7441bdeadc596c1b94e67a8f941ea998ef08b2cb3a925c959bcaae2ca9e6e60f95b989c709b9a0b90a0c69d9eaccd863bc924e70450ebbbb87369d721a9ec798fe66308e045417d0a56b86d84b305c555a0e766190d1ad0934a1befbbe031853277569f8383846d971d0daf05d023545d274f1bdd4b00e8954ba39dacc4a0875208f36d3c9207af096ea0f0d3baa752b48545a5d79cce0c2ebb6ff601d92978a33c1a8a707c1ae1470a09663acb6b9519391b61891bf5e06699aa0a0dbae21f0aaaa6f9b9d59f41928d")

verifier=PKCS115_SigScheme(keypub)

try:
    verifier.verify(hash,firma)
    print("Firma válida")
except:
    print("La firma no es válida")

# Calculamos la firma con la curva elíptica ed25519
import ed25519

publickey = open("ed25519-publ","rb").read()
privatekey = open("ed25519-priv","rb").read()

signedKey = ed25519.SigningKey(privatekey)
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
signature = signedKey.sign(msg, encoding='hex')
print("Firma en Hex:", signature)

try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, msg, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")