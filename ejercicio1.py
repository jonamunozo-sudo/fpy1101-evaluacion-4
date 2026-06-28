def mostrar_menu():
    print("\n........MENU PRINCIPAL ........")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("........................................")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion (1-6): "))
            return opcion
        except ValueError:
            print("Error: Por favor, ingrese un numero entero valido.")

def validar_titulo(titulo):
    return bool(titulo and titulo.strip())

def validar_copias(copias_str):
    if copias_str.isdigit():
        return int(copias_str) >= 0
    return False

def validar_prestamo(prestamo_str):
    if prestamo_str.isdigit():
        return int(prestamo_str) > 0
    return False

def agregar_libro(lista_libros):
    print("\n--- AGREGAR NUEVO LIBRO ---")
    titulo = input("Ingrese el titulo del libro: ")
    copias_raw = input("Ingrese la cantidad de copias: ")
    prestamo_raw = input("Ingrese el período de prestamo (en dias): ")

    if not validar_titulo(titulo):
        print("Error: El titulo no puede estar vacio ni contener solo espacios.")
        return

    if not validar_copias(copias_raw):
        print("Error: Las copias deben ser un numero entero mayor o igual que cero.")
        return

    if not validar_prestamo(prestamo_raw):
        print("Error: El periodo de prestamo debe ser un numero entero mayor que cero.")
        return


    nuevo_libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_raw),
        "prestamo": int(prestamo_raw),
        "disponible": False
    }
    
    lista_libros.append(nuevo_libro)
    print(f"¡Libro '{nuevo_libro['titulo']}' agregado exitosamente!")


def buscar_libro(lista_libros, titulo_buscar):
    for i in range(len(lista_libros)):
        if lista_libros[i]["titulo"] == titulo_buscar:
            return i
    return -1

def actualizar_disponibilidad(lista_libros):
    for libro in lista_libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

def main():
    biblioteca = []
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_libro(biblioteca)
            
        elif opcion == 2:
            print("\n--- BUSCAR LIBRO ---")
            titulo_buscar = input("Ingrese el título del libro a buscar: ")
            posicion = buscar_libro(biblioteca, titulo_buscar)
            
            if posicion != -1:
                libro = biblioteca[posicion]
                print(f"\nLibro encontrado en la posicion: {posicion}")
                print(f"Titulo: {libro['titulo']}")
                print(f"Copias: {libro['copias']}")
                print(f"Prestamo: {libro['prestamo']} dias")
                print(f"Disponible: {'Si' if libro['disponible'] else 'No'}")
            else:
                print("El libro no se encuentra registrado.")
                
        elif opcion == 3:
            print("\n--- ELIMINAR LIBRO ---")
            titulo_eliminar = input("Ingrese el título del libro que desea eliminar: ")
            posicion = buscar_libro(biblioteca, titulo_eliminar)
            
            if posicion != -1:
                libro_eliminado = biblioteca.pop(posicion)
                print(f"¡El libro '{libro_eliminado['titulo']}' ha sido eliminado exitosamente!")
            else:
                print(f"El libro '{titulo_eliminar}' no se encuentra registrado.")
                
        elif opcion == 4:
            actualizar_disponibilidad(biblioteca)
            print("\nDisponibilidad de todos los libros actualizada correctamente.")
            
        elif opcion == 5:
            actualizar_disponibilidad(biblioteca)
            
            print("\n...LISTA DE LIBROS ...")
            if not biblioteca:
                print("(La biblioteca esta vacia)")
            else:
                for libro in biblioteca:
                    print(f"Titulo: {libro['titulo']}")
                    print(f"Copias: {libro['copias']}")
                    print(f"Prestamo: {libro['prestamo']}")
                    estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                    print(f"Estado: {estado}")
                    print("\...................................... ")
                    
        elif opcion == 6:
            print("\nGracias por usar el sistema. Vuelva Pronto")
            break
            
        else:
            print("Opcion invalida. Intente con un número del 1 al 6.")

if __name__ == "__main__":
    main()