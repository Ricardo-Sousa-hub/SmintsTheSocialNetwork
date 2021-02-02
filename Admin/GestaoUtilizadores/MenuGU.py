from Menus import Menu
from Admin.GestaoUtilizadores import Gestao_de_utilizadores


def MenuGu():
    while True:

        op = Menu.Menu("Gestão de utilizadores",
                       ["Inserir", "Alterar", "Eliminar", "Listar todos", "Pesquisa por nome", "Estatistica"], 6)

        if op == 1:
            Gestao_de_utilizadores.inserirUtilizadores()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Gestao_de_utilizadores.inserirUtilizadores()
                usrop = input("Deseja repetir o processo? s/n: ")

            input("Prima qualquer tecla para continuar")

        elif op == 2:
            Gestao_de_utilizadores.alterarUtilizador()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Gestao_de_utilizadores.alterarUtilizador()
                usrop = input("Deseja repetir o processo? s/n: ")

            input("Prima qualquer tecla para continuar")

        elif op == 3:
            Gestao_de_utilizadores.eliminarUtilizador()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Gestao_de_utilizadores.eliminarUtilizador()
                usrop = input("Deseja repetir o processo? s/n: ")

            input("Prima qualquer tecla para continuar")

        elif op == 4:
            Gestao_de_utilizadores.listarUtilizadores()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Gestao_de_utilizadores.listarUtilizadores()
                usrop = input("Deseja repetir o processo? s/n: ")

            input("Prima qualquer tecla para continuar")

        elif op == 5:
            Gestao_de_utilizadores.pesquisarporUtilizador()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Gestao_de_utilizadores.pesquisarporUtilizador()
                usrop = input("Deseja repetir o processo? s/n: ")

            input("Prima qualquer tecla para continuar")

        elif op == 6:
            Gestao_de_utilizadores.estatistica()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Gestao_de_utilizadores.estatistica()
                usrop = input("Deseja repetir o processo? s/n: ")

            input("Prima qualquer tecla para continuar")

        elif op == 0:
            break
