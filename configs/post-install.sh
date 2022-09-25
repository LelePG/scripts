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


#Comentários de programas que não vou instalar
#org.octave.Octave
#net.sonic_pi.SonicPi
#com.stremio.Stremio
#org.supertuxproject.SuperTux
#org.desmume.DeSmuME
#io.mgba.mGBA
PROGRAMAS_FLATPAK=(
cc.arduino.arduinoide
com.getpostman.Postman
nl.hjdskes.gcolor3
org.flameshot.Flameshot
org.audacityteam.Audacity
org.videolan.VLC
org.kde.kdenlive
com.obsproject.Studio
org.deluge_torrent.deluge
com.spotify.Client
org.gnome.gitlab.somas.Apostrophe
org.gnome.Extensions
io.github.mpobaschnig.Vaults
net.supertuxkart.SuperTuxKart
com.stepmania.StepMania
com.discordapp.Discord
org.telegram.desktop
org.kicad.KiCad
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

#Instalação dos programas snap
for programa in ${PROGRAMAS_SNAP[@]}; do
  if ! snap list | grep -q $programa; then # Só instala se já não estiver instalado
    sudo snap install "$programa"  2>> log.txt
    echo "[INSTALANDO] - $programa"
  else
    echo "[JÁ EXISTE] - $programa"
  fi
done

#mysql_secure_installation 

# Scripts adicionais
chmod +x config-git.sh
chmod +x config-vscode.sh
chmod +x config-zsh.sh
chmod +x config-node.sh
chmod +x clonando-repos.sh

echo "OS PROGRAMAS ESTÃO PRONTOS UHUUUUUU!!!"



