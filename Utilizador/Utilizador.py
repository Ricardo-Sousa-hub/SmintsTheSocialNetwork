import pickle
import random


def criarpost(utilizador):
    try:
        users = pickle.load(open("users.dat", "rb"))
        publicacoes = pickle.load(open("publicacoes.dat", "rb"))
        comentarios = pickle.load(open("comentarios.dat", "rb"))
        ids = pickle.load(open("ids.dat", "rb"))
        while True:
            publicacao = input("Publicacao? ")
            if publicacao == "sair":
                break
            else:
                x = random.randint(0, 1000)
                while x in ids:
                    x = random.randint(0, 1000)

                ids.append(x)
                publicacoes.append(utilizador + "," + str(x) + "," + "pub" + "," + publicacao)
                while True:
                    comentario = input("Comentario? ")
                    if comentario == "sair":
                        break
                    else:
                        comentarios.append(utilizador + "," + str(x) + "," + "c" + "," + comentario)

                pickle.dump(users, open("users.dat", "wb"))
                pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
                pickle.dump(comentarios, open("comentarios.dat", "wb"))

    except (IOError, OSError):
        listapublicacoes = []
        listacoments = []
        ids = []
        while True:
            publicacao = input("Publicacao? ")
            if publicacao == "sair":
                break
            else:
                x = random.randint(0, 1000)
                while x in ids:
                    x = random.randint(0, 1000)
                ids.append(x)
                listapublicacoes.append(utilizador + "," + str(x) + "," + "pub" + "," + publicacao)
                while True:
                    comentario = input("Comentario? ")
                    if comentario == "sair":
                        break
                    else:
                        listacoments.append(utilizador + "," + str(x) + "," + "c" + "," + comentario)

        pickle.dump(listapublicacoes, open("publicacoes.dat", "wb"))
        pickle.dump(listacoments, open("comentarios.dat", "wb"))
        pickle.dump(ids, open("ids.dat", "wb"))


def verpublicacoes():
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))

    for i in range(len(publicacoes)):
        j = publicacoes[-i-1]
        j = j.split(",")
        print("Autor:", j[0])
        print(j[3], "\nIndex de publicacao: ", i)
        print("=" * 30)
        for y in range(len(comentarios)):
            aux = comentarios[-y-1]
            aux = aux.split(",")
            if (aux[1] == j[1]) and (aux[2] == "c"):
                print("Comentario de:", aux[0])
                print("     ", aux[3], "\nIndex de comentario: ", y)
                print("-" * 30)


def comentarPublicacoes(utilizador):
    verpublicacoes()
    selecao = int(input("Digite o index da publicacao que quer comentar: "))
    comentario = input("Digite o comentario, se desejar sair digite sair? ")

    if comentario == "sair":
        return 0
    else:
        publicacoes = pickle.load(open("publicacoes.dat", "rb"))
        comentarios = pickle.load(open("comentarios.dat", "rb"))
        x = publicacoes[-selecao-1]
        x = x.split(",")
        comentarios.append(utilizador + "," + str(x[1]) + "," + "c" + "," + comentario)
        pickle.dump(comentarios, open("comentarios.dat", "wb"))


def alterarPublicacoes(utilizador):
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    verpublicacoes()
    indexpub = int(input("Digite o index da publicacao que pretende alterar: "))

    aux = publicacoes[-indexpub-1]
    aux = aux.split(",")
    if aux[0] == utilizador:
        alterarpub = input("Digite a nova publicacao, se desejar sair, digite ssair: ")
        if alterarpub == "sair":
            return 0
        else:
            publicacoes.pop(-indexpub-1)
            publicacoes.insert(-indexpub-1, (utilizador + "," + str(aux[1]) + "," + "pub" + "," + alterarpub))
            pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
    else:
        print("Nao pode modificar esta publicacao pois nao lhe pertence.")


def removerPublicacoes(utilizador):
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    for i in range(len(publicacoes)):
        j = publicacoes[-i-1]
        j = j.split(",")
        if j[0] == utilizador:
            print(j[3], "\nIndex de publicacao: ", i)
            print("=" * 30)
            for y in range(len(comentarios)):
                aux = comentarios[-y-1]
                aux = aux.split(",")
                if (aux[0] == utilizador) and (aux[1] == j[1]) and (aux[2] == "c"):
                    print("     ", aux[3], "\n      Index de comentario:", y)
                    print("-" * 30)

    remove = input("Digite o index da publicacao que deseja remover, se desejar sair, digite sair: ")
    if remove == "sair":
        return 0
    else:
        remove = int(remove)
        autor = publicacoes[-remove-1].split(",")
        if autor[0] == utilizador:
            print(publicacoes[-remove-1])
            aux = publicacoes[-remove-1]
            aux = aux.split(",")

            user = utilizador

            publicacoes.pop(-remove-1)
            listapos = []

            for i in range(len(comentarios)):
                j = comentarios[-i-1]
                j = j.split(",")
                if j[0] == user and j[1] == aux[1]:
                    listapos.append(comentarios[-i-1])

            for i in listapos:
                comentarios.remove(i)
        else:
            print("Nao pode remover este comentario, pois nao lhe pertence.")

        print("Publicacao removida com sucesso.")

        pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
        pickle.dump(comentarios, open("comentarios.dat", "wb"))


def alterarComentarios(utilizador):
    verpublicacoes()
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    alterar = int(input("Index de comentario? "))

    id = comentarios[-alterar-1]
    id = id.split(",")
    print(id)

    if id[0] == utilizador:
        newcoment = input("Novo comentario, se desejar sair, digite sair? ")
        if newcoment == "sair":
            return 0
        else:
            comentarios.pop(-alterar-1)
            comentarios.insert(-alterar-1, (utilizador + "," + id[1] + "," + "c" + "," + newcoment))

            for i in range(len(publicacoes)):
                j = publicacoes[-i-1]
                j = j.split(",")
                print(j[3], "\nIndex de publicacao: ", i)
                print("=" * 30)
                for y in range(len(comentarios)):
                    aux = comentarios[-y-1]
                    aux = aux.split(",")
                    if (aux[1] == j[1]) and (aux[2] == "c"):
                        print("Comentario de:", aux[0])
                        print("     ", aux[3], "\n      Index de comentario:", y)
                        print("-" * 30)
    else:
        print("O comentario não pode ser alterado pois não lhe pertence")

    pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
    pickle.dump(comentarios, open("comentarios.dat", "wb"))


def removerComentarios(utilizador):
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    verpublicacoes()
    if len(comentarios) == 0:
        print("Não existem comentarios")
        return 0

    removercomentario = int(input("Digite o index do comentario que pretende remover, digite -1 se pretender sair: "))
    if removercomentario == -1:
        return 0
    else:
        aux = comentarios[-removercomentario-1]
        aux = aux.split(",")

        if aux[0] == utilizador:
            comentarios.pop(-removercomentario-1)
        else:
            print("Comentario nao pertence ao utilizador")

    pickle.dump(comentarios, open("comentarios.dat", "wb"))


def verPerfil(utilizador):
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    print("Perfil de: ", utilizador)
    for i in range(len(publicacoes)):
        j = publicacoes[-i-1]
        j = j.split(",")
        print("Minhas publicacaoes: ")
        if j[0] == utilizador:
            print(j[3], "\nIndex de publicacao: ", i)
            print("=" * 30)
            for y in range(len(comentarios)):
                aux = comentarios[-y-1]
                aux = aux.split(",")
                if (aux[1] == j[1]) and (aux[2] == "c"):
                    print("Comentario de:", aux[0])
                    print("     ", aux[3], "\nIndex de comentario: ", y)
                    print("-" * 30)


def definicoesdeconta(utilizador):
    print("Definicoes de conta TODO")
