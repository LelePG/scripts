#!/bin/bash
## Adicionar o caminho pra esse arquivo como alias no arquivo de src do terminal
# alias nome='CAMINHO' e depois disso source no arquivo que foi editado pro alias ficar disponível.

LINKS=(

)

for link in "${LINKS[@]}"; do
    brave --new-tab "$link" 2>/dev/null # no momento estou usando o brave, mas se você estiver usando outro navegador, altere o navegador nesse comando.
done
