import pickle
import webbrowser
import re
import datetime
from Utilizador.Utilizador import verPerfil



def writehtml(users, email, telefone, idade):
    with open("utilizadores.html", "w") as f:
        f.write("""<!DOCTYPE html>
<html> 
    <head>
        <style>
            #users{
              font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
              border-collapse: collapse;
              width: 100%;
            }

            #users td, #users th{
                border: 1px solid #ddd;
                padding: 8px;
            }

            #users tr:nth-child(even){background-color: #f2f2f2;}
            
            #users tr:hover {background-color: #ddd;}

            #users th{
                padding-top: 12px;
                padding-bottom: 12px;
                text-align: left;
                background-color: Green;
                color: white;
            }
        </style>
    </head>
    <body>
        <table id="users">
            <tr>
                <th>Utilizador</th>
                <th>Idade</th>
                <th>Contacto</th>
                <th>Email</th>
            </tr>\n""")
        for i in range(len(users)):
            f.write(
                "       <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr> \n".format(users[i], idade[i],
                                                                                         telefone[i], email[i]))
        f.write("""    </table>    
    </body>
</html>""")
        f.close()


def picklefechar(users, email, telefone, idade, palavrapasse):
    pickle.dump(users, open("users.dat", "wb"))
    pickle.dump(email, open("correio.dat", "wb"))
    pickle.dump(telefone, open("telefone.dat", "wb"))
    pickle.dump(idade, open("Data.dat", "wb"))
    pickle.dump(palavrapasse, open("Password.dat", "wb"))


def pickleabrir():
    users = pickle.load(open("users.dat", "rb"))
    email = pickle.load(open("correio.dat", "rb"))
    telefone = pickle.load(open("telefone.dat", "rb"))
    idade = pickle.load(open("Data.dat", "rb"))
    palavrapasse = pickle.load(open("Password.dat", "rb"))
    return users, email, telefone, idade, palavrapasse


def valnum(update):
    aux = int(update) // 1000000
    aux1 = int(update) // 10000000
    aux2 = int(update) // 1000000
    indicativos = [91, 921, 9240, 9241, 9243, 9244, 925, 926, 927, 929, 93, 96]

    while (aux not in indicativos) and (aux1 not in indicativos) and (aux2 not in indicativos):
        print("Por favor digite um numero valido")
        update = input("Numero de utiliziador: ")
        aux = int(update) // 1000000
        aux1 = int(update) // 10000000
        aux2 = int(update) // 1000000

    return update


def validacao_para_numero(contacto):
    return any(char.isdigit() for char in contacto) and any(char.isalpha() for char in contacto) or any(
        char.isalpha() for char in contacto) and contacto == "" and contacto == " "


def verificaremail(mail):
    email = pickle.load(open("correio.dat", "rb"))
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while not re.search(regex, mail) or mail in email:
        print("Email invalido")
        mail = input("Digite o seu email novamente: ")

    return mail


def modificarNome(nome, lista, op):
    users, email, telefone, idades, palavrapasse = pickleabrir()
    novonome = str(input("Digite o novo nome: "))
    while " " in novonome and novonome in users:
        print("Erro, por favor digite um nome valido.")
        novonome = str(input("Nome de utilizador? "))

    for i in range(len(lista)):
        if lista[i] == nome:
            pos = i
            lista.pop(pos)
            lista.insert(pos, novonome)

    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))

    for i in range(len(publicacoes)):
        x = publicacoes[i]
        x = x.split(".")
        if x[0] == nome:
            x[0] = novonome
            publicacoes.pop(i)
            x = ".".join(x)
            publicacoes.insert(i, x)
        for y in range(len(comentarios)):
            k = comentarios[y]
            k = k.split(".")
            if k[0] == nome:
                k[0] = novonome
                comentarios.pop(y)
                k = ".".join(k)
                comentarios.insert(y, k)

    pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
    pickle.dump(comentarios, open("comentarios.dat", "wb"))
    picklefechar(users, email, telefone, idades, palavrapasse)


def modificarEmail(user, lista, users, op):
    novoemail = str(input("Digite um novo email: "))
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while not re.search(regex, novoemail) or novoemail in lista:
        print("Email invalido")
        novoemail = str(input("Digite o seu email novamente: "))
    for i in range(len(users)):
        if users[i] == user:
            lista.pop(i)
            lista.insert(i, str(novoemail))


def modificarContacto(user, lista, users, op):
    novonumero = input("Digite novo contacto: ")
    aux = valnum(novonumero)

    for i in range(len(users)):
        if users[i] == user:
            lista.pop(i)
            lista.insert(i, str(aux))


def modificarPassword(user, lista, users, op):
    novapalavra = input("Nova palavra passe: ")

    for i in range(len(users)):
        if users[i] == user:
            lista.pop(i)
            lista.insert(i, str(novapalavra))


def inserirUtilizadores():
    print("Inserir utilizador")
    try:
        users, email, telefone, idades, palavrapasse = pickleabrir()

        nome = str(input("Nome de utilizador? "))

        while " " in nome and nome in users:
            print("Erro, por favor digite um nome valido.")
            nome = input("Nome de utilizador? ")

        users.append(nome)
        mail = str(input("Email de utilizador? "))
        mail = verificaremail(mail)
        while mail in email:
            print("Email já em uso")
            mail = str(input("Email de utilizador? "))
            mail = verificaremail(mail)
        email.append(mail)
        numero = input("Numero de utilizador: ")

        x = list(numero)

        while " " in x:
            print("O numero que digitou contem espaços, por favor reescreva o numero.")
            numero = input("Numero de utilizador: ")
            x = list(numero)

        while validacao_para_numero(numero):
            print("Numero de utilizador inválido.")
            numero = input("Numero de utilizador: ")

        while len(numero) > 9 or len(numero) < 9:
            print("O numero de telefone tem de ter 9 digitos")
            numero = input("Numero de utilizador? ")

        while numero in list(telefone):
            print("Numero já registado, por favor digite outro numero")
            numero = input("Numero de utilizador? ")

        numero = valnum(numero)

        telefone.append(numero)

        data = input("Data de nascimento do tipo dd-mm-aaaa: ")
        while '/' in data or ' ' in data:
            print("Por favor digite uma data valida")
            data = input("Data de nascimento do tipo dd-mm-aaaa: ")

        data = data.split('-')
        if datetime.datetime.today().month > int(data[1]):
            idade = datetime.datetime.today().year - int(data[2])
        else:
            if datetime.datetime.today().month == int(data[1]):
                if datetime.datetime.today().day >= int(data[0]):
                    idade = datetime.datetime.today().year - int(data[2])
                else:
                    idade = datetime.datetime.today().year - int(data[2]) - 1
            else:
                idade = datetime.datetime.today().year - int(data[2]) - 1

        idades.append(idade)

        password = input("Palavra passe: ")
        palavrapasse.append(password)

        writehtml(users, email, telefone, idades)

        picklefechar(users, email, telefone, idades, palavrapasse)

    except (OSError, IOError):
        users = []
        email = []
        telefone = []
        idades = []
        palavrapasse = []
        nome = str(input("Nome de utilizador? "))

        while " " in nome and nome in users:
            print("Erro, por favor digite um nome valido.")
            nome = input("Nome de utilizador? ")

        users.append(nome)
        mail = str(input("Email de utilizador? "))

        while mail in email:
            print("Email já existe")
            mail = str(input("Email de utilizador? "))

        if len(email) > 0:
            mail = verificaremail(mail)

        email.append(mail)
        numero = input("Numero de utilizador: ")

        while validacao_para_numero(numero):
            print("Numero de utilizador inválido.")
            numero = input("Numero de utilizador: ")

        while len(numero) > 9 or len(numero) < 9:
            print("O numero de telefone tem de ter 9 digitos")
            numero = input("Numero de utilizador? ")

        numero = valnum(numero)

        telefone.append(numero)

        data = int(input("Data de nascimento: "))

        idade = datetime.date.today().year - (data % 10000)

        idades.append(idade)

        password = input("Palavra passe: ")
        palavrapasse.append(password)

        writehtml(users, email, telefone, idades)

        picklefechar(users, email, telefone, idades, palavrapasse)


def alterarUtilizador():
    print("Alterar utilizador")
    try:
        users = pickle.load(open("users.dat", "rb"))
        email = pickle.load(open("correio.dat", "rb"))
        telefone = pickle.load(open("telefone.dat", "rb"))
        users = list(users)
        email = list(email)
        telefone = list(telefone)

        if len(users) > 0:

            op = int(input(
                "Pretende modificar: \n 1-Nome de utilizador \n 2-Email de utilizador \n 3-Numero de utilizadores \n "
                "Opcao: "))
            if op == 1:
                nome = input("Digite o nome de utilizador que pretende alterar: ")

                while " " in nome and nome in users:
                    print("Erro, por favor digite um nome valido.")
                    nome = input("Nome de utilizador? ")

                modificarNome(nome, users, op)

                pickle.dump(users, open("telefone.dat", "wb"))

            elif op == 2:
                mail = input("Digite o email de utilizador que pretende alterar: ")
                mail = verificaremail(mail)
                modificarEmail(mail, email, users, op)

                pickle.dump(email, open("correio.dat", "wb"))

            elif op == 3:
                numero = input("Digite o numero de utilizador que pretende alterar: ")

                while validacao_para_numero(numero):
                    print("Numero de utilizador inválido.")
                    numero = input("Numero de utilizador: ")

                while len(numero) > 9 or len(numero) < 9:
                    print("O numero de telefone tem de ter 9 digitos")
                    numero = input("Numero de utilizador? ")

                numero = valnum(numero)

                modificarContacto(numero, telefone, users, op)

                pickle.dump(telefone, open("telefone.dat", "wb"))

        else:
            print("Nao existem utilizadores")

    except (OSError, IOError):
        print("Não existem dados")


def eliminarUtilizador():
    print("Eliminar utilizadores")
    try:
        users, email, telefone, idades, palavrapasse = pickleabrir()
        publicacoes = pickle.load(open("publicacoes.dat", "rb"))
        comentarios = pickle.load(open("comentarios.dat", "rb"))
        if len(users) > 0:
            for i in users:
                print(i)
                print("------------")
            users = list(users)
            email = list(email)
            telefone = list(telefone)
            while True:
                try:
                    delete = input("Digite o nome que quer apagar: ")
                    aux = []
                    aux1 = []
                    email.pop(users.index(delete))
                    telefone.pop(users.index(delete))
                    idades.pop(users.index(delete))
                    palavrapasse.pop(users.index(delete))
                    users.remove(delete)

                    for i in range(len(publicacoes)):
                        x = publicacoes[i]
                        x = x.split(".")
                        if x[0] == delete:
                            aux.append(i)
                            for y in range(len(comentarios)):
                                y = comentarios[y]
                                y = y.split(".")
                                if y[0] == delete:
                                    aux1.append(y)
                    for i in aux:
                        publicacoes.pop(i)
                    for y in aux1:
                        comentarios.pop(y)

                    pickle.dump(publicacoes, open("publicacoes.dat", "wb"))
                    pickle.dump(comentarios, open("comentarios.dat", "wb"))

                    picklefechar(users, email, telefone, idades, palavrapasse)

                    writehtml(users, email, telefone, idades)

                    break
                except ValueError:
                    print("Utilizador não encontrado")
        else:
            print("Nao existem utilizadores")
    except(OSError, IOError):
        print("Não existem dados")


def listarUtilizadores():
    print("Lista de utilizadores")
    try:
        users = pickle.load(open("users.dat", "rb"))
        email = pickle.load(open("correio.dat", "rb"))
        telefone = pickle.load(open("telefone.dat", "rb"))
        idades = pickle.load(open("data.dat", "rb"))

        if len(users) > 0:
            for i in users:
                print(i)
                print("------------")
                print(idades[users.index(i)])
                print("------------")
                print(email[users.index(i)])
                print("------------")
                print(telefone[users.index(i)])
                print("------#------")

            writehtml(users, email, telefone, idades)

            webbrowser.open_new_tab("utilizadores.html")
        else:
            print("Utilziadores nao encontrados")

    except(OSError, IOError):
        print("Não existem dados")


def pesquisarporUtilizador():
    print("Pesquisar por utilizador")
    try:
        users = pickle.load(open("users.dat", "rb"))
        email = pickle.load(open("correio.dat", "rb"))
        telefone = pickle.load(open("telefone.dat", "rb"))
        idades = pickle.load(open("data.dat", "rb"))

        if len(users) > 0:
            pesquisa = input("Digite um nome, email ou numero para pesquisar: ")
            if pesquisa in users:
                print("==========================================")
                print("Info sobre", pesquisa)
                print("Idade:", idades[users.index(pesquisa)])
                print("Email:", email[users.index(pesquisa)])
                print("Contacto:", telefone[users.index(pesquisa)])
                print("==========================================")
                verPerfil(pesquisa)
            else:
                if pesquisa in str(telefone):
                    print("==========================================")
                    print("Info sobre", pesquisa)
                    print("Nome:", users[telefone.index(pesquisa)])
                    print("Idade:", idades[telefone.index(pesquisa)])
                    print("Email:", email[telefone.index(pesquisa)])
                    print("==========================================")
                    verPerfil(users[telefone.index(pesquisa)])
                else:
                    if pesquisa in email:
                        print("==========================================")
                        print("Info sobre", pesquisa)
                        print("Nome:", users[email.index(pesquisa)])
                        print("Idade:", idades[email.index(pesquisa)])
                        print("Contacto:", telefone[email.index(pesquisa)])
                        print("==========================================")
                        verPerfil(users[email.index(pesquisa)])

                    else:
                        print(pesquisa, "nao encontrado")
        else:
            print("Nao existe ennhum utilizador")
    except(OSError, IOError):
        print("Não existem dados")


def pesquisafiltrada():
    publicacoes = pickle.load(open("publicacoes.dat", "rb"))
    comentarios = pickle.load(open("comentarios.dat", "rb"))
    pesquisa = input("Digite uma ou mais palavras chave para pesquisar nas publicacoes ou nos comentarios")

    for i in range(len(publicacoes)):
        aux = publicacoes[i]
        aux = aux.split(".")
        if pesquisa in aux[3]:
            print("Publicacao de ", aux[0], aux[3])
            for y in range(len(comentarios)):
                aux1 = comentarios[y]
                aux1 = aux1.split(".")
                if aux1[1] == aux[1] and pesquisa in aux1[3]:
                    print("     Comentario de ", aux1[0], aux1[3])


def estatistica():
    print("Pessoas com o mesmo provedor de email - 1")
    print("Pessoas com a mesma operadora de telemovel - 2")
    op = input("Digite a sua opcao? ")
    while not op.isdigit() or int(op) < 1 or int(op) > 2:
        print("Digite um numero valido")
        op = input("Digite a sua opcao? ")

    if int(op) == 1:
        listaauxiliar = []
        provedor = input("Digite o provedor de email que pretende procurar: ")
        e = 0
        users, email, telefone, idades, palavrapasse = pickleabrir()
        for i in range(len(email)):
            aux = email[i].split("@")
            if aux[1] == provedor:
                listaauxiliar.append(email[i])
                e = e + 1
        if e == 0:
            print("Não existem utilziadores com esse email")
        else:
            print(f"Existem {e} utilziadores com o provedor {provedor}")
            for i in listaauxiliar:
                print(i)
    elif int(op) == 2:
        users, email, telefone, idades, palavrapasse = pickleabrir()
        vodafone = 0
        meo = 0
        nos = 0
        listaauxiliar1 = []
        listaauxiliar2 = []
        listaauxiliar3 = []
        for i in range(len(telefone)):
            aux = telefone[i]
            if aux[:2] == '91' or aux[:3] == '921':
                vodafone = vodafone + 1
                listaauxiliar1.append(telefone[i])
            else:
                if aux[:2] == '96' or (aux[:3] == '925' or aux[:3] == '926' or aux[:3] == '927') or (aux[:4] == '9240' or aux[:4] == '9241' or aux[:4] == '9243' or aux[:4] == '9244'):
                    meo = meo + 1
                    listaauxiliar2.append(telefone[i])
                else:
                    if aux[:2] == '93' or aux[:3] == '929':
                        nos = nos + 1
                        listaauxiliar3.append(telefone[i])

        print(f"Existem {meo} utilizadores que sao clientes da operadora MEO")
        print("Meo: ")
        for i in listaauxiliar2:
            print(i)
        print(f"Existem {nos} utilziadores que sao clientes da operadora NOS")
        print("NOS: ")
        for i in listaauxiliar3:
            print(i)
        print(f"Existem {vodafone} utilizadores que sao clientes da operadora VODAFONE")
        print("VODAFONE: ")
        for i in listaauxiliar1:
            print(i)