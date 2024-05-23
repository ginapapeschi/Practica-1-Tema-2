class Bebe:
    __dniMama: float
    __tipoParto: str
    __FyHnacimiento: str
    __peso: float
    __altura: float

    def __init__(self, dni, tipo, fyh, xpeso, alt):
        self.__dniMama = dni
        self.__tipoParto = tipo
        self.__FyHnacimiento = fyh
        self.__peso = xpeso
        self.__altura = alt

    def getDNImama(self):
        return self.__dniMama
    
    def getTipoParto(self):
        return self.__tipoParto
    
    def getFyH(self):
        return self.__FyHnacimiento
    
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__altura
