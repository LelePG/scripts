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

echo "Iniciando a instalação..."

PROGRAMAS_FLATPAK=(
org.octave.Octave
cc.arduino.arduinoide
#net.sonic_pi.SonicPi
com.getpostman.Postman
com.getferdi.Ferdi
nl.hjdskes.gcolor3
org.flameshot.Flameshot
org.audacityteam.Audacity
org.videolan.VLC
org.kde.kdenlive
com.obsproject.Studio
org.deluge_torrent.deluge
#com.stremio.Stremio
com.spotify.Client
org.gnome.gitlab.somas.Apostrophe
org.gnome.Extensions
io.github.mpobaschnig.Vaults
#org.supertuxproject.SuperTux
net.supertuxkart.SuperTuxKart
#org.desmume.DeSmuME
#io.mgba.mGBA
com.stepmania.StepMania
)

PROGRAMAS_APT=(
php
mysql-server
gnome-tweak-tool
peek
gparted
traceroute
unrar
lutris
lm-sensors
net-tools
)

PROGRAMAS_SNAP=(
pomatez
brave
mysql-workbench-community
chromium
)


#Instalação dos programas flatpak
for programa in ${PROGRAMAS_FLATPAK[@]}; do
  if ! dpkg -l | grep -q $programa; then # Só instala se já não estiver instalado
    flatpak install flathub "$nome_do_programa" -y > /dev/null
    echo "[INSTALANDO] - $nome_do_programa"
  else
    echo "[JÁ EXISTE] - $nome_do_programa"
  fi
done

sudo su # muda para o super usuario já que vou precisar do sudo pros comandos abaixo
add-apt-repository ppa:lutris-team/lutris #adiciona lutris aos repositórios

#Instalação dos programas apt
for programa in ${PROGRAMAS_APT[@]}; do
  if ! dpkg -l | grep -q $programa; then # Só instala se já não estiver instalado
    apt install "$nome_do_programa" -y > /dev/null
    echo "[INSTALANDO] - $nome_do_programa"
  else
    echo "[JÁ EXISTE] - $nome_do_programa"
  fi
done

#Instalação dos programas snap
for programa in ${PROGRAMAS_SNAP[@]}; do
  if ! dpkg -l | grep -q $programa; then # Só instala se já não estiver instalado
    apt install "$nome_do_programa" -y > /dev/null
   echo "[INSTALANDO] - $nome_do_programa"
  else
    echo "[JÁ EXISTE] - $nome_do_programa"
  fi
done

mysql_secure_installation 

# Scripts adicionais
chmod +x config-git.sh
chmod +x config-vscode.sh
chmod +x config-zsh.sh
chmod +x config-node.sh
chmod +x clonando-repos.sh

echo "OS PROGRAMAS ESTÃO PRONTOS UHUUUUUU!!!"



