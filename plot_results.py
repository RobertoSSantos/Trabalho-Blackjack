import matplotlib.pyplot as plt

# Lista de caminhos dos arquivos
file_names = ["results_simple.txt", "results_double.txt", "results_master.txt"]

# Loop para processar cada arquivo e plotar um gráfico separado para cada um
for file_name in file_names:
    # Listas para armazenar dados do arquivo atual
    executions = []
    wins = []
    loses = []
    expected_scores = []

    # Leitura do arquivo
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Processamento das linhas do arquivo
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("Execução"):
            # Obtém o número da execução
            execution_number = int(line.split()[-1])
            executions.append(execution_number)

            # Extrai dados de Wins, lose e Player expected score
            wins_line = lines[i + 1].strip().split(": ")[1].split(",")[0]
            loses_line = lines[i + 1].strip().split(": ")[2]
            expected_score_line = float(lines[i + 2].strip().split()[-1])

            wins.append(int(wins_line))
            loses.append(int(loses_line))
            expected_scores.append(expected_score_line)

    # Criar gráfico
    plt.figure(figsize=(10, 6))  # Tamanho da figura

    # Plotar os dados do arquivo atual
    plt.plot(executions, wins, label='Wins')
    plt.plot(executions, loses, label='Lose')
    plt.plot(executions, expected_scores, label='Expected Score')

    # Configurar rótulos e título do gráfico
    plt.xlabel('Execução')
    plt.ylabel('Resultados')
    plt.title(f'{file_name} - Wins, Lose, and Expected Score Over Executions')

    # Adicionar legenda
    plt.legend()

    # Mostrar o gráfico
    plt.show()
