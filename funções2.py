def voto():
    ano = int(input("Digite seu ano de nascimento: "))
    idade = 2025 - ano
    return idade

idade = voto()

print(f"Você tem {idade} anos")

if idade < 16:
    print("Voto NEGADO!")
elif idade >= 70 or (idade >= 16 and idade < 18):
    print("Voto OPCIONAL!")
else:
    print("Voto OBRIGATÓRIO!")

print("___________________________________")

