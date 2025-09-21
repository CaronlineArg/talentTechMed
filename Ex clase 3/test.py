""" 
Excepciones

try:
    valor = int(input("Ingresa un número entero: "))
    resultado = 10 / valor
    print(f"10 / {valor} = {resultado}")
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Entrada inválida, no es un número entero.")
finally:
    print("Operación finalizada.")

    

    Actividad 1: Mejorando la calculadora

Refactorizar el script de la calculadora lineal en al menos 4 funciones separadas. una por cada tipo de operación. Como ser: Sumar(), Restar(), Multiplicar() y Dividir()

Añadir manejo de excepciones para entradas inválidas y división por cero.

Actividad 2: Git y Github

Git local

Crear una carpeta nueva para el proyecto de calculadora.

Inicializar un repositorio con git init.

Agregar y confirmar cambios con git add y git commit.

GitHub

Crear una cuenta en github.com si no tenés una.

Crear un nuevo repositorio desde tu perfil (usá el mismo nombre del proyecto).

Copiar la URL del repositorio (HTTPS).

Enlazar el repositorio local con GitHub.

Subir los archivos usando git push.

Flujo de trabajo con Git y GitHub.

Crear un repositorio en GitHub: Vas a GitHub, creás un nuevo repositorio y le ponés un nombre descriptivo.

Vincular repositorio local con GitHub: Abrí tu terminal y escribí este comando para vincular tu repositorio local con el que creaste en GitHub:

git remote add origin https://github.com/tu-usuario/proyecto.git

Subir cambios a GitHub: Después de hacer algunos cambios y hacer commits, podés subirlos a GitHub con el comando:

git push -u origin main

Comandos Básicos de Git

git init

Convierte la carpeta actual en un repositorio Git local

git clone URL

Descarga una copia de un repositorio remoto

git status

Muestra el estado actual del repositorio

git add archivo.txt

Añade un archivo al área de preparación

git commit -m "mensaje"

Crea un nuevo commit con los cambios preparados

git push origin main

Envía los commits locales al repositorio remoto

git pull origin main

Obtiene y fusiona cambios del repositorio remoto

git branch nueva-rama

Crea una nueva rama

git checkout nueva-rama

Cambia a la rama especificada

"""

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def dividir(a,b):
    if (b==0):
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a/b
def multiplicar(a,b):
    return a*b
def exponenciar(a,b):
    return a**b
def modulo(a,b):
    return a%b

def calculadora():
    print("Calculadora")
    a=float(input("ingrese un numero para calcular"))
    print("menu de operaciones: 1) sumar 2) restar, 3) dividir, 4) multiplicar, 5) exponenciar, 6) modulo")
    opciones=input("ingresa numero de operación")
    b=float(input("ingrese un numero para calcular"))
    try:
        if opciones=="1": resultado = sumar(a,b)
        elif opciones=="2": resultado = restar(a,b)
        elif opciones=="3": resultado = dividir(a,b)
        elif opciones=="4": resultado = multiplicar(a,b)
        elif opciones=="5": resultado = exponenciar(a,b)
        elif opciones=="6": resultado = modulo(a,b)
        else:
            print("Opción inválida.") 
            return 
        print(f"Resultado: {resultado}")
    except ZeroDivisionError as e:
        print(f"error: {e}")        

if __name__ == '__main__': 
    calculadora()