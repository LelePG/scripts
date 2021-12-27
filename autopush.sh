#!/bin/bash

# Criação de um alias para este script
#pastaAtual= pwd | tr -d '\n'
#arquivo="/autopush.sh"
#alias autopush="$pastaAtual$arquivo"

git add --all
git commit -m "$1"
git push


