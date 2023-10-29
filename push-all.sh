#!/bin/bash


pasta_principal="$PWD"


# Verifique se a pasta inicial existe
if [ -d "$pasta_principal" ]; then
    # Iterar sobre as pastas filhas
    for repositorio in "$pasta_principal"/*; do
        if [ -d "$repositorio/.git" ]; then
            # Verifique se a pasta é um repositório Git
            echo "Fazendo push em $repositorio"
            # Navegar até o diretório do repositório
            cd "$repositorio"
            # Executar o git push
            git push
            # Voltar para a pasta raiz
            cd "$pasta_principal"
        fi
    done
else
    echo "A pasta inicial não existe."
fi

