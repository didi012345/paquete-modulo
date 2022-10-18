from sys import path
path.append('..\\Paquetes')

import primo.primo
print(primo.primo.es_primo(int(input("introduzca un numero:"))))

import Funciones.module
print(Funciones.module.pares())

import Funciones.module
print(Funciones.module.impares())

import operacion.operacion
print(operacion.operacion.operacion(10,9))
