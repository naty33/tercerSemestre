# Declaramos una variable
'''try:
    archivo = open('prueba.txt', 'w')#La w es la de write que significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo'''

try:
    archivo = open('prueba.txt', 'w', encoding= 'utf8')#La w es la de write que significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo
#al ejecutar el finally el archivo ya sse cerro....por lo que no se deben cvargar mas modificaciones al archivo
#archivo.write('Todo quedo perfecto'): dejamos como comentario para quer no altere el archivo cerrado

