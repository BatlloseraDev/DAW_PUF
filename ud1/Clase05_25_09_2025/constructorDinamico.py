class AtributosPersona:
    def __init__(self, altura, **kwargs):
        self.altura = altura
        self.peso = kwargs.get("peso",0)
        self.gafas = kwargs.get("gafas",None)


atributos = AtributosPersona(altura=180, peso=70, gafas=True)

print(atributos.peso)
print(atributos.gafas)