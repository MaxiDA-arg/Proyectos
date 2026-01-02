import jwt

# Reemplazamos los valores para revisar el comportamiento de pyjwt
encoded_jwt = jwt.encode({"usuario": "Don Pepito de los palotes", "rol": "isAdmin", "iat": 1667933533}, "", algorithm="HS256")
print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"Con KeepCoding aprendemos", algorithms="HS256")
print(decode_jwt)