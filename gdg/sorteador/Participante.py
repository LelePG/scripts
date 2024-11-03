class Participante:
    def __init__(self, nome, sobrenome, email, ingresso):
        self.nome_completo = f"{nome.strip()} {sobrenome.strip()}".capitalize()
        self.email = email
        self.ingresso = ingresso

    def __repr__(self):
        return f"Participante(nome_completo='{self.nome_completo}', email='{self.email}', ingresso='{self.ingresso}')"