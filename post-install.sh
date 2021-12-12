#!/bin/bash

# testa se o flatpak está instalado
if ! [ -x "$(command -v flatpak)" ]; then
  echo 'Instale o Flatpack.' >&2
  exit 1
fi
echo "Iniciando a instalação..."


# Jogos
flatpak install flathub org.supertuxproject.SuperTux
flatpak install flathub net.supertuxkart.SuperTuxKart

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

#Dev
flatpak install flathub org.octave.Octave
flatpak install flathub net.sonic_pi.SonicPi
flatpak install flathub cc.arduino.arduinoide
flatpak install flathub com.visualstudio.code
flatpak install flathub com.getpostman.Postman

#Internet
flatpak install flathub org.chromium.Chromium
flatpak install flathub org.deluge_torrent.deluge

# Outros
flatpak install flathub com.spotify.Client
flatpak install flathub com.github.phase1geo.minder
flatpak install flathub org.gnome.gitlab.somas.Apostrophe
flatpak install flathub com.github.johnfactotum.Foliate
flatpak install flathub nz.mega.MEGAsync

