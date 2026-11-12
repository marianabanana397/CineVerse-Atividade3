class Catalogo:
    def __init__(self, titulo, tipo, genero, ano, id=None):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.ano = ano

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "tipo": self.tipo,
            "genero": self.genero,
            "ano": self.ano
        }