import pickle
import random
import webbrowser
import datetime


def writehtmltweet(publicacoes, comentarios):
    if len(publicacoes) > 0:
        with open("tweet.html", "w") as f:
            f.write("""<!DOCTYPE html>
    <html> 
        <head>
            <style>
    
                hr{
                    background-color: black;
                }
    
                .tweet{
                    border-radius: 10px;
                    margin-left: 15%;
                    margin-right: 15%;
                    padding-left: 15px;
                    padding-right: 15px;
                    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin-top: 1%;
                    margin-bottom: 1%;
                }
    
                .nome{
                    font-size: 15px;
                    font-weight: bold;
                    margin-bottom: -13px;
                }
    
                .nome2{
                    font-size: 15px;
                    font-weight: bold;
                    margin-bottom: -13px;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
    
                .alinhamento{
                    margin-left: 150px;
                    margin-right: 150px;
                }
    
                .comentario{
                    margin-left: 15%;
                    margin-right: 15%;
                    padding-left: 15px;
                    padding-right: 15px;
                    border: 1px solid black;
                }
    
            </style>
        </head>
        <body>
            <div class="alinhamento">\n""")
            for i in range(len(publicacoes)):
                j = publicacoes[i]
                j = j.split(".")
                f.write(f"""<div class="tweet">
                    <p class="nome">{j[0]} Hora de publicacao: {j[4]}</p>
                    <p>{j[3]}</p>
                </div>""")
                f.write('''<div class="comentario">''')
                for y in range(len(comentarios)):
                    aux = comentarios[y]
                    aux = aux.split(".")
                    if (aux[1] == j[1]) and (aux[2] == "c"):
                        f.write(f'''<p class="nome2">{aux[0]} Hora de comentario: {aux[4]}</p>
                    <p>{aux[3]}</p>
                    <hr>''')
                f.write("</div>")
            f.write("""    </div>    
        </body>
    </html>""")
            f.close()
    else:
        with open("tweet.html", "w") as f:
            f.write("""<!DOCTYPE html>
                <html> 
                    <body>
                        <h1>Isto parece vazio</h1>
                        <h1>Tenta fazer uma publicacao</h1>
                    </body>
                </html>""")
        f.close()


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
                publicacoes.append(utilizador + "." + str(x) + "." + "pub" + "." + publicacao + "." + str(datetime.datetime.now()))
                while True:
                    comentario = input("Comentario? ")
                    if comentario == "sair":
                        break
                    else:
                        comentarios.append(utilizador + "." + str(x) + "." + "c" + "." + comentario + "." + str(datetime.datetime.now()))

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
                listapublicacoes.append(utilizador + "." + str(x) + "." + "pub" + "." + publicacao + "." + str(datetime.datetime.now()))
                while True:
                    comentario = input("Comentario? ")
                    if comentario == "sair":
                        break
                    else:
                        listacoments.append(utilizador + "." + str(x) + "." + "c" + "." + comentario + "." + str(datetime.datetime.now()))

        pickle.dump(listapublicacoes, open("publicacoes.dat", "wb"))
        pickle.dump(listacoments, open("comentarios.dat", "wb"))
        pickle.dump(ids, open("ids.dat", "wb"))


def verpublicacoes():
    try:
        publicacoes = pickle.load(open("publicacoes.dat", "rb"))
        comentarios = pickle.load(open("comentarios.dat", "rb"))

        for i in range(len(publicacoes)):
            j = publicacoes[i]
            j = j.split(".")
            print("Autor:", j[0], " Hora de publicacao: ", j[4])
            print(j[3], "\nIndex de publicacao: ", i)
            print("=" * 30)
            for y in range(len(comentarios)):
                aux = comentarios[y]
                aux = aux.split(".")
                if (aux[1] == j[1]) and (aux[2] == "c"):
                    print("Comentario de:", aux[0], " Hora: ", aux[4])
                    print("     ", aux[3], "\nIndex de comentario: ", y)
                    print("-" * 30)

        writehtmltweet(publicacoes, comentarios)
        webbrowser.open_new_tab("tweet.html")
    except Exception:
        print("Ainda não existem publicacoes.")


def comentarPublicacoes(utilizador):
    verpublicacoes()
    selecao = int(input("Digite o index da publicacao que quer comentar: "))
    comentario = input("Digite o comentario, se desejar sair digite sair? ")

    if comentario == "sair":
        return 0
    else:
        publicacoes = pickle.load(open("publicacoes.dat", "rb"))
        comentarios = pickle.load(open("comentarios.dat", "rb"))
        x = publicacoes[selecao]
        x = x.split(".")
        comentarios.append(utilizador + "." + str(x[1]) + "." + "c" + "." + comentario + "." + str(datetime.datetime.now()))
        pickle.dump(comentarios, open("comentarios.dat", "wb"))


def alterarPublicacoes(utilizador):
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    verpublicacoes()
    indexpub = int(input("Digite o index da publicacao que pretende alterar: "))

    aux = publicacoes[indexpub]
    aux = aux.split(".")
    if aux[0] == utilizador:
        alterarpub = input("Digite a nova publicacao, se desejar sair, digite ssair: ")
        if alterarpub == "sair":
            return 0
        else:
            publicacoes.pop(indexpub)
            publicacoes.insert(indexpub, (utilizador + "." + str(aux[1]) + "." + "pub" + "." + alterarpub + "." + str(datetime.datetime.now())))
            pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
    else:
        print("Nao pode modificar esta publicacao pois nao lhe pertence.")


def removerPublicacoes(utilizador):
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    for i in range(len(publicacoes)):
        j = publicacoes[i]
        j = j.split(".")
        if j[0] == utilizador:
            print(j[3], "Hora: ", j[4] ,"\nIndex de publicacao: ")
            print("=" * 30)
            for y in range(len(comentarios)):
                aux = comentarios[y]
                aux = aux.split(",")
                if (aux[0] == utilizador) and (aux[1] == j[1]) and (aux[2] == "c"):
                    print("     ", aux[3], "Hora: ", j[4] ,"\n      Index de comentario:", y)
                    print("-" * 30)

    remove = input("Digite o index da publicacao que deseja remover, se desejar sair, digite sair: ")
    if remove == "sair":
        return 0
    else:
        remove = int(remove)
        autor = publicacoes[remove].split(".")
        if autor[0] == utilizador:
            print(publicacoes[remove])
            aux = publicacoes[remove]
            aux = aux.split(".")

            user = utilizador

            publicacoes.pop(remove)
            listapos = []

            for i in range(len(comentarios)):
                j = comentarios[i]
                j = j.split(".")
                if j[0] == user and j[1] == aux[1]:
                    listapos.append(comentarios[i])

            for i in listapos:
                comentarios.remove(i)
        else:
            print("Nao pode remover esta publicacao, pois nao lhe pertence.")

        print("Publicacao removida com sucesso.")

        pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
        pickle.dump(comentarios, open("comentarios.dat", "wb"))


def alterarComentarios(utilizador):
    verpublicacoes()
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    alterar = int(input("Index de comentario? "))

    id = comentarios[alterar]
    id = id.split(".")
    print(id)

    if id[0] == utilizador:
        newcoment = input("Novo comentario, se desejar sair, digite sair? ")
        if newcoment == "sair":
            return 0
        else:
            comentarios.pop(alterar)
            comentarios.insert(alterar, (utilizador + "." + id[1] + "." + "c" + "." + newcoment + "." + str(datetime.datetime.now())))

            for i in range(len(publicacoes)):
                j = publicacoes[i]
                j = j.split(".")
                print(j[3], "Hora:", j[4] , "\nIndex de publicacao: ", i)
                print("=" * 30)
                for y in range(len(comentarios)):
                    aux = comentarios[y]
                    aux = aux.split(".")
                    if (aux[1] == j[1]) and (aux[2] == "c"):
                        print("Comentario de:", aux[0])
                        print("     ", aux[3], "Hora: ",aux[4] ,"\n      Index de comentario:", y)
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
        aux = comentarios[removercomentario]
        aux = aux.split(".")

        if aux[0] == utilizador:
            comentarios.pop(removercomentario)
        else:
            print("Comentario nao pertence ao utilizador")

    pickle.dump(comentarios, open("comentarios.dat", "wb"))


def verPerfil(utilizador):
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    print("Perfil de: ", utilizador)
    print(f"Publicacoes de {utilizador}: ")
    for i in range(len(publicacoes)):
        j = publicacoes[i]
        j = j.split(".")
        if j[0] == utilizador:
            print(j[3], "Hora: ", j[4] ,"\nIndex de publicacao: ", i)
            print("=" * 30)
            for y in range(len(comentarios)):
                aux = comentarios[y]
                aux = aux.split(".")
                if (aux[1] == j[1]) and (aux[2] == "c"):
                    print("Comentario de:", aux[0])
                    print("     ", aux[3],"Hora: ", aux[4] , "\nIndex de comentario: ", y)
                    print("-" * 30)


def definicoesdeconta(utilizador):
    print("Definicoes de conta de", utilizador)
    print("TODO...")


def gostardepublicacao(utilizador):
    print("Gostos de publicacao...TODO...")

def gostardecomentarios(utilizador):
    print("Gostos de comentarios...TODO...")


