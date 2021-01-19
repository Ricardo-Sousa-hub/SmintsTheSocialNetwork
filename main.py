from Admin.Admin import MenuPrincipalAdmin
from User import MenuPrincipalUser
from Admin.GestaoUtilizadores import Gestao_de_utilizadores
import pickle

while True:

    try:
        users = pickle.load(open("users.dat", "rb"))
        palavrapasse = pickle.load(open("Password.dat", "rb"))
    except (OSError, IOError) as e:
        print("Não existem utilizadores, por favor crie um novo")

    try:
        opcao = int(input("Login - 1\n"
                          "Criar nova conta - 2\n"
                          "Terminar - 0\n"
                          "Opcao: "))
        if opcao == 1:
            utilizador = str(input("Utilizador: "))
            password = str(input("Password: "))

            if utilizador == "Admin" and password == "admin":
                MenuPrincipalAdmin()
            else:
                if utilizador in users:
                    userpos = users.index(utilizador)
                    passpos = palavrapasse.index(password)
                    if userpos == passpos:
                        print("Bem-vindo")
                        MenuPrincipalUser(utilizador)
                    else:
                        print("Palavra passe incorreta ou utilziador nao existente")
                else:
                    print("Nome de utilziador incorreto ou nao existente")
        elif opcao == 2:
            Gestao_de_utilizadores.inserirUtilizadores()

        elif opcao == 0:
            break
    except Exception:
        print("Digite um numero válido")

