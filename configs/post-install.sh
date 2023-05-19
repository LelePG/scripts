#!/bin/bash

# testa se o flatpak está instalado
if ! [ -x "$(command -v flatpak)" ]; then
  echo 'Instale o Flatpack.' >&2
  exit 1
fi

if ! [ -x "$(command -v snap)" ]; then
  echo 'Instale o snap.' >&2
  exit 1
fi

if ! [ -x "$(command -v espeak)" ]; then
  sudo apt-get install espeak #mensagens de audio que serão usadas durante a instalação
fi


function notificacao(){
  echo $*
  espeak -s 150 -v pt+f4 " $*"
  notify-send " $*"
}

notificacao "Iniciando"


PROGRAMAS_FLATPAK=(
cc.arduino.IDE2
com.getpostman.Postman
nl.hjdskes.gcolor3
org.flameshot.Flameshot
org.audacityteam.Audacity
org.videolan.VLC
org.kde.kdenlive
com.obsproject.Studio
org.deluge_torrent.deluge
com.spotify.Client
org.gnome.Extensions
io.github.mpobaschnig.Vaults
net.supertuxkart.SuperTuxKart
com.stepmania.StepMania
com.discordapp.Discord
org.kicad.KiCad
com.github.k4zmu2a.spacecadetpinball
com.github.suzie97.communique
com.lakoliu.Furtherance
io.github.Qalculate
io.github.lainsce.Emulsion
io.github.slgobinath.SafeEyes
io.posidon.Paper
md.obsidian.Obsidian
org.kde.ktouch 
)

#lutris
PROGRAMAS_APT=(
php
mysql-server
gnome-tweak-tool
peek
gparted
traceroute
unrar
lm-sensors
net-tools
postgresql
nodejs
gocryptfs
)

PROGRAMAS_SNAP=(
pomatez
brave
mysql-workbench-community
chromium
stacer 
zenkit
)


#Instalação dos programas flatpak
for programa in ${PROGRAMAS_FLATPAK[@]}; do
  if ! flatpak list | grep -q $programa; then # Só instala se já não estiver instalado
    echo "[INSTALANDO] - $programa"
    flatpak install flathub "$programa" -y >>2 log.txt
  else
    echo "[JÁ EXISTE] - $programa"
  fi
done
notificacao "Programas Flatpak instalados. Insira a senha pra instalações a p t."

#add-apt-repository ppa:lutris-team/lutris #adiciona lutris aos repositórios

#Instalação dos programas apt
for programa in ${PROGRAMAS_APT[@]}; do
  if ! dpkg -l | grep -q $programa; then # Só instala se já não estiver instalado
    echo "[INSTALANDO] - $programa"
    sudo apt-get install "$programa"  2>> log.txt
  else
    echo "[JÁ EXISTE] - $programa"
  fi
done

notificacao "Programas a p t instalados. Insira a senha pra instalações isnépi."
#Instalação dos programas snap
for programa in ${PROGRAMAS_SNAP[@]}; do
  if ! snap list | grep -q $programa; then # Só instala se já não estiver instalado
    sudo snap install "$programa"  2>> log.txt
    echo "[INSTALANDO] - $programa"
  else
    echo "[JÁ EXISTE] - $programa"
  fi
done

notificacao "Programas isnépi instalados. Vamos para os próximos script."


#mysql_secure_installation 

# Scripts adicionais
chmod +x config-git.sh
chmod +x config-vscode.sh
chmod +x config-zsh.sh
chmod +x config-node.sh
chmod +x clonando-repos.sh

# notificacao "Hora de configurar o Guit"
#./config-git
# notificacao "Hora de configurar o node"
#./config-node
# notificacao "Hora de configurar o terminal"
#./config-zsh
# notificacao "Hora de configurar o vs code"
#./config-vscode


echo "OS PROGRAMAS ESTÃO PRONTOS UHUUUUUU!!!"
espeak -s 150 -v pt+f4 'Tudo pronto'



