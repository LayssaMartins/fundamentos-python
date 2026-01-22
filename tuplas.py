# Criando a tupla com os números por extenso
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

# Pedindo um número ao usuário
numero = int(input("Digite um número entre 0 e 20: "))

# Verificando se o número está dentro do intervalo permitido
if 0 <= numero <= 20:
    print(f"Você digitou o número {numeros[numero]}.")
else:
    print("Número inválido! Digite um valor entre 0 e 20.")

print("____________________________________________________")

times = ("flamengo", "Atletico Mineiro", "Palmeiras", "Grêmio", "São Paulo","Fluminense", "Internacional", "Corinthians", "Athletico Paranaense", "Santos", "Ceará", "Bahia", "Botafogo", "Fortaleza", "Vasco da Gama", "América Mineiro", "Goiás", "Red Bull Bragantino", "Cuiabá", "Coritiba" )
print( f"Os cinco primeiros colocados são{times[0:5]}")
print (f"Os últimos colocados na tabela são{times[-4:]}")
print("em ordem alfabética fica:")
print(sorted(times))

nome = str(input("Digite o nome de um time, para saber em que posição ele está: "))
posição = times.index(nome)+1
print(f"Está na posição {posição}")

print("____________________________________________________")

import random
# Gerando cinco números aleatórios e armazenando em uma tupla
numeros = tuple(random.randint(1, 100) for _ in range(5))
# Mostrando os números gerados
print("Números sorteados:", numeros)
# Exibindo o menor e o maior valor
print("Menor número:", min(numeros))
print("Maior número:", max(numeros))




