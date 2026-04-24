from validate import validar_id, validar_nombre, validar_correo
from file import load_data, save_data

def crear_registro(id, nombre, correo):
    try:
        registros = load_data()
        ids = {str(r["id"]) for r in registros}

        id_validado = validar_id(id, ids)
        nombre_validado = validar_nombre(nombre)
        correo_validado = validar_correo(correo)

        nuevo = {
            "id": id_validado,
            "nombre": nombre_validado,
            "correo": correo_validado
        }

        registros.append(nuevo)
        save_data(registros)
        print(" Registro guardado en archivo")

    except ValueError as e:
        print(f" {e}")


def listar_registros():
    registros = load_data()

    if not registros:
        print("No hay registros")
        return

    for r in registros:
        print(r)


def buscar_registro(id):
    registros = load_data()

    for r in registros:
        if str(r["id"]) == str(id):
            return r

    return None


def actualizar_registro(id, nuevo_nombre=None, nuevo_correo=None):
    try:
        registros = load_data()

        for r in registros:
            if str(r["id"]) == str(id):
                if nuevo_nombre:
                    r["nombre"] = validar_nombre(nuevo_nombre)
                if nuevo_correo:
                    r["correo"] = validar_correo(nuevo_correo)

                save_data(registros)
                print(" Registro actualizado")
                return

        print(" Registro no encontrado")

    except ValueError as e:
        print(f" {e}")


def eliminar_registro(id):
    registros = load_data()
    nuevos = [r for r in registros if str(r["id"]) != str(id)]

    if len(nuevos) == len(registros):
        print(" Registro no encontrado")
        return

    save_data(nuevos)
    print(" Registro eliminado")