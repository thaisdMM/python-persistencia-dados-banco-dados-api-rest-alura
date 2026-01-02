# 1- Escrever um arquivo com a função open() e sempre substitui o conteúdo

with open("dados.txt", "w") as file:
    file.write("Olá, mundo!")

# 2- Ler um arquivo com a função open()
with open("dados.txt", "r") as read_file:
    conteudo = read_file.read()
    print(conteudo)

# 3- Append - adicionar conteudo no final da arquivo
with open("dados.txt", "a") as append_file:
    append_file.write("\nAdicionando conteúdo ao final do arquivo.")

# 2- Ler um arquivo com a função open()
with open("dados.txt", "r") as read_file:
    conteudo = read_file.read()
    print(conteudo)

# 4- Manipulando arquivo csv
import csv

# 4.1- Escrever arquivo csv
with open("dados.csv", "w") as csv_file:
    escritor = csv.writer(csv_file)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["Miguel", 16])

# 4.2- Ler arquivo csv
with open("dados.csv", newline="") as read_csv_file:
    leitor = csv.reader(read_csv_file)
    for linha in leitor:
        print(linha)

# escrevi mais uma linha direto no arquivo

with open("dados.csv", newline="") as read_csv_file:
    leitor = csv.reader(read_csv_file)
    for linha in leitor:
        print(linha)

# # 5- Manipulando arquivos JSON
import json

# 5.1- Escrever aquivo json
dados = {"nome": "Ana", "idade": 32, "enderecos": ["a", "b"]}
with open("dados.json", "w") as json_file:
    json.dump(dados, json_file)

# 5.2- Ler arquivo json
with open("dados.json", "r") as read_json_file:
    dados_leitura = json.load(read_json_file)
    print(dados_leitura)

# LIMITAÇÃO DO USO DE ARQUIVOS

# Falta de estrutura relacional
# Dificuldade de busca
# Concorrência - pode ocorrer erros na escrita e na leitura
# Falta de segurança e integridadade
# Pouco escalável
