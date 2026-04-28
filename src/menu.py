from service import (
    crear_registro,
    listar_registros,
    buscar_registro,
    actualizar_registro,
    eliminar_registro
)
from colorama import init, Fore, Style, Back
from integration import export_to_csv, generate_report

init(autoreset=True)

def menu():
    print(Back.RED+ "                            ")
    print(Fore.RED + "    SISTEMA DE REGISTROS    ")
    print(Back.RED+ "                            ")

    while True:
        print(Fore.RED + "\n1. Crear registro")
        print(Fore.WHITE + "2. Listar registros")
        print(Fore.RED + "3. Buscar registro")
        print(Fore.WHITE + "4. Actualizar registro")
        print(Fore.RED + "5. Eliminar registro")
        print(Fore.WHITE + "6. Exportar a CSV")
        print(Fore.RED + "7. Salir")

        opcion = input(Fore.WHITE + "\nSeleccione una opción: ")

        if opcion == "1":
            id = input(Style.BRIGHT + "Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese correo: ")
            crear_registro(id, nombre, correo)

        elif opcion == "2":
            print(Fore.RED + "\n--- LISTA DE REGISTROS ---")
            listar_registros()

        elif opcion == "3":
            id = input(Style.BRIGHT + "Ingrese ID a buscar: ")
            resultado = buscar_registro(id)
            if resultado:
                print(Fore.RED + "\n--- REGISTRO ENCONTRADO ---")
                print(resultado)
            else:
                print(" Registro no encontrado")

        elif opcion == "4":
            id = input(Style.BRIGHT + "Ingrese ID a actualizar: ")
            if not buscar_registro(id):
                print(" Registro no encontrado")
                continue
            print("(Deje en blanco para no cambiar)")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_correo = input("Nuevo correo: ")
            actualizar_registro(id, nuevo_nombre or None, nuevo_correo or None)

        elif opcion == "5":
            id = input(Style.BRIGHT + "Ingrese ID a eliminar: ")
            eliminar_registro(id)
        elif opcion == "6":
            export_to_csv()
        elif opcion == "8":
            generate_report()
        elif opcion == "7":
            print(Fore.RED + "Saliendo del sistema...")
            break

        else:
            print(Fore.RED + "Opción inválida")