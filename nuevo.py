from hashlib import sha512
from werkzeug.security import generate_password_hash, check_password_hash

variable = sha512(b"Hola")#la b es para pasarlo a binario :)

#print(f'variable {variable.digest()}')#retorna una cadena cifrada en binario
#print(f'variable {variable.hexdigest()}')#retorna una cadena en hexadecimal

#alteracion 

variableSegundoIntento = sha512(b"Holo")#la b es para pasarlo a binario :)
#print(f'Variable 2: {variableSegundoIntento.digest()}')
#print(f'Variable 2: {variableSegundoIntento.hexdigest()}')

#generate_password_hash

variableConGenerate = generate_password_hash("1234567890")
variable2ConGenerate = generate_password_hash("5555555555")

print(f'Variables con gener4ate_password_hash {variableConGenerate}')
print(f'Variables con gener4ate_password_hash {variable2ConGenerate}')

if check_password_hash(variableConGenerate, "5"):
    print("access guaranted1")
else:
    print("access denegated1")

if check_password_hash(variable2ConGenerate, "5"):
    print("access guaranted2")
else:
    print("access denegated2")
