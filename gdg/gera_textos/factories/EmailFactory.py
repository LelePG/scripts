from datetime import datetime, timedelta

class EmailFactory:
    def __init__(self, evento, data, caminho_output):
        self.EVENTO = evento
        self.DATA = data
        self.CAMINHO_OUTPUT = caminho_output
        self.texto = ""

    def comDivisorInicio(self):
        self.texto = f"{'=*'*25}\n{self.texto}"
        return self

    def comDivisorFim(self):
        self.texto += f"{'=*'*25}\n\n"
        return self

    def comDivisorIntermediario(self):
        self.texto += f"{'='*50}\n"
        return self

    def comTexto(self, texto):
        self.texto += f"{texto}\n\n"
        return self
    
    def comInfoEnvio(self, email, assunto):
        self.texto += f"Email:{email}\nAssunto: {assunto}\n"
        return self
    
    def comOi(self, nome):
        self.texto += f"Olá, {nome}, tudo bem?\n\n"
        return self
    
    def comTchau(self):
        self.texto += f"Atenciosamente\nOrganização GDG Pelotas\n"
        return self
    
    def comLinkModelo(self, link):
        self.texto += f"Link modelo: {link}\n"
        return self
    
    def comCabecalhoPadrao(self,email, nome, assunto):
        return self.comDivisorInicio().comInfoEnvio(email, assunto).comDivisorIntermediario().comOi(nome)    
    
    def dePalestraNaoAceita(self, email, nome, tituloPalestra):
        return self.comCabecalhoPadrao(email, nome, f"Retorno Call For Papers {self.EVENTO}").comTexto(f"Ficamos muito felizes que você tenha submetido a sua palestra '{tituloPalestra}', para o {self.EVENTO} e agradecemos imensamente pela sua dedicação, disposição em transmitir conhecimento e por cada segundo gasto preparando sua submissão.").comTexto("Tivemos muitas atividades incríveis submetidas, mas não foi possível selecionar todas elas. Infelizmente, não pudemos alocar sua atividade em nossa programação, mas gostaríamos de agradecer pela sua submissão e pela confiança em nossa comunidade.").comTexto("Mais uma vez, agradecemos pelo seu tempo e disposição, e gostaríamos de convidar você a prestigiar as atividades da nossa programação.").comTexto(f"Se tiver alguma dúvida ou sugestão, não hesite em nos contatar.").comTchau().comDivisorFim()
        
    def dePalestraAceita(self, email, nome, tituloPalestra, data):
        return self.comCabecalhoPadrao(email, nome, f"Sua palestra foi aceita para o {self.EVENTO}"). comTexto(f"Ficamos muito felizes em receber sua proposta de palestra para o {self.EVENTO} e é com muita alegria que informamos que a sua palestra '{tituloPalestra}' foi selecionada para o evento!").comTexto(f"Estamos enviando este e-mail para solicitar a confirmação da sua presença no evento que acontecerá no dia {data} em Pelotas–RS.").comTexto(f"Se tiver alguma dúvida, sugestão ou reclamação, não hesite em nos contatar.").comTchau().comDivisorFim()

        
    def deConfirmacaoInfo(self, email, nome, tituloPalestra, mini_bio, resumo, link_modelo_slides):
        return self.comDivisorInicio().comInfoEnvio(email, f"Confirmação de informações {self.EVENTO}").comLinkModelo(link_modelo_slides).comDivisorIntermediario().comOi(nome).comTexto(f"Estamos enviando este e-mail para confirmar alguns detalhes de divulgação da sua palestra '{tituloPalestra}'. Precisamos de um ok da sua mini-bio, da descrição da palestra e da arte de divulgação que está anexada a este e-mail.").comTexto(f"Mini-Bio:\n{mini_bio}").comTexto(f"Descrição da palestra:\n{resumo}").comTexto("Se quiser fazer alguma alteração na mini-bio, na descrição ou na arte de divulgação, por favor, nos avise.").comTexto("Já vou aproveitar esse email pra dar alguns avisos rápidos. Ainda estamos montando a grade do evento, então se você tiver alguma restrição de horário, por favor nos avise para que possamos encontrar o horário mais adequado. O credenciamento do evento começa às 13:30, e a abertura às 14:00, com previsão de ir até as 18:00. Também temos um modelo de slides disponível que pode ser acessado clicando aqui. O uso do modelo é opcional, então você pode se sentir a vontade para utilizar o modelo que preferir.").comTchau().comDivisorFim()
        
    def deUltimosAvisos(self,email, nome, prazo_slides):
        return self.comCabecalhoPadrao(email, nome, "Ultimos Avisos").comTexto(f"O {self.EVENTO} está chegando e nós estamos trabalhando muito por aqui para fazermos um evento incível em conjunto!").comTexto("Tenho alguns avisos importantes para compartilhas:").comTexto(f"1. Em breve enviaremos para vocês o link de um grupo no Whatsapp exclusivo para palestrantes no evento. Esse grupo serve apenas para facilitar a comunicação com a organização do evento no dia do evento, e a participação nele é opcional.").comTexto("2. O seu ingresso para o evento foi gerado pela plataforma e faremos o seu chekin de forma automática, então você não precisa se preocupar com ele.").comTexto(f"3. Como o evento está chegando, pedimos que você nos envie uma versão em PDF dos seus slides até {prazo_slides}, como medida de segurança. Se você quiser levar o seu notebook para apresentar seus slides na sua própria máquina, pode levar, desde que ele tenha uma entrada HDMI. Essa versão em PDF só será usada em caso de emergência, ou então de preferência da palestrante, já que algumas pessoas preferem fazer a apresentação dessa forma. Salientamos que os slides devem ser enviados em formato PDF, o que garante que a sua apresentação não sofrerá modificações no software de apresentação das máquinas do evento, que provavelmente estarão configuradas com Linux.").comTexto("Até logo").comTchau().comDivisorFim()
    
    def salvar(self):
        with open(self.caminho_output, 'a') as f:
            f.write(self.texto)
        self.texto = ""
        
    def gerar(self):
        return self.texto
    