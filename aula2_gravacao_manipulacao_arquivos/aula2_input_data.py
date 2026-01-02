nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# with open("input_data.txt", "w") as file:
#     file.write(f"Nome: {nome}\n")
#     file.write(f"Idade: {idade}")

with open("input_data.txt", "a") as file:
    file.write(f"\nNome: {nome}\n")
    file.write(f"Idade: {idade}")
