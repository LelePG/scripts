from Post import Post

def exibir_menu():
    print("Selecione o tipo de postagem que deseja gerar:")
    print("1. Faltam X dias")
    print("2. Patrocinadores")
    print("3. Palestrantes")
    print("4. Como Chegar")
    print("5. Horas Complementares")
    print("6. Guia de Preparação")
    print("7. Programação")
    print("0. Sair")

def executar_opcao(opcao):
    if opcao == "1": # Faltam X dias
        dias = input("Digite os dias separados por vírgula: ")
        lista_dias = dias.split(',')
        for dia in lista_dias:
            Post().deFaltamDias(dia).salvar()
    elif opcao == "2": # Patrocinadores
        patrocinadores = input("Digite os patrocinadores separados por vírgula: ")
        for p in patrocinadores.split(','):
            Post().dePatrocinador(p).salvar()
    elif opcao == "3": # Palestrantes
        arquivo_csv = input("Digite o nome do arquivo csv: ")
        with open(arquivo_csv) as csvfile:
            leitor_csv = csv.DictReader(csvfile)
            for linha in leitor_csv:
                Post().dePalestrante(linha["nome"], linha["titulo"], linha["resumo"], linha["mini-bio"]).salvar()
    elif opcao == "4": # Como Chegar
        Post().deComoChegar().salvar()
    elif opcao == "5": # Horas Complementares
        Post().deHorasComplementares().salvar()
    elif opcao == "6": # Guia de Preparação
        Post().deGuiaPreparacao().salvar()
    elif opcao == "7": # Programação
        Post().deProgramacao().salvar()
    else:
        print("Opção inválida.")


while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "0":
        break
    executar_opcao(opcao)