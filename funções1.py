b = int(input("Digite o tamanho da base:"))
h = int(input("Digite o tamanho da altura:"))

def área(b,h):
    a = b * h
    print(a)

print(f"A área de um terreno {b} x {h} é de")
área(b,h)

print("________________________________")

def escreva (msg):
    tam = len(msg)
    print("~" * tam)
    print(msg)
    print("~" * tam)

escreva("Layssa vai ser uma ótima desenvolvedora :)")

print("________________________________")

