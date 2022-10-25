from sys import path
path.append('..\\Paquetes')

import primo.primo
print(primo.primo.es_primo(int(input("Vamos a descubrir un numero primo. Introduzca un numero:"))))

import operacion.operacion
print("Ahora vamos hacer una operacón para esto: ")
print(operacion.operacion.operacion(int(input("Introduzca el primer numero: ")),int(input("Introduzca el primer numero: "))))

import Funciones.module
print("Ahora unos números pares: ")
print(Funciones.module.pares())

import Funciones.module
print("Ahora unos números impares: ")
print(Funciones.module.impares())

