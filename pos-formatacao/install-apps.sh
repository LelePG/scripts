#!/bin/bash

# testa se o flatpak está instalado
if ! [ -x "$(command -v flatpak)" ]; then
  echo 'Instale o Flatpack.' >&2
  exit 1
fi

# testa se o snap está instalado
if ! [ -x "$(command -v snap)" ]; then
  echo 'Instale o snap.' >&2
  exit 1
fi

# testa se o apt está instalado
if ! [ -x "$(command -v apt-get)" ]; then
  echo 'Instale o apt.' >&2
  exit 1
fi


function notificacao(){
  echo $*
  notify-send " $*"
}

notificacao "Iniciando..."


PROGRAMAS_FLATPAK=(
cc.arduino.IDE2
nl.hjdskes.gcolor3
org.flameshot.Flameshot
org.kde.kdenlive
com.obsproject.Studio
org.deluge_torrent.deluge
net.supertuxkart.SuperTuxKart
org.supertuxproject.SuperTux
com.stepmania.StepMania
com.heroicgameslauncher.hgl
org.kicad.KiCad
md.obsidian.Obsidian
com.github.k4zmu2a.spacecadetpinball
org.chromium.Chromium
org.gnome.Boxes
io.github.flattool.Warehouse
com.github.tchx84.Flatseal
com.stremio.Stremio
dev.bragefuglseth.Keypunch
com.github.johnfactotum.Foliate
net.codelogistics.webapps
io.github.nate_xyz.Paleta
org.inkscape.Inkscape
com.github.unrud.VideoDownloader
org.mozilla.firefox
org.gnome.Mines
org.wesnoth.Wesnoth
org.gnome.Boxesflatpak 
io.github.flattool.Ignition
org.gnome.design.Lorem
io.github.mpobaschnig.Vaults
app.zen_browser.zen
com.opera.Opera
io.beekeeperstudio.Studio
org.thonny.Thonny
org.gnome.Extensions
#com.discordapp.Discord
)

PROGRAMAS_APT=(
gnome-tweak-tool
peek
gparted
traceroute
unrar
lm-sensors
net-tools
git
zsh
)

PROGRAMAS_SNAP=(
mysql-workbench-community
guvcview 
organize-my-files
nordvpn
vivaldi
spotify
vlc
)

PROGRAMAS_APPIMAGE=(
  'https://github.com/justinforlenza/keylight-control/releases/'
  'https://responsively.app/'
  'https://github.com/Figma-Linux/figma-linux/releases'
)

PROGRAMAS_DEB=(
  'https://code.visualstudio.com/download'
  'https://docs.docker.com/desktop/setup/install/linux/'
)

echo "Solicitando credenciais de administrador para instalação dos programas..."
sudo -v

# Mantém o sudo ativo
(
  while true; do
    sudo -v
    sleep 60  
    kill -0 $$ 2>/dev/null || exit
  done
) & SUDO_KEEPER_PID=$!

# Garante que o sudo será encerrado ao sair do script
trap 'kill -9 $SUDO_KEEPER_PID 2>/dev/null' EXIT


#Instalação dos programas flatpak
notificacao "Instalando programas Flatpak..."
for programa in ${PROGRAMAS_FLATPAK[@]}; do
  if flatpak list | grep -q $programa; then
    echo "[JÁ EXISTE] - $programa"
  else
    echo "[INSTALANDO] - $programa"
    flatpak install flathub "$programa" -y 2>> log.txt
  fi
done
notificacao "Programas Flatpak instalados."

#Instalação dos programas apt
notificacao "Instalando programas apt..."
for programa in ${PROGRAMAS_APT[@]}; do
  if dpkg -l | grep -q $programa; then 
    echo "[JÁ EXISTE] - $programa"
  else
    echo "[INSTALANDO] - $programa"
    sudo apt-get install "$programa"  2>> log.txt
  fi
done
notificacao "Programas apt instalados"

#Instalação dos programas snap
notificacao "Instalando programas snap..."
for programa in ${PROGRAMAS_SNAP[@]}; do
  if snap list | grep -q $programa; then 
    echo "[JÁ EXISTE] - $programa"
  else
    echo "[INSTALANDO] - $programa"
    sudo snap install "$programa"  2>> log.txt
  fi
done
notificacao "Programas snap instalados."

# Instala o Volta e Node
notificacao "Instalando Volta e Node.JS..."
curl https://get.volta.sh | bash
volta install node
notificacao "Volta e Node.JS instalados."

# Abre os programas AppImage no navegador
notificacao "Abrindo programas AppImage no navegador..."
for programa in ${PROGRAMAS_APPIMAGE[@]}; do
  vivaldi --new-tab "$programa" 2>> log.txt
done
notificacao "Programas AppImage abertos no navegador."

# Abre os programas DEB no navegador
notificacao "Abrindo programas DEB no navegador..."
for programa in ${PROGRAMAS_DEB[@]}; do
  vivaldi --new-tab "$programa" 2>> log.txt
done
notificacao "Programas DEB abertos no navegador."

notificacao "Faça a instalação manual dos programas AppImage e DEB."

# Menu de finalização
echo ""
echo "================================================="
echo "          INSTALAÇÃO DE APLICATIVOS CONCLUÍDA    "
echo "================================================="
echo ""

echo "Selecione uma opção:"
opcoes=("Encerrar programa" "Executar script de pós-instalação")

select opcao in "${opcoes[@]}"
do
    case $opcao in
        "Encerrar programa")
            notificacao "Instalação finalizada com sucesso!"
            break
            ;;
        "Executar script de pós-instalação")
            notificacao "Iniciando script de pós-instalação..."
            
            POST_INSTALL_SCRIPT="$(dirname "$0")/post-install.sh"
            
            if [ -f "$POST_INSTALL_SCRIPT" ]; then
                chmod +x "$POST_INSTALL_SCRIPT"
                bash "$POST_INSTALL_SCRIPT"
            else
                notificacao "Erro: Script de pós-instalação não encontrado!"
            fi
            break
            ;;
        *) 
            echo "Opção inválida. Tente novamente."
            ;;
    esac
done

exit 0
