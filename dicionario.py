situação = {}
nome = str(input("Digite seu nome:"))
média = int(input("Digite sua média:"))
if média > 7:
    status = "Você está aprovado!"
elif média == 7:
    status = "Você está na média"
else: 
    status = "Você está reprovado"

situação["Nome"] = nome
situação["Média"] = média
situação["Situação"] = status 

print(situação)

print("_________________________")

