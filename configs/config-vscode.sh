#!/bin/bash

# Extensões que eu costumo usar
EXTENSOES=(
mhutchie.git-graph
MS-vsliveshare.vsliveshare
ritwickdey.LiveServer
alexandernanberg.horizon-theme-vscode
formulahendry.code-runner
usernamehw.errorlens
rangav.vscode-thunder-client
esbenp.prettier-vscode
BeardedBear.beardedtheme
firsttris.vscode-jest-runner
bradlc.vscode-tailwindcss
oderwat.indent-rainbow
mongodb.mongodb-vscode
)


for extensao in ${EXTENSOES[@]}; do
    code --install-extension "$extensao"
done


