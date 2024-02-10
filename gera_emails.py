# -*- coding: utf-8 -*-

"""
    Script para automatizar a escrita de e-mails para eventos. 
    Inputs necessários: 
    - um arquivo de texto com o modelo do texto
    - um arquivo csv com os dados a serem utilizados
    As chaves de substituição do texto devem estar no formato ${nome-coluna}
    Importante: nome-coluna deve ser exatamente o nome da coluna onde aquela informação está armazenada no arquivo csv
    Outputs: Arquivos com o texto do modelo adaptado e nomes compostos de um prefixo a ser definido e um número
    Exemplo de chamada: python3 gera_emails.py modelo.txt arquivo.csv 'resultado' 
    Definição de alias (deve ser feita no arquivo .zshrc ou .bashrc): alias gera_emails='python3 ~/scripts/gera_emails.py'
"""
import csv
import re
import argparse

parser = argparse.ArgumentParser(description='Script para automatizar a escrita de e-mails para eventos.')

parser.add_argument('ARQUIVO_MODELO', type=str, help='O nome do arquivo de modelo')
parser.add_argument('ARQUIVO_CSV', type=str, help='O nome do arquivo csv')
parser.add_argument('PREFIXO_SAIDA', type=str, help='Prefixo dos arquivos de saída')

args = parser.parse_args()

# ler o texto do modelo
with open(args.ARQUIVO_MODELO, 'r') as arquivo:
    texto = arquivo.read()

# Pegar todas as coisas que precisarão ser interpoladas
padrao = r'\$\{([^}]*)\}'
lista = re.findall(padrao, texto)

with open(args.ARQUIVO_CSV) as csvfile:
    leitor_csv = csv.DictReader(csvfile)
    numero = 1

    for linha in leitor_csv:
        copiaTexto = texto

        for item in lista:
            copiaTexto = copiaTexto.replace('${'+item+'}', linha[item])

        nome_arquivo = f'{args.PREFIXO_SAIDA}{numero}.txt'

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(copiaTexto)

        numero += 1

