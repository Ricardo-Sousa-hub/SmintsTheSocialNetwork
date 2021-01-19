def Menu(titulo, opcoes, nop):
    print()
    print(titulo)
    print()
    for i in range(nop):
        print(i + 1, "-", opcoes[i])
        print("-" * 30)
    print("0 - Terminar")
    while True:
        try:
            op = int(input("Opcao? "))
        except ValueError:
            print("Digite um numero inteiro!")
            continue
        if op >= 0 and op <= nop:
            break
        else:
            print("O valor deve estar entre 1 e 4")

    return op
