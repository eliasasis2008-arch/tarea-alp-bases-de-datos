import sqlite3

conn = sqlite3.connect(r"videojuegos.db")
cursor = conn.cursor()
print("conexion establecida")
conn.commit()


def mostrar_videojuegos():
    cursor.execute("SELECT * FROM videojuegos")
    videojuego = cursor.fetchall()

    if videojuego:
        for juego in videojuego:
            print(juego)
    else:
        print("No hay videojuegos registrados.")


while True:
    print("\n VIDEOJUEGO")
    print("1. Mostrar todos los videojuegos")
    print("2. Buscar por id")
    print("3. Agregar un videojuego")
    print("4. Modificar el precio de un videojuego")
    print("5. Eliminar un videojuego")
    print("6. Salir")

    opcion = input("Elegi una opcion: ")

   
    if opcion == "1":
        mostrar_videojuegos()

    
    elif opcion == "2":
        id = input("Ingresa el id que queres buscar: ")

        cursor.execute(
            "SELECT * FROM videojuegos WHERE id = ?",
            (id,)
        )

        videojuegos = cursor.fetchall()

        if videojuegos:
            for juego in videojuegos:
                print(juego)
        else:
            print("No se encontraron juegos con ese id.")

    
    elif opcion == "3":
        id = input("Ingresa el id del videojuego: ")
        titulo = input("Ingresa el titulo del videojuego: ")
        precio = input("Ingresa su precio: ")
        genero = input("Ingresa su genero: ")
        año = input("Ingresa su año de lanzamiento: ")

        cursor.execute(
            "INSERT INTO videojuegos (id, titulo, precio, genero, año) VALUES (?, ?, ?, ?, ?)",
            (id, titulo, precio, genero, año)
        )

        conn.commit()

        print("videojuego agregado correctamente.")
        print("Tabla actualizada:")
        mostrar_videojuegos()

    
    
    elif opcion == "4":
        id = input("Ingresa el id del videojuego que queres modificar: ")
        precio = input("Ingresa el nuevo precio: ")

        cursor.execute(
            "UPDATE videojuegos SET precio = ? WHERE id = ?",
            (precio, id)
        )

        conn.commit()

        print("videojuego actualizado correctamente.")
        print("Tabla actualizada:")
        mostrar_videojuegos()

    
    elif opcion == "5":
        id  = input("Ingresa el id del videojuego que queres eliminar: ")

        cursor.execute(
            "DELETE FROM videojuegos WHERE id = ?",
            (id,)
        )

        conn.commit()
        print("videojuego eliminado correctamente.")

        print("Tabla actualizada:")
        mostrar_videojuegos()

    
    elif opcion == "6":
        print("Cerrando el programa...")
        break

    else:
        print("Opcion invalida. Elegi un numero del 1 al 6.")

conn.close()
print("Conexion cerrada.")