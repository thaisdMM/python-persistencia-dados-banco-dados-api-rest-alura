# 3 - DICIONARIOS
# Não ordenado, Mutável, chave: valor

telefones = {"joao": 911238940, "leo": 9243442233}
print(telefones)
print(telefones["leo"])  # output: 9243442233
# adcionando novo valor
telefones["maria"] = 9877777733
print(telefones)  # output: {'joao': 911238940, 'leo': 9243442233, 'maria': 9877777733}

# 1.
filmes_dict = {
    "Um lugar chamado Notting Hill": "12/07/1999",
    "Harry Potter": "30/05/2002",
    "Crepúsculo": "13/12/2005",
}
print(filmes_dict)

# 2.
filmes = ["Um lugar chamado Notting Hill", "Harry Potter", "Crepúsculo"]
datas_filmes = "12/07/1999", "30/05/2002", "13/12/2005"
filmes_dict2 = {}

filmes_dict2[filmes[0]] = datas_filmes[0]
filmes_dict2[filmes[1]] = datas_filmes[1]
filmes_dict2[filmes[2]] = datas_filmes[2]
print(filmes_dict2)

# iterador

for key, value in filmes_dict.items():
    print(key, value)

# 3. iteração sem o zip
filmes_dict4 = {}
for i in range(len(filmes)):
    filmes_dict4[filmes[i]] = datas_filmes[i]
    # print(i)
    # print(filmes_dict4)
print()
print(filmes_dict4)


# usando o zip()
print()
filmes_dict3 = dict(zip(filmes, datas_filmes))
print(filmes_dict3)

duracao = ["2h 4min", "2h 32min", "2h 2min"]

# adicionando uma lista como valor
filmes_dict4 = {}
for i in range(len(filmes)):
    filmes_dict4[filmes[i]] = [datas_filmes[i], duracao[i]]
    # print(i)
    # print(filmes_dict4)
print()
print(filmes_dict4)
nomes_filmes = list(filmes_dict4.keys())

print(f"Duração do filme {nomes_filmes[1]} = {filmes_dict4['Harry Potter'][1]}\n")


# imprimindo chave e valor
for key, value in filmes_dict4.items():
    print(
        f"{key:<30} | data que foi assistido: {value[0]} | duração do filme: {value[1]}"
    )
