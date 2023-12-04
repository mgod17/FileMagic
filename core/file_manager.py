import os
import shutil


class FileManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def crear_carpetas(self):
        carpeta_organizados = os.path.join(self.folder_path, "Organizados")
        sub_carpetas = ["Imagenes", "Videos", "Documentos", "Musica", "Otros"]

        if not os.path.exists(carpeta_organizados):
            os.makedirs(carpeta_organizados)

        for sub_carpeta in sub_carpetas:
            sub_carpeta_path = os.path.join(carpeta_organizados, sub_carpeta)
            if not os.path.exists(sub_carpeta_path):
                os.makedirs(sub_carpeta_path)
        print("Carpetas y sub-carpetas creadas con exito")

    def mover_archivos(self, carpeta_organizados):
        subcarpetas = ["Imagenes", "Videos", "Documentos", "Musica", "Otros"]
        for archivo in os.listdir(self.folder_path):
            archivo_path = os.path.normpath(os.path.join(self.folder_path, archivo))
            if os.path.isfile(archivo_path):
                try:
                    tipo_archivo = self.obtener_tipo_archivo(archivo_path)
                    if tipo_archivo in subcarpetas:
                        nombre_archivo = os.path.basename(archivo_path)
                        destino_path = os.path.join(
                            carpeta_organizados, tipo_archivo, nombre_archivo
                        )
                        shutil.move(archivo_path, destino_path)
                except FileNotFoundError:
                    print(f"Archivo no encontrado: {archivo}")

    def obtener_tipo_archivo(self, archivo_path):
        try:
            extension = os.path.splitext(archivo_path)[1].lower()

            tipo_a_carpeta = {
                ".jpg": "Imagenes",
                ".jpeg": "Imagenes",
                ".png": "Imagenes",
                ".gif": "Imagenes",
                ".mp4": "Videos",
                ".avi": "Videos",
                ".pdf": "Documentos",
            }

            tipo_carpeta = tipo_a_carpeta.get(extension, "Otros")

            return tipo_carpeta
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo_path}")
        return "Otros"
