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

# Instalações via flathub
# Dev
flatpak install flathub org.octave.Octave
flatpak install flathub net.sonic_pi.SonicPi
flatpak install flathub cc.arduino.arduinoide
flatpak install flathub com.visualstudio.code
flatpak install flathub com.getpostman.Postman

# Social
flatpak install flathub com.discordapp.Discord
flatpak install flathub org.telegram.desktop

# Graficos
flatpak install flathub nl.hjdskes.gcolor3
flatpak install flathub org.flameshot.Flameshot
flatpak install flathub org.inkscape.Inkscape
flatpak install flathub net.scribus.Scribus

# Video e Audio
flatpak install flathub org.audacityteam.Audacity
flatpak install flathub org.kde.kdenlive
flatpak install flathub com.obsproject.Studio
flatpak install flathub com.uploadedlobster.peek

#Internet
flatpak install flathub org.chromium.Chromium
flatpak install flathub org.deluge_torrent.deluge

# Outros
flatpak install flathub com.spotify.Client
flatpak install flathub com.github.phase1geo.minder
flatpak install flathub org.gnome.gitlab.somas.Apostrophe
flatpak install flathub com.github.johnfactotum.Foliate
flatpak install flathub nz.mega.MEGAsync
flatpak install flathub com.github.robertsanseries.ciano
flatpak install flathub org.gnome.Extensions

# Jogos
flatpak install flathub org.supertuxproject.SuperTux
flatpak install flathub net.supertuxkart.SuperTuxKart
flatpak install flathub org.desmume.DeSmuME
flatpak install flathub io.mgba.mGBA

# Instalações via apt
sudo apt-get update
sudo apt-get install nodejs
npm install -g @vue/cli
sudo apt-get install mysql-server
sudo apt-get install gparted
sudo apt-get install gnome-tweak-tool

# Instalações snap
sudo snap install zenkit
sudo snap install brave
sudo snap install onlyoffice-desktopeditors
sudo snap install screenkey --beta
sudo snap install mysql-workbench-community

# Scripts adicionais
chmod +x config-git.sh
chmod +x config-vscode.sh
chmod +x config-zsh.sh
./config-git
./config-vscode
./config-zsh

echo "TÁ TUDO PRONTO. UHUUUU"




