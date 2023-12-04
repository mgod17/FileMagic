import os
from core.file_manager import FileManager

def main():
    carpeta_descargas = "C:/Users/Mariano/Downloads"
    file_manager = FileManager(carpeta_descargas)

    while True:
        print("\n1. Organizar los archivos de descargas")       
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            file_manager.crear_carpetas()
            file_manager.mover_archivos(
                os.path.join(file_manager.folder_path, "Organizados")
            )
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
