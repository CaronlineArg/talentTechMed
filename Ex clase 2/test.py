""" Actividad 1:

Define variables para almacenar el nombre, edad y profesión del usuario.

Solicita estos datos por teclado utilizando input().

Imprime en pantalla un mensaje personalizado incluyendo todos estos datos.

Actividad 2:

Escribe un pequeño script que utilice un bucle para mostrar los primeros 10 números pares.

Usa condicionales para validar y mostrar sólo los números pares. """
nombre = input("cual es tu nombre?")
edad =str(input("cual es tu edad?"))
profesion = input("cual es tu profesion?")
print("tu nombre es: " + nombre + "edad: "+ edad + "profesion: " + profesion)

contador= 0
while contador < 10:
    contador += 1
    if (contador % 2==0):
        print(contador)
    else:
        print("-")
    