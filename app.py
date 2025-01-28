"""
Python Básico: Explicaciones y ejemplos
Este script contiene los conceptos básicos de Python con ejemplos explicados.
"""

# 1. Variables Básicas
# Una variable es un contenedor para almacenar datos.
# Se asignan usando el signo igual (=).

# Enteros (int): Números enteros positivos o negativos
edad = 25  # Un número entero
print(f"Edad: {edad}")

# Flotantes (float): Números con decimales
pi = 3.1416  # Número con decimales
print(f"Valor de pi: {pi}")

# Cadenas de texto (str): Texto entre comillas
nombre = "Omar"  # Una cadena de texto
print(f"Hola, mi nombre es {nombre}")

# Booleanos (bool): Verdadero o Falso
es_estudiante = True  # Un valor booleano
print(f"¿Eres estudiante? {es_estudiante}")

# 2. Operaciones Matemáticas
# Python soporta operaciones básicas como suma, resta, multiplicación y división
x = 10
y = 5

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y  # Siempre devuelve un flotante
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# División entera y módulo
division_entera = x // y  # División sin decimales
modulo = x % y  # Residuo de la división
print(f"División entera: {division_entera}, Módulo: {modulo}")

# Potencia
potencia = x ** y  # x elevado a la y
print(f"Potencia: {potencia}")

# 3. Estructuras de Datos
# Listas: Colección de elementos ordenados que pueden cambiar
frutas = ["manzana", "pera", "naranja"]  # Lista de cadenas
print(f"Frutas: {frutas}")

# Diccionarios: Colección de pares clave-valor
persona = {
    "nombre": "Omar",
    "edad": 25,
    "es_estudiante": True
}
print(f"Datos de la persona: {persona}")

# Tuplas: Colección de elementos ordenados e inmutables
coordenadas = (10.5, -20.3)
print(f"Coordenadas: {coordenadas}")

# Conjuntos: Colección de elementos únicos
colores = {"rojo", "verde", "azul"}
print(f"Colores: {colores}")

# 4. Condicionales
# Permiten tomar decisiones en base a condiciones
if es_estudiante:
    print("Eres estudiante.")
else:
    print("No eres estudiante.")

# 5. Bucles
# Bucle for: Itera sobre una colección
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Bucle while: Repite mientras una condición sea verdadera
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# 6. Funciones
# Bloque de código reutilizable que realiza una tarea específica

def saludar(nombre):
    """Esta función saluda a una persona por su nombre."""
    return f"Hola, {nombre}!"

mensaje = saludar("Omar")
print(mensaje)

# 7. Manejo de Errores
# Uso de try-except para manejar excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# 8. Archivos
# Leer y escribir en archivos
# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("¡Hola, este es un archivo de prueba!")

# Leer un archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(f"Contenido del archivo: {contenido}")

# 9. Importar Módulos
# Python tiene módulos que puedes importar para usar funcionalidades adicionales
import math
raiz_cuadrada = math.sqrt(16)  # Calcula la raíz cuadrada
print(f"Raíz cuadrada de 16: {raiz_cuadrada}")

# 10. Clases y Objetos
# Concepto básico de programación orientada a objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

omar = Persona("Omar", 25)
print(omar.presentarse())

# ¡Listo! Este script cubre los conceptos básicos de Python.
