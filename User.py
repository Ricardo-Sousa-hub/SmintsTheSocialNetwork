from Utilizador import Utilizador
from Menus import Menu
from Admin.GestaoUtilizadores import Gestao_de_utilizadores


def MenuPrincipalUser(utilizador):
    while True:
        op = Menu.Menu("Gestão de rede social",
                       ["Criar post", "Ver publicacoes", "Comentar publicacoes", "Alterar publicacoes",
                        "Remover publicacoes", "Alterar comentarios", "Remover comentarios", "Pesquisar por utilziador",
                        "Ver perfil", "Definicoes de conta"], 10)
        if op == 1:
            Utilizador.criarpost(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.criarpost(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 2:
            Utilizador.verpublicacoes()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.verpublicacoes()
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 3:
            Utilizador.comentarPublicacoes(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.comentarPublicacoes(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 4:
            Utilizador.alterarPublicacoes(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.alterarPublicacoes(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 5:
            Utilizador.removerPublicacoes(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.removerPublicacoes(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 6:
            Utilizador.alterarComentarios(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.alterarComentarios(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 7:
            Utilizador.removerComentarios(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.removerComentarios(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 8:
            Gestao_de_utilizadores.pesquisarporUtilizador()
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Gestao_de_utilizadores.pesquisarporUtilizador()
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 9:
            Utilizador.verPerfil(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.verPerfil(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 10:
            Utilizador.definicoesdeconta(utilizador)
            usrop = input("Deseja repetir o processo? s/n: ")
            while usrop == "s":
                Utilizador.definicoesdeconta(utilizador)
                usrop = input("Deseja repetir o processo? s/n: ")
            input("Prima qualquer tecla para continuar")
        elif op == 0:
            break
