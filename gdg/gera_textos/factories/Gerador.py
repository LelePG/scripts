from .PostFactory import PostFactory
from .EmailFactory import EmailFactory
class Gerador:
    def __init__(self, evento, link_inscricao, local, data, hora, hashtags, link_modelo_slides, caminho_output="output.txt"):
        self.EVENTO = evento
        self.LINK_INSCRICAO = link_inscricao
        self.LOCAL = local
        self.DATA = data
        self.HORA = hora
        self.HASHTAGS = hashtags
        self.ARQUIVO_CSV = ""
        self.LINK_MODELO_SLIDES = link_modelo_slides
        self.post = PostFactory(self.EVENTO, self.LINK_INSCRICAO, self.LOCAL, self.DATA, self.HORA, self.HASHTAGS, caminho_output)
        self.email = EmailFactory(self.EVENTO, self.DATA, caminho_output)
        
    def postFaltamDias(self):
        dias = input("Digite os dias separados por vírgula: ")
        lista_dias = dias.split(',')
        for dia in lista_dias:
            self.post.deFaltamDias(dia).salvar()
    
    def postEAmanha(self):
        self.post.deEAmanha().salvar()
        
    def postEHoje(self):
        self.post.deEHoje().salvar()
    
    def postDePatrocinadores(self):
        patrocinadores = input("Digite os patrocinadores separados por vírgula: ")
        for p in patrocinadores.split(','):
            self.post.dePatrocinador(p).salvar()
    
    def postDeApoiadores(self):
        apoiadores = input("Digite os apoiadores separados por vírgula: ")
        for a in apoiadores.split(','):
            self.post.deApoiador(a).salvar()
            
    def postComoChegar(self):
        self.post.deComoChegar().salvar()
        
    def postHorasComplementares(self):
        self.post.deHorasComplementares().salvar()
    
    def postGuiaPreparacao(self):
        self.post.deGuiaPreparacao().salvar()
    
    def postProgramacao(self):
        self.post.deProgramacao().salvar()
        
    def processarCSV(self,acaoLinha):
        if not self.ARQUIVO_CSV:
            textoInput = input("Digite o nome do arquivo csv (enter para 'planilha'): ")
            self.ARQUIVO_CSV = textoInput if textoInput else "planilha"            

        with open(f"{self.ARQUIVO_CSV}.csv") as csvfile:
            leitor_csv = csv.DictReader(csvfile)
            for linha in leitor_csv:
                acaoLinha(linha)
        
    def postPalestrantes(self):
        self.processarCSV(lambda linha: self.post.dePalestrante(linha["nome"], linha["titulo"], linha["resumo"], linha["mini-bio"]).salvar())

    def emailPalestraNaoAceita(self):
        self.processarCSV(lambda linha: self.email.dePalestraNaoAceita(linha["email"], linha["nome"], linha["titulo"]).salvar())

    def emailPalestraAceita(self):
        self.processarCSV(lambda linha: self.email.dePalestraAceita(linha["email"],linha["nome"], linha["titulo"], self.DATA).salvar())

    def emailConfirmacaoInfo(self):
        self.processarCSV(lambda linha: self.email.deConfirmacaoInfo(linha["email"],linha["nome"], linha["titulo"], linha["mini-bio"], linha["resumo"], self.LINK_MODELO_SLIDES).salvar())
    
    def emailUltimosAvisos(self):
        prazo = input("Digite até quando é pra mandar os slides: ")
        self.processarCSV(lambda linha: self.email.deUltimosAvisos(linha["email"],linha["nome"], prazo).salvar())
