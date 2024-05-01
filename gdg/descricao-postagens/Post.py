import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()

class Post:
    def __init__(self):
        self.EVENTO = os.getenv('EVENTO')
        self.LINK_INSCRICAO = os.getenv('LINK_INSCRICAO')
        self.LOCAL = os.getenv('LOCAL')
        self.DATA = os.getenv('DATA')
        self.HORA = os.getenv('HORA')
        self.HASHTAGS = os.getenv('HASHTAGS')
        self.texto = ""

    def comHashtags(self):
        self.texto += self.HASHTAGS + "\n"
        return self

    def comDivisorInicio(self):
        self.texto = f"{'=*'*25}\n{self.texto}"
        return self

    def comDivisorFim(self):
        self.texto += f"{'=*'*25}\n\n"
        return self

    def comDivisorIntermediario(self):
        self.texto += f"{'='*50}\n"
        return self

    def comTituloOrganizacao(self, titulo):
        self.texto += f"Titulo da postagem: {titulo}\n"
        return self
    

    def comTexto(self, texto):
        self.texto += f"{texto}\n"
        return self

    def comLocal(self):
        self.texto += f"📍 Local: {self.LOCAL}\n"
        return self

    def comDataHora(self):
        self.texto += f"📅 {self.DATA} - {self.HORA}\n"
        return self

    def comLinkInscricao(self):
        self.texto += f"🔗 Inscrições: {self.LINK_INSCRICAO}\n"
        return self

    def comCabecalhoPadrao(self, titulo):
        return (self
                .comDivisorInicio()
                .comTituloOrganizacao(titulo)
                .comDivisorIntermediario()
                )
    
    def comFooterPadrao(self):
        return (self
                .comHashtags()
                .comDivisorFim()
                )

    def comFooterInformativo(self):
        return (self
                .comLinkInscricao()
                .comDataHora()
                .comLocal()
                .comFooterPadrao()
                )
    
    def mostrar(self):
        print(self.texto)

    def salvar(self, nome_arquivo="output.txt"):
        with open(nome_arquivo, 'a') as f:
            f.write(self.texto)
    
    def deFaltamDias(self, dia):
        data_evento = datetime.strptime(f"{self.DATA}/2024", '%d/%m/%Y')
        data_postagem = data_evento - timedelta(days=int(dia))
        return (self
                .comDivisorInicio()
                .comTituloOrganizacao(f'Faltam {dia} dias')
                .comTexto(f"Data da postagem: {data_postagem.strftime('%d/%m/%Y')}")
                .comDivisorIntermediario()
                .comTexto(f"⏳ Faltam {str(dia).zfill(2)} dias para o {self.EVENTO} ")
                .comTexto(f"O {self.EVENTO} está chegando e ainda dá tempo de garantir o seu ingresso.")
                .comFooterInformativo()
                )

    def dePatrocinador(self, patrocinador):
        return (self
                .comCabecalhoPadrao(f'Patrocinador {patrocinador}')
                .comTexto(f"🤝 O {patrocinador} é um patrocinador oficial do {self.EVENTO}")
                .comTexto(f"Agradecemos demais por possibilitar que o {self.EVENTO} seja possível!")
                .comFooterPadrao()
                )

    def dePalestrante(self, nome, titulo, resumo, mini_bio):
        return (self
                .comCabecalhoPadrao(f'Palestrante {nome}')
                .comTexto(f"📣 Palestra Confirmada {self.EVENTO}!")
                .comTexto(f"⭐ {titulo}")
                .comTexto(f"🎤 {nome}")
                .comTexto("📘 Descrição da palestra:")
                .comTexto(resumo)
                .comTexto("📘 Bio do palestrante:")
                .comTexto(mini_bio)
                .comFooterInformativo()
                )

    def deHorasComplementares(self):
        return (self
                .comCabecalhoPadrao('Horas complementares')
                .comTexto("📣 Precisando de horas complementares para a faculdade?")
                .comTexto(f"O {self.EVENTO} terá certificado de participação com a carga horária correspondente ao evento. Se você está precisando de horas complementares, não perca essa oportunidade!")
                .comTexto(f"Te esperamos no {self.EVENTO}!")
                .comFooterInformativo()
                )

    def deComoChegar(self):
        return (self
                .comCabecalhoPadrao('Como Chegar')
                .comTexto(f"⏳ O {self.EVENTO} está chegando!")
                .comTexto(f"O {self.EVENTO} acontecerá dia {self.DATA} no {self.LOCAL}. ")
                .comTexto(f"O credenciamento começa às {self.HORA} e recomendamos que você se planeje para chegar ao local do evento com antecedência para evitar transtornos.")
                .comTexto("Tem alguma dúvida de como chegar ao local do evento? Dá uma olhadinha no nosso guia!")
                .comFooterPadrao()
                )
    
    def deGuiaPreparacao(self):
        return (self
                .comCabecalhoPadrao('Guia de Preparação')
                .comTexto(f"⏳ O {self.EVENTO} está chegando!")
                .comTexto("Não esquece de conferir o nosso guia de preparação com algumas informações importantes!")
                .comFooterPadrao()
                )

    def deProgramacao(self):
        return (self
                .comCabecalhoPadrao('Programação')
                .comTexto(f"🕖 Olha a programação do {self.EVENTO} na sua timeline!")
                .comTexto(f"O {self.EVENTO} está chegando e a programação já está disponível! Confira as palestras incríveis que vão rolar nesse evento.")
                .comFooterInformativo()
                )
