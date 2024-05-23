class Mama:
    __dni: int
    __edad: int
    __AyN: str

    def __init__(self, xdni, xedad, ayn):
        self.__dni = xdni
        self.__edad = xedad
        self.__AyN = ayn

    def __str__ (self):
        return (f"""
            Apellido y Nombre: {self.__AyN}
            Edad: {self.__edad} """)

    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getAyN(self):
        return self.__AyN