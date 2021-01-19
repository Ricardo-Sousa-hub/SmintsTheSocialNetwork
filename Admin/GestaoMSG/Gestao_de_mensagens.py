import pickle
from Utilizador import Utilizador
from Admin.GestaoUtilizadores import Gestao_de_utilizadores


def addpublicacao():
    Utilizador.criarpost("Admin")


def alterarpublicacao():
    Utilizador.alterarPublicacoes("Admin")


def eliminarpublicacao():
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    for i in range(len(publicacoes)):
        j = publicacoes[i]
        j = j.split(",")
        id = j[1]
        print(j[3], "\nIndex de publicacao: ", i)
        print("=" * 30)
        for y in range(len(comentarios)):
            aux = comentarios[y]
            aux = aux.split(",")
            if (aux[1] == id) and (aux[2] == "c"):
                print("     ", aux[3], "\n      Index de comentario:", y)
                print("-" * 30)

    remove = input("Digite o index da publicacao que deseja remover, se desejar sair, digite sair: ")
    if remove == "sair":
        return 0
    else:
        remove = int(remove)
        print(publicacoes[remove])
        aux = publicacoes[remove]
        aux = aux.split(",")

        user = aux[0]
        id = aux[1]

        publicacoes.pop(remove)
        listapos = []

        for i in range(len(comentarios)):
            j = comentarios[i]
            j = j.split(",")
            if j[0] == user and j[1] == id:
                listapos.append(comentarios[i])
            for y in listapos:
                comentarios.remove(y)

        print("Publicacao removida com sucesso.")

        pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
        pickle.dump(comentarios, open("comentarios.dat", "wb"))


def gestaodemensagens():
    Utilizador.verpublicacoes()


def pesquisafiltrada():
    Gestao_de_utilizadores.pesquisarporUtilizador()
