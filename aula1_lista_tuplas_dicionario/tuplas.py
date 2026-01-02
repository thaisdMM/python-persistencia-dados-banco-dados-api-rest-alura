# 2- TUPLAS
# Ordenada e imutável(uma vez declarada ela não dá para mudar)

tupla = 123, 345, "oi"
print(tupla)  # output: (123, 345, 'oi')
print(tupla[2])


lista = [1, "Python", 2]
tupla2 = tupla, lista
print(tupla2)  # output: ((123, 345, 'oi'), [1, 'Python', 2])

datas_filmes = "12/07/1999", "30/05/2002", "13/12/2005"
print(datas_filmes)  # output: ('12/07/1999', '30/05/2002', '13/12/2005')

# iteração
for i in tupla:
    print(i)
