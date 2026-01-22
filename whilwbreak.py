n = -1
ndigitados = 0
s = 0
while n!= 999:
    n = int(input("Digite um valor"))
    if n == 999:
        break
    ndigitados += 1
    s += n

print("Você digitou {} números:" . format(ndigitados))
print("E a soma dos números foi:{}" .format(s))
print('Fim')

print("____________________________________")

while True:
    num = int(input("Digite um número para ver a tabuada (negativo para sair): "))
    if num < 0:
        print("Programa encerrado.")
        break
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-")


    