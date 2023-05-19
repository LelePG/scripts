#!bin/bash
echo "Não coloque extensões nos nomes dos arquivos!!"
read -p "Arquivo de entrada: " ENTRADA
read -p "Arquivo de saida: " SAIDA

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \-dNOPAUSE -dQUIET -dBATCH -sOutputFile="$PWD/$SAIDA.pdf" "$PWD/$ENTRADA.pdf"
