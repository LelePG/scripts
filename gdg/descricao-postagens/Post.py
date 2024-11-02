from datetime import datetime, timedelta

class PostFactory:
    def __init__(self, evento, link_inscricao, local, data, hora, hashtags, caminho_output):
        self.EVENTO = evento
        self.LINK_INSCRICAO = link_inscricao
        self.LOCAL = local
        self.DATA = data
        self.HORA = hora
        self.HASHTAGS = hashtags
        self.CAMINHO_OUTPUT = caminho_output
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
        self.texto += f"{texto}\n\n"
        return self

    def comLocal(self):
        self.texto += f"📍 Local: {self.LOCAL}\n\n"
        return self

    def comDataHora(self):
        self.texto += f"📅 {self.DATA} - {self.HORA}\n\n"
        return self

    def comLinkInscricao(self):
        self.texto += f"🔗 Inscrições: {self.LINK_INSCRICAO}\n\n"
        return self

    def comCabecalhoOrganizacao(self, titulo):
        return (self
                .comDivisorInicio()
                .comTituloOrganizacao(titulo)
                .comDivisorIntermediario()
                )
    
    def comFinalizacao(self):
        return (self
                .comHashtags()
                .comDivisorFim()
                )

    def comInscricaoELocal(self):
        return (self
                .comLinkInscricao()
                .comDataHora()
                .comLocal()
                )
    
    def mostrar(self):
        print(self.texto)

    def salvar(self):
        with open(self.CAMINHO_OUTPUT, 'a') as f:
            f.write(self.texto)
        self.texto = ""
    
    def gerar(self):
        return self.texto
    
    def deFaltamDias(self, diasFaltantes):
        data_evento = datetime.strptime(f"{self.DATA}/2024", '%d/%m/%Y')
        data_postagem = data_evento - timedelta(days=int(diasFaltantes))
        return (self
                .comDivisorInicio()
                .comTituloOrganizacao(f'Faltam {diasFaltantes} dias')
                .comTexto(f"Data da postagem: {data_postagem.strftime('%d/%m/%Y')}")
                .comDivisorIntermediario()
                .comTexto(f"⏳ Faltam {str(diasFaltantes).zfill(2)} dias para o {self.EVENTO} ")
                .comTexto(f"O {self.EVENTO} está chegando e ainda dá tempo de garantir o seu ingresso.")
                .comInscricaoELocal()
                .comFinalizacao()
                )

    def deEHoje(self):
        data_postagem = datetime.strptime(f"{self.DATA}/2024", '%d/%m/%Y')
        return (self
                .comDivisorInicio()
                .comTituloOrganizacao(f'É hoje!')
                .comTexto(f"Data da postagem: {data_postagem.strftime('%d/%m/%Y')}")
                .comDivisorIntermediario()
                .comTexto(f"🎉 O {self.EVENTO} é hoje! ")
                .comTexto(f"Esperamos todo mundo logo mais no {self.LOCAL} às {self.HORA}.")
                .comFinalizacao()
                )
    
    def deEAmanha(self):
        data_evento = datetime.strptime(f"{self.DATA}/2024", '%d/%m/%Y')
        data_postagem = data_evento - timedelta(days=int(1))
        return (self
                .comDivisorInicio()
                .comTituloOrganizacao(f'É amanhã')
                .comTexto(f"Data da postagem: {data_postagem.strftime('%d/%m/%Y')}")
                .comDivisorIntermediario()
                .comTexto(f"🎉 É amanhã! ")
                .comTexto(f"O {self.EVENTO} está chegando! Amanhã, dia {self.DATA}, te esperamos no {self.LOCAL} às {self.HORA}.")
                .comFinalizacao()
                )

    def dePatrocinador(self, patrocinador):
        return (self
                .comCabecalhoOrganizacao(f'Patrocinador {patrocinador.strip()}')
                .comTexto(f"🤝 O {patrocinador.strip()} é um patrocinador oficial do {self.EVENTO}!")
                .comTexto(f"Agradecemos demais por possibilitar que o {self.EVENTO} seja possível!")
                .comFinalizacao()
                )
    
    def deApoiador(self, apoiador):
        return (self
                .comCabecalhoOrganizacao(f'Apoiador {apoiador.strip()}')
                .comTexto(f"🤝 O {apoiador.strip()} é um apoiador oficial do {self.EVENTO}!")
                .comTexto(f"Agradecemos demais por possibilitar que o {self.EVENTO} seja possível!")
                .comFinalizacao()
                )

    def dePalestrante(self, nome, titulo, resumo, mini_bio):
        return (self
                .comCabecalhoOrganizacao(f'Palestrante {nome}')
                .comTexto(f"📣 Palestra Confirmada {self.EVENTO}!")
                .comTexto(f"⭐ {titulo}")
                .comTexto(f"🎤 {nome}")
                .comTexto("📘 Descrição da palestra:")
                .comTexto(resumo)
                .comTexto("📘 Bio do palestrante:")
                .comTexto(mini_bio)
                .comInscricaoELocal()
                .comFinalizacao()
                )

    def deHorasComplementares(self):
        return (self
                .comCabecalhoOrganizacao('Horas complementares')
                .comTexto("📣 Precisando de horas complementares para a faculdade?")
                .comTexto(f"O {self.EVENTO} terá certificado de participação com a carga horária correspondente ao evento. Se você está precisando de horas complementares, não perca essa oportunidade!")
                .comTexto(f"Te esperamos no {self.EVENTO}!")
                .comInscricaoELocal()
                .comFinalizacao()
                )

    def deComoChegar(self):
        return (self
                .comCabecalhoOrganizacao('Como Chegar')
                .comTexto(f"⏳ O {self.EVENTO} está chegando!")
                .comTexto(f"O {self.EVENTO} acontecerá dia {self.DATA} no {self.LOCAL}. ")
                .comTexto(f"O credenciamento começa às {self.HORA} e recomendamos que você se planeje para chegar ao local do evento com antecedência para evitar transtornos.")
                .comTexto("Tem alguma dúvida de como chegar ao local do evento? Dá uma olhadinha no nosso guia!")
                .comFinalizacao()
                )
    
    def deGuiaPreparacao(self):
        return (self
                .comCabecalhoOrganizacao('Guia de Preparação')
                .comTexto(f"⏳ O {self.EVENTO} está chegando!")
                .comTexto("Não esquece de conferir o nosso guia de preparação com algumas informações importantes!")
                .comFinalizacao()
                )

    def deProgramacao(self):
        return (self
                .comCabecalhoOrganizacao('Programação')
                .comTexto(f"🕖 Olha a programação do {self.EVENTO} na sua timeline!")
                .comTexto(f"O {self.EVENTO} está chegando e a programação já está disponível! Confira as palestras incríveis que vão rolar nesse evento.")
                .comInscricaoELocal()
                .comFinalizacao()
                )
        
    def deIngressosEsgotados(self):
        return self.comCabecalhoOrganizacao('Ingressos Esgotados')
        .comTexto(f"🚨 Os ingressos para o {self.EVENTO} estão esgotados! 🚨")
        .comTexto(f"Agradecemos imensamente a todos que garantiram sua presença. Estamos animados para compartilhar momentos incríveis com vocês no dia {self.DATA}.")
        .comTexto(f"Nos vemos no {self.EVENTO}!")
        .comHashtags()
        .comFinalizacao()

    def deNaoEsquecaCopo(self):
        return (self
                .comCabecalhoOrganizacao('Não esqueça seu copo')
                .comTexto("🌱 Traga seu copo para o ${self.EVENTO}! 💚")
                .comTexto("Pedimos que todos tragam seus copos reutilizáveis, pois não teremos copos descartáveis no evento.")
                .comTexto("Assim, ajudamos a reduzir o uso de plástico e deixamos nosso evento ainda mais sustentável.")
                .comTexto("E quem trouxer o seu copo ainda vai ganhar um brinde especial.")
                .comTexto("Contamos com vocês!")
                .comInscricaoELocal()
                .comFinalizacao()
                
    def deNaoEsquecaAlimento(self):
        return (self
                .comCabecalhoOrganizacao('Não esqueça seu alimento')
                .comTexto("🍽️ Se você optou pelo ingresso + alimento, não esqueça de levar 1kg de alimento não perecível para o evento 🍽️")
                .comTexto("Lembramos que a entrada de quem comprou este tipo de ingresso só será permitida para aqueles que apresentarem o alimento na entrada. Contamos com a sua colaboração!")
                .comInscricaoELocal()
                .comFinalizacao()
                )
    
    def deSaveTheDate(self):
        return (self
                .comCabecalhoOrganizacao('Save the Date')
                .comTexto(f"📅 Anote na agenda!")
                .comTexto(f"No dia {self.DATA} acontecerá o {self.EVENTO}.")
                .comTexto(f"Fique de olho nas nossas redes para mais informações.")
                .comFinalizacao()
                )
    

    def deC4p(self):
        return (self
                .comCabecalhoOrganizacao('Call for Papers')
                .comTexto("🎤 Que tal compartilhar seus conhecimentos sobre tecnologia com a comunidade?")
                .comTexto("O call for papers para o {self.EVENTO} que acontecerá dia {self.DATA} em Pelotas está aberto, e essa é a sua oportunidade de compartilhar seus conhecimentos sobre tecnologia com a comunidade. Não deixe de subtemer a sua palestra, e qualquer dúvida, manda uma mensagem pra gente!")
                .comInscricaoELocal()
                .comFinalizacao()
                )

    def de1loteComCamiseta(self):
        return (self
                .comCabecalhoOrganizacao('Ingressos Abertos')
                .comTexto("🎫 Os ingressos para o {self.EVENTO} estão abertos!")
                .comTexto("E nesse evento, além de ter o melhor preço, os ingressos do primeiro lote tem uma novidade: agora você pode optar por um ingresso que inclui uma camiseta oficial do evento além do ingresso comum.")
                .comTexto("Garanta logo o seu ingresso e a sua camiseta!")
                .comInscricaoELocal()
                .comFinalizacao()
                )

    def deTragaSeuLixo(self):
        return (self
                .comCabecalhoOrganizacao('Ponto de Coleta de Lixo Tecnológico')
                .comTexto("🗑️ Ponto de Coleta de Lixo Tecnológico no DevFest Rio Grande do Sul 2024!")
                .comTexto("Você tem algum eletrônico que não usa mais? Que tal trazê-lo para descarte no ponto de coleta do Pelotas Parque Tecnológico? Você ajuda a o meio ambiente a ainda libera um espacinho a mais na sua casa!")
                .comInscricaoELocal()
                .comFinalizacao()
                )

