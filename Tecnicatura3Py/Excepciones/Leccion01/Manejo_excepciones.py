'''
try:
    10/0
except ZeroDivisionError as e:
    print (f'Ocurrio un error: {e}')

try:
    10/0
except ZeroDivisionError as e:
    print (f'Ocurrio un error: {e}')

resultado = None
a = 10
b = 0
try:
    resultado = a / b #modificamos
except Exception as e:
    print (f'Ocurrio un error: {e}')

print(f'El resultado es: {resultado}')
print('seguimos...')

resultado = None
a = 7
b = 0
try:
    resultado = a / b #modificamos
except TypeError as e:
    print (f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print (f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:#Clase padre al final para ser preciso en el error los demas son clases hijas con errores especificos
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')

print(f'El resultado es: {resultado}')
print('seguimos...')'''
'''
resultado = None

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    resultado = a / b #modificamos
except TypeError as e:
    print (f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print (f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:#Clase padre al final para ser preciso en el error los demas son clases hijas con errores especificos
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')

print(f'El resultado es: {resultado}')
print('seguimos...')'''
from NumerosIgualesException import NumerosIgualesException
resultado = None

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    if a == b:
        raise NumerosIgualesException('Son numeros iguales')
    resultado = a / b #modificamos
except TypeError as e:
    print (f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print (f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:#Clase padre al final para ser preciso en el error los demas son clases hijas con errores especificos
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
else:
    print("No se arrojo ninguna excepción")
finally:#Siempre se va a ejecutar
    print("Ejecución de este bloque finally")

print(f'El resultado es: {resultado}')
print('seguimos...')




