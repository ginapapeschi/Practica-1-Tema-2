from ClaseMama import Mama
import csv
import numpy as np

class GestorMama:
    __listaGMama: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int

    def __init__ (self):
        self.__dimension = 17
        self.__cantidad = 0
        self.__incremento = 5
        self.__listaGMama = np.empty(self.__dimension, dtype = Mama)
    
    def agregarMama(self, nuevo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaGMama.resize(self.__dimension)
        else:
            self.__listaGMama[self.__cantidad] = nuevo
            self.__cantidad += 1

    def leerdatos(self):
        archivo = open('Mamas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                dni = fila [0]
                edad = fila[1]
                ayn = fila [2]
                nuevaMama = Mama(dni, edad, ayn)
                self.agregarMama(nuevaMama)
        archivo.close()

    def buscarDNI(self, xdni):
        i = 0
        pos = -1
        band = True
        while i < len(self.__listaGMama) and band:
            print("X")
            if self.__listaGMama[i].getDNI() == xdni:
                pos = i
                band = False
            else:
                i += 1
        return(pos)

    def mostrarInfoMama(self, GN):
        print("\n")
        dni = int(input("Ingrese el DNI: "))
        pos = self.buscarDNI(dni)
        if pos != -1:
             for i in (self.__listaGMama):
                print("Información de la madre:")
                AyN = self.__listaGMama[pos].getAyN()
                edad = self.__listaGMama[pos].getEdad()
                print(f"""
                    Apellido y Nombre: {AyN}
                    Edad: {edad} """)
    
            