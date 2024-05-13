from Clientes import GestorCli
from Movimientos import GestorMov

#agregado
def menu_opciones():
    op = int(input("""

                                    MENÚ DE OPCIONES
        (1) Ingresa DNI del cliente para actualizar saldo con operaciones
        (2) Ingresa DNI del cliente para mostrar nombre y apellido si no hubo movimientos
        (3) Ordenar movimientos por número de cuentas
        (0) Salir
        --> """))
    return op
#agregado

if __name__== "__main__":
    print("a")
    gestCli = GestorCli()
    gestMov = GestorMov()
    gestCli.leerdatos()
    gestMov.leerdatos()
    opcion = menu_opciones()
    print("a")
    while opcion != 0:
        if opcion == 1:
            gestCli.actualiza_sald(gestMov)
        elif opcion == 2:
            gestCli.mostrarDatos_siNoHayMov(gestMov)
        elif opcion == 3:
            gestMov.ordenarMov()
            gestMov.listarMov()
        else:
            print("¡Opción inválida!")
        opcion = menu_opciones()