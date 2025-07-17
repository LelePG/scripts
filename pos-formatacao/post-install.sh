#!/bin/bash

function notificacao() {
  echo $*
  notify-send " $*"
}

function configurar_git() {
  notificacao "Iniciando configuração do Git"
  
  read -p "Nome: " NOME
  read -p "E-mail: " EMAIL

  if ! [ -x "$(command -v git)" ]; then
    sudo apt-get install git
  fi

  # Configuração de credenciais
  git config --global user.name "$NOME"
  git config --global user.email $EMAIL

  # Chave SSH
  ssh-keygen -t ed25519 -C "$EMAIL"
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519

  echo "Copie a chave do arquivo ~/Desktop/chave.txt e cole na plataforma correspondente"
  cat ~/.ssh/id_ed25519.pub > ~/Desktop/chave.txt
  
  notificacao "Configuração do Git concluída"
}

function configurar_zsh() {
  notificacao "Iniciando configuração do ZSH"
  
   if ! [ -x "$(command -v zsh)" ]; then
    sudo apt-get install zsh
  fi

  sudo chsh -s $(which zsh)
  sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
  
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
  echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
  
  notificacao "ZSH instalado! Reinicie o computador para aplicar as alterações e fazer a configuração do terminal"
}

function configurar_vscode(){
    notificacao "Iniciando configuração do Visual Studio Code"
    
    EXTENSOES=(
        mhutchie.git-graph
        MS-vsliveshare.vsliveshare
        ritwickdey.LiveServer
        formulahendry.code-runner
        usernamehw.errorlens
        rangav.vscode-thunder-client
        esbenp.prettier-vscode
        BeardedBear.beardedtheme
        BeardedBear.beardedicons
        firsttris.vscode-jest-runner
        bradlc.vscode-tailwindcss
        oderwat.indent-rainbow
        GitHub.copilot
        GitHub.copilot-chat
        johnpapa.vscode-peacock
        docker.docker
        humao.rest-client
        mechatroner.rainbow-csv
        Prisma.prisma
        mongodb.mongodb-vscode
        bierner.markdown-mermaid
        pomdtr.excalidraw-editor
        streetsidesoftware.code-spell-checker
        streetsidesoftware.code-spell-checker-portuguese-brazilian
        formulahendry.auto-rename-tag
        redhat.vscode-yaml
        yzhang.markdown-all-in-one
        Cardinal90.multi-cursor-case-preserve
        wix.vscode-import-cost
        tomoki1207.pdf
        heybourn.headwind
        aaron-bond.better-comments
        meganrogge.template-string-converter
        ReacTreeDev.reactree
    )
    
    for extensao in ${EXTENSOES[@]}; do
        if code --list-extensions | grep -q "$extensao"; then
            echo "[JÁ EXISTE] - $extensao"
        else
            echo "[INSTALANDO] - $extensao"
            code --install-extension "$extensao" 2>> log.txt
        fi
    done
}

function configurar_node(){
    PACOTES_NODE=(@nestjs/cli)
    for pacote in ${PACOTES_NODE[@]}; do
        if npm list -g "$pacote" --depth=0 2>/dev/null | grep -q "$pacote"; then
            echo "[JÁ EXISTE] - $pacote"
        else
            echo "[INSTALANDO] - $pacote"
            npm install -g "$pacote" 2>> log.txt
        fi
    done
    notificacao "Volta, Node.JS e pacotes Node.js instalados."
}

function configurar_imagens_docker(){
    notificacao "Iniciando configuração do Docker"
    
    IMAGENS_DOCKER=(
        mongo:latest
        postgres:latest
        mysql:latest
        ollama:latest
        n8nio/n8n:latest
    )
    
    for imagem in ${IMAGENS_DOCKER[@]}; do
        if docker images | grep -q "$imagem"; then
            echo "[JÁ EXISTE] - $imagem"
        else
            echo "[BAIXANDO] - $imagem"
            docker pull "$imagem" 2>> log.txt
        fi
    done
    
    notificacao "Instalação de imagens do Docker concluída"
}


while true; do
    clear
    echo "=========================================="
    echo "        MENU DE PÓS-INSTALAÇÃO           "
    echo "=========================================="
    echo ""
    echo "Escolha uma opção:"
    echo "1. Configurar Git"
    echo "2. Configurar ZSH com Oh-My-ZSH e PowerLevel10k"
    echo "3. Instalar Extensões no Visual Studio Code"
    echo "4. Instalar pacotes Node"
    echo "5. Instalar Imagens do Docker"
    echo "6. Configurar todos (Git, ZSH, VSCode, Node.js e Docker)"
    echo "7. Sair"
    echo ""
    
    read -p "Digite sua opção: " opcao
    
    case $opcao in
        1)
            configurar_git
            read -p "Pressione Enter para continuar..."
            ;;
        2)
            configurar_zsh
            read -p "Pressione Enter para continuar..."
            ;;
        3)
            configurar_vscode
            read -p "Pressione Enter para continuar..."
            ;;
        4)
            configurar_node
            read -p "Pressione Enter para continuar..."
            ;;
        5)
            configurar_imagens_docker
            read -p "Pressione Enter para continuar..."
            ;;
        6)
            configurar_git
            configurar_zsh
            configurar_vscode
            configurar_node
            configurar_imagens_docker
            read -p "Pressione Enter para continuar..."
            ;;
        7)
            notificacao "Finalizando script de pós-instalação"
            exit 0
            ;;
        *)
            echo "Opção inválida!"
            read -p "Pressione Enter para continuar..."
            ;;
    esac
done

