# print() muestra mensajes al usuario
print("hola mundo alv")

# len() sirve paara contar el la cantidad de objetos 
print(len(str(123456789)))

#str() convierte todo a strings
print(str("hola mundo alv"))
print(int(123456))

#Listas
numeros = [1,2,3,4,5,6,7,8,9]
 
#sort() cambia el orden de los numeros en la lista
numeros.sort()
print(numeros)

#reverse() invierte el orden de los numeros de la lista
numeros.reverse()
print(numeros)

#append() agrega un nueo elemento a la lista
numeros.append(199)
print(numeros)

#INDICE para mostrar un nmero en especifico
print(numeros[0])
print(numeros[1])

#Diccionario
usuario = {'nombre':'Walter','edad':'19','ciudad':'Guatemala'}
print(usuario['nombre'])

#Agregar un nuevo elemento a la lista
usuario['lenguaje_actual'] = 'Python'
print(usuario)

#contar la cantidad de objetos en una lista
print(len(usuario))

#pop() borra un elemento del diccionario
usuario.pop('edad')
print(usuario)

#Modificar un valor existente de un diccionario
usuario['nombre'] = 'Estuardo'
print(usuario)

#if y else 
edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

#funciones
def saludo():
    print("Hola!")
    print("Como estan?")
saludo()

name = input("Ingresa tu nombre: ")
def hi(name):
        print("Hola "+name+"!")
        print("Como estas?")
hi(name)

#Bucles
for i in range(1,6):
    print(i)

def SaludarTodas(nombre):
    print("Hola "+nombre+"!")

girls = ['Rachel','Sophie','Esther','Pamela','Monica']
for nombre in girls:
    SaludarTodas(nombre)
    print("Siguiente")

#while
usuarios = []
pregunta = input("Desea agregar un usuario? S/N: ")
while pregunta == "s":
    dpi = input("Ingresa tu DPI: ")
    pin = input("Ingreas tu PIN: ")

    usuario = {}
    usuario[dpi] = dpi
    usuario[pin] = pin

    usuarios.append(usuario)

    print(usuarios)

    pregunta = input("Desea agregar un usuario? S/N: ")

buscar_dpi = input("Busca tu DPI: ")
buscar_pin = input("Busca tu PIN: ")
if buscar_dpi == dpi and buscar_pin == pin:
    print("Datos correctos!")
else:
    print("Datos no coinciden")

print(usuario[dpi])
print(usuario[pin])
