import os

from utilidades.helpers import Helper


class FileManager:

    @staticmethod
    def lector(ruta):
        informacionParseada= []
        if not os.path.exists(ruta):
            return False, "La ruta no existe"
        with open(ruta,"r",encoding="utf-8") as f:
            linea = f.read().splitlines()
            for datos in linea:

                informacionParseada.append(Helper.convertirTextoAObjeto(datos))

            return True, "información leida correctamente",informacionParseada

    @staticmethod
    def guardar(ruta, contenido):

        os.makedirs(
            os.path.dirname(ruta) if os.path.dirname(ruta) else ".",
            exist_ok=True
        )#Comprueba los directorios de la ruta, si no tiene el directorio es esta carpeta, si ya existe no crea nada y no da error
        with open(ruta,"a",encoding="utf-8") as f:
            f.write(contenido)


