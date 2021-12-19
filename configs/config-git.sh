read -p "Nome: " NOME
read -p "E-mail: " EMAIL

#sudo apt-get install git

# Configuração de credenciais
git config --global user.name "$NOME"
git config --global user.email $EMAIL

# Chave SSH
ssh-keygen -t ed25519 -C "$EMAIL"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

echo "Copie a chave e cole na plataforma correspondente"

cat ~/.ssh/id_ed25519.pub

