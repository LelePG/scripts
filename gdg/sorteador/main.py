import pandas as pd
from leitor import LeitorExcelSympla
import random
import logging
import os

if __name__ == "__main__":
    caminhoPlanilha = 'planilha.xlsx'  ## alterar caso necessário
    leitor = LeitorExcelSympla()  ## alterar caso necessário
    ingressosParaIgnorar = ["Organização e Palestrantes"]  ## alterar caso necessário

    if not os.path.exists(caminhoPlanilha):
        print(f"Erro: O arquivo {caminhoPlanilha} não foi encontrado.")
        exit(1)
        
        
    logging.basicConfig(filename='sorteio.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    participantes = leitor.ler(caminhoPlanilha, ingressosParaIgnorar)
    jaSorteados = []
    
    
    while True:
        premio = input("O que será sorteado? ")
        
        if premio == "" or premio.lower().strip() == "sair":
            break
        
        qtde_sorteios = int(input("Quantos usuários devem ser sorteados? "))
        
        print("Aperte enter para iniciar o sorteio")
        input()
        
        for i in range(qtde_sorteios):
            sorteado = random.sample(participantes, 1)[0]
            jaSorteados.append(sorteado)
            participantes = [p for p in participantes if p not in jaSorteados]
            print("\033c", end="")
            print(f"O ganhador do sorteio {i+1} de {premio} é: {sorteado.nome_completo}")
            print("Aperte enter para continuar.")
            logging.info(f"O ganhador do sorteio {i+1} de {premio} é: {sorteado}")
            input()
            print("\033c", end="")

            
        continuar = input("Iniciar outro sorteio? (s/N) ")
        
        if continuar.lower().strip() == "s":
            print("\033c", end="")
            continue
        
        break
        