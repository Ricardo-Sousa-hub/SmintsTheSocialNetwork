from Admin.Admin import MenuPrincipalAdmin
from User import MenuPrincipalUser
from Admin.GestaoUtilizadores import Gestao_de_utilizadores
import pickle
import os

clear = lambda: os.system('cls')

while True:
    try:
        clear()
        users = pickle.load(open("users.dat", "rb"))
        palavrapasse = pickle.load(open("Password.dat", "rb"))

        opcao = input("Login - 1\n"
                      "Criar nova conta - 2\n"
                      "Terminar - 0\n"
                      "Opcao: ")

        while opcao.isdigit() == False or int(opcao) < 0 or int(opcao) > 2:
            print("Digite um numero valido")
            opcao = input("Login - 1\n"
                          "Criar nova conta - 2\n"
                          "Terminar - 0\n"
                          "Opcao: ")

        if int(opcao) == 1:
            clear()
            users = pickle.load(open("users.dat", "rb"))
            palavrapasse = pickle.load(open("Password.dat", "rb"))
            utilizador = str(input("Utilizador: "))
            password = str(input("Password: "))

            if utilizador == "Admin" and password == "admin":
                MenuPrincipalAdmin()
            else:
                if utilizador in users:
                    # noinspection PyBroadException
                    userpos = users.index(utilizador)
                    if password in palavrapasse:
                        passpos = palavrapasse.index(password)
                        if userpos == passpos:
                            print("Bem-vindo")
                            cliente = utilizador
                            MenuPrincipalUser(cliente)
                        else:
                            print("Nome de utilziador/palavra passe incorreto(a) ou nao existente")
                    else:
                        print("Palavra passe incorreta")
                else:
                    print("Utilizador não se encontra registado")
        elif int(opcao) == 2:
            Gestao_de_utilizadores.inserirUtilizadores()

        elif int(opcao) == 0:
            break

    except (OSError, IOError):
        clear()
        print("Não existem utilizadores, por favor crie um novo")
        opcao = input("Login - 1\n"
                      "Criar nova conta - 2\n"
                      "Terminar - 0\n"
                      "Opcao: ")

        while opcao.isdigit() == False or int(opcao) < 0 or int(opcao) > 2:
            print("Digite um numero valido")
            opcao = input("Login - 1\n"
                          "Criar nova conta - 2\n"
                          "Terminar - 0\n"
                          "Opcao: ")

        if int(opcao) == 1:
            utilizador = str(input("Utilizador: "))
            password = str(input("Password: "))

            if utilizador == "Admin" and password == "admin":
                MenuPrincipalAdmin()
            else:
                print("Por favor crie um novo utilziador.")
        elif int(opcao) == 2:
            clear()
            Gestao_de_utilizadores.inserirUtilizadores()

        elif int(opcao) == 0:
            break