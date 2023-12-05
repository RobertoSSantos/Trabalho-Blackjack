#!/bin/bash

# Caminho do arquivo
file_name="results_master.txt"

# Comando a ser executado
command="python3 blackjack_game.py 100 0.8 0.5 0.5 0.1"

# Número de vezes para executar o comando
num_executions=100

# Limpar o conteúdo do arquivo
> "$file_name"

# Loop para executar o comando e salvar a saída no arquivo
for ((i=1; i<=$num_executions; i++)); do
    echo "Execução $i" >> "$file_name"
    $command
    echo -e "\n----------------------------------------\n" >> "$file_name"
done

echo "Comando executado $num_executions vezes. Saída registrada em $file_name"
