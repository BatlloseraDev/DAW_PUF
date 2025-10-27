from datetime import  date


from modelos.heroe import Heroe
from modelos.villano import Villano


class Helper:

    rutaGuardadoHeroe= "data/heroes.txt"
    rutaGuardadoVillano = "data/villanos.txt"

    @staticmethod
    def convertirObjetoATexto(objeto):
        texto = ""
        if type(objeto) is Heroe :
            texto +="Heroe/"
            arrais= vars(objeto)
            for key, value in arrais.items():
                texto += f"{value}/" # texto += f"{key}:{value}/"


        elif type(objeto) is Villano :
            texto += "Villano/"
            arrais = vars(objeto)
            for key, value in arrais.items():
                texto += f"{value}/"

        else:
            return False, "error al convertir un objeto a texto"
        texto = texto[:-1]
        texto+="\n"
        return True, texto

    @staticmethod
    def convertirTextoAObjeto(datos):
        contenido= datos.split("/")
        objeto= None
        if contenido[0] == "Heroe":
            fecha= contenido[3].split("-")
            fecha = list(map(int, fecha))
            objeto= Heroe(contenido[1],contenido[2],date(fecha[0],fecha[1],fecha[2]),contenido[4],codigoLimpio=int(contenido[5]),
                          bienDocumentado=int(contenido[6]),gitgod=int(contenido[7]),arquitecto=int(contenido[8]),
                          detallista=int(contenido[9]))

        elif contenido[0] == "Villano":
            fecha = contenido[3].split("-")
            fecha = list(map(int, fecha))
            objeto = Villano(contenido[1], contenido[2], date(fecha[0], fecha[1], fecha[2]), contenido[4],
                           chagepeteador=int(contenido[5]),entregadorTardio= int(contenido[6]),
                            ausencias= int(contenido[7]),hablador= int(contenido[8]))

        return objeto

    @staticmethod
    def devolverRutaGuardado(tipo):
        if tipo == 1:
            return Helper.rutaGuardadoHeroe
        elif tipo == 2:
            return Helper.rutaGuardadoVillano
        else:
            return None