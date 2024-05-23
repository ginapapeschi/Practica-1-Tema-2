from ClaseBebe import Bebe
import csv

class GestorNacimiento:
    __listaGNac: list

    def __init__(self):
        self.__listaGNac = []

    def agregarNacimiento(self, nuevo):
        self.__listaGNac.append(nuevo)

    def leerdatos(self):
        archivo = open('Nacimientos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                dni = fila[0]
                tipo = fila[1]
                fecha =  fila[2]
                peso = fila[3]
                altura = fila[4]
                nuevoBebe = Bebe (dni, tipo, fecha, peso, altura)
                self.agregarNacimiento(nuevoBebe)
        archivo.close()

