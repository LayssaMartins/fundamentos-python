while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    opcao = 0  # Inicializa a opção para entrar no loop
    while opcao != 5:
        print("Ok! Agora veja as opções")
        print("[1] Somar")
        print("[2] Multiplicar")
        print("[3] Maior")
        print("[4] Novos números")
        print("[5] Sair do programa")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print(f"A soma de {num1} + {num2} = {num1 + num2}")
        elif opcao == 2:
            print(f"A multiplicação de {num1} * {num2} = {num1 * num2}")
        elif opcao == 3:
            if num1 > num2:
                print(f"O maior número é {num1}")
            elif num2 > num1:
                print(f"O maior número é {num2}")
            else:
                print("Os dois números são iguais.")
        elif opcao == 4:
            print("Informe os números novamente...\n")
            break  # Sai do loop interno para reiniciar o processo
        elif opcao == 5:
            print("Saindo do programa...")
            exit()  # Encerra o programa imediatamente
        else:
            print("Opção inválida! Tente novamente.")
