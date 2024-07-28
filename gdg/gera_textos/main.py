import os
from dotenv import load_dotenv
import csv
from factories.Gerador import Gerador

load_dotenv()

def exibir_menu():
    print("Selecione o tipo de postagem que deseja gerar:")
    print("1. Post Faltam X dias")
    print("2. Post É Amanhã")
    print("3. Post É Hoje")
    print("4. Post Patrocinadores")
    print("5. Post Apoiadores")
    print("6. Post Palestrantes")
    print("7. Post Como Chegar")
    print("8. Post Horas Complementares")
    print("9. Post Guia de Preparação")
    print("10. Post Programação")
    print("11. Email Palestra Não Aceita")
    print("12. Email Palestra Aceita")
    print("13. Email Confirmação de Informações")
    print("14. Email Últimos Avisos")
    print("0. Sair")
    
gerador = Gerador(
    os.getenv("EVENTO"),
    os.getenv("LINK_INSCRICAO"),
    os.getenv("LOCAL"),
    os.getenv("DATA"),
    os.getenv("HORA"),
    os.getenv("HASHTAGS"),
    os.getenv("LINK_MODELO_SLIDES")
)

def executar_opcao(opcao):
    if opcao == "1":
        gerador.postFaltamDias()
    elif opcao == "2":
        gerador.postEAmanha()
    elif opcao == "3":
        gerador.postEHoje()
    elif opcao == "4":
        gerador.postDePatrocinadores()
    elif opcao == "5":
        gerador.postDeApoiadores()
    elif opcao == "6":
        gerador.postPalestrantes()
    elif opcao == "7":
        gerador.postComoChegar()
    elif opcao == "8":
        gerador.postHorasComplementares()
    elif opcao == "9":
        gerador.postGuiaPreparacao()
    elif opcao == "10":
        gerador.postProgramacao()
    elif opcao == "11":
        gerador.emailPalestraNaoAceita()
    elif opcao == "12":
        gerador.emailPalestraAceita()
    elif opcao == "13":
        gerador.emailConfirmacaoInfo()
    elif opcao == "14":
        gerador.emailUltimosAvisos() 
    else:
        print("Opção inválida.")


while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "0":
        break
    executar_opcao(opcao)