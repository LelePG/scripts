#!/bin/bash

# Extensões que eu costumo usar
EXTENSOES=(
eamodio.gitlens
mhutchie.git-graph
pnp.polacode
PKief.material-icon-theme
MS-vsliveshare.vsliveshare
ritwickdey.LiveServer
alexandernanberg.horizon-theme-vscode
formulahendry.code-runner
usernamehw.errorlens
rangav.vscode-thunder-client
platformio.platformio-ide
esbenp.prettier-vscode
Vue.volar
BeardedBear.beardedtheme
Syler.sass-indented
bradlc.vscode-tailwindcss
oderwat.indent-rainbow
)


for extensao in ${EXTENSOES[@]}; do
    code --install-extension "$extensao"
done


