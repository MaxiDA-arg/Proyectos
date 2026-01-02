# Generamos el XOR de datos HEX
def xor_hex(hex1, hex2):
 
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)

    # Realizar la operación XOR entre los bytes
    xor_result = bytes(a ^ b for a, b in zip(bytes1, bytes2))

    # Convertir el resultado XOR a HEX
    return xor_result.hex()

# Claves consigna 1
clave_desarrollo = ("B1EF2ACFE2BAEEFF")
clave_final_c1 = ("91BA13BA21AABB12")
# Calcular el valor XOR
clave_properties_c1 = xor_hex(clave_desarrollo, clave_final_c1)
# Consigna 1
print("Clave asignada por Key Manager: ", clave_properties_c1)

# Claves consigna 
clave_desarrollo = ("B1EF2ACFE2BAEEFF")
clave_properties_c2 = ("B98A15BA31AEBB3F")
# Calcular el valor XOR
clave_final_c2 = xor_hex(clave_desarrollo, clave_properties_c2)
# Consigna 2
print("Clave en Memoria: ", clave_final_c2)