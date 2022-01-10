#!/bin/bash

# https://github.com/nodesource/distributions/blob/master/README.md#debinstall -> lugar onde achar a instalação do node.
curl -fsSL https://deb.nodesource.com/setup_17.x | sudo -E bash -
sudo apt-get install -y nodejs

npm install -g @vue/cli
npm install -g @angular/cli
npm install -g typescript
npm install -g gulp-cli




