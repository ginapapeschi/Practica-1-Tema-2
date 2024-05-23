from GestorMamas import GestorMama
from GestorNacimientos import GestorNacimiento
def menu():
    op = input("""
                            MENÚ DE OPCIONES
            (a) Ingresar el DNI de una mamá para mostrar su información.
            (b) Mostrar datos de la/s mamá/s que han tenido parto múltiple.
            (0) Cerrar menú.
            Su opción --> """)
    return op

if __name__ == '__main__':
    GMama = GestorMama()
    GNac = GestorNacimiento()
    GMama.leerdatos()
    GNac.leerdatos()
    opcion = menu()
    while opcion != 0:
        if opcion == 'a':
            GMama.mostrarInfoMama(GNac)
        
        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:
            pass

    
    opcion = menu()