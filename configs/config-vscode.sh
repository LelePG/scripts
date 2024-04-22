#!/bin/bash

# Extensões que eu costumo usar
EXTENSOES=(
mhutchie.git-graph
MS-vsliveshare.vsliveshare
ritwickdey.LiveServer
formulahendry.code-runner
usernamehw.errorlens
rangav.vscode-thunder-client
esbenp.prettier-vscode
BeardedBear.beardedtheme
firsttris.vscode-jest-runner
bradlc.vscode-tailwindcss
oderwat.indent-rainbow
GitHub.copilot
GitHub.copilot-chat
johnpapa.vscode-peacock
)


for extensao in ${EXTENSOES[@]}; do
    code --install-extension "$extensao"
done


