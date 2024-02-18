#!/bin/bash

# Define o caminho da pasta principal
main_folder="exemplo"

# Define o caminho da pasta de destino
destination_folder="content"

# Loop através das pastas na pasta principal
for folder in "$main_folder"/*/; do
    # Obtém o nome da pasta atual
    folder_name=$(basename "$folder")
    
    # Verifica se existe um arquivo README.md na pasta atual
    if [ -f "$folder/Readme.md" ]; then
        # Cria uma pasta na pasta de destino com o mesmo nome da pasta atual
        mkdir -p "$destination_folder/$folder_name"      
        # Copia o arquivo README.md para a pasta de destino
        hugo new "$destination_folder/$folder_name/index.md"
        cat "$folder/Readme.md" >> "$destination_folder/$folder_name/index.md"
        # Se tiver a pasta imagem, copiar essa pasta também        
        if [ -d "$folder/img" ]; then
            cp -R "$folder/img" "$destination_folder/$folder_name"
        fi
        
        echo "Pasta $folder_name copiada com sucesso."
    else
        echo "A pasta $folder_name não contém um arquivo README.md. Ignorando."
    fi
done

echo "Processo concluído."
