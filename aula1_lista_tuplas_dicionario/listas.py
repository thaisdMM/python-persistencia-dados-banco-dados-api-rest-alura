# 1- LISTAS
# ordenadas e mutável

lista = []
print(lista)
lista = [1, "Python", 2]
print(lista)  # output: [1, 'Python', 2]
print(lista[0])  # output: 1
print(lista[2])  # output: 2
# mutável: alterando um elemento:
lista[0] = "alterado"
print(lista)  # output: ['alterado', 'Python', 2]

# inserindo elementos na lista

# 1. append
lista.append("novo elemento")
print(lista)  # output: ['alterado', 'Python', 2, 'novo elemento']

# 2. insert
lista.insert(0, "posicão 0: insert")
print(lista)  # output: ['posicão 0: insert', 'alterado', 'Python', 2, 'novo elemento']

filmes = ["Um lugar chamado Notting Hill", "Harry Potter", "Crepúsculo"]
print(filmes)

# iterador
for i in lista:
    print(i)
