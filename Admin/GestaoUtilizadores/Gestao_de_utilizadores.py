import pickle
import webbrowser
import re
import datetime


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
    return (users, email, telefone, idade, palavrapasse)


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

    return email


def modificar(opcao, lista, op):
    if op == 1:
        text = "nome"
    elif op == 2:
        text = "email"
    elif op == 3:
        text = "contacto"
        opcao = str(opcao)
    if opcao in lista:
        num = lista.index(opcao)

        if op == 1:
            update = input("Digite o novo {}: ".format(text))

            while any(char.isdigit() for char in update) and any(char.isalpha() for char in update) or any(
                    char.isdigit() for char in update):
                print("Digite um nome valido.")
                update = input("Digite o novo {}: ".format(text))

            while update == opcao:
                print("Por favor digite um nome diferente do que pretende modificar")
                update = input("Digite o novo {}: ".format(text))

        elif op == 2:
            update = input("Digite o novo {}: ".format(text))

            update = verificaremail(update)

            while update == opcao:
                print("Digite um email diferente do que pretende modificar")
                update = input("Digite o novo {}: ".format(text))
        elif op == 3:
            update = input("Digite o novo {}: ".format(text))

            while validacao_para_numero(update) == True:
                print("Digite um numero valido.")
                update = input("Numero de utilizador? ")

            while update == opcao:
                print("Digite um numero de utilziador diferente do que pretende modificar")
                update = input("Digite o novo {}: ".format(text))
            while len(update) > 9 or len(update) < 9:
                print("O numero de telefone tem de ter 9 digitos")
                update = input("Numero de utilizador? ")

            update = valnum(update)

        lista.pop(num)
        lista.insert(num, update)
    else:
        print("Utilizador não encontrado")


def inserirUtilizadores():
    print("Inserir utilizador")
    try:
        users, email, telefone, idades, palavrapasse = pickleabrir()

        nome = str(input("Nome de utilizador? "))

        while any(char.isdigit() for char in nome) and any(char.isalpha() for char in nome) or any(
                char.isdigit() for char in nome):
            print("Erro, por favor digite um nome valido.")
            nome = input("Nome de utilizador? ")

        users.append(nome)
        mail = str(input("Email de utilizador? "))

        mail = verificaremail(mail)

        email.append(mail)
        numero = input("Numero de utilizador: ")

        x = list(numero)

        while " " in x:
            print("O numero que digitou contem espaços, por favor reescreva o numero.")
            numero = input("Numero de utilizador: ")
            x = list(numero)

        while validacao_para_numero(numero) == True:
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

        data = int(input("Data de nascimento: "))

        idade = datetime.date.today().year - (data % 10000)

        idades.append(idade)

        password = input("Palavra passe: ")
        palavrapasse.append(password)

        writehtml(users, email, telefone, idades)

        picklefechar(users, email, telefone, idades, palavrapasse)

    except (OSError, IOError) as e:
        users = []
        email = []
        telefone = []
        idades = []
        palavrapasse = []
        nome = str(input("Nome de utilizador? "))

        while any(char.isdigit() for char in nome) and any(char.isalpha() for char in nome) or any(
                char.isdigit() for char in nome):
            print("Erro, por favor digite um nome valido.")
            nome = input("Nome de utilizador? ")

        users.append(nome)
        mail = str(input("Email de utilizador? "))

        while mail in email:
            print("Email já existe")
            mail = str(input("Email de utilizador? "))

        mail = verificaremail(mail)

        email.append(mail)
        numero = input("Numero de utilizador: ")

        while validacao_para_numero(numero) == True:
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
                "Pretende modificar: \n 1-Nome de utilizador \n 2-Email de utilizador \n 3-Numero de utilizadores \n Opcao: "))
            if op == 1:
                nome = input("Digite o nome de utilizador que pretende alterar: ")

                while any(char.isdigit() for char in nome) and any(char.isalpha() for char in nome) or any(
                        char.isdigit() for char in nome):
                    print("Erro, por favor digite um nome valido.")
                    nome = input("Nome de utilizador? ")

                modificar(nome, users, op)

                pickle.dump(users, open("telefone.dat", "wb"))

            elif op == 2:
                mail = input("Digite o email de utilizador que pretende alterar: ")
                mail = verificaremail(mail)
                modificar(mail, email, op)

                pickle.dump(email, open("correio.dat", "wb"))

            elif op == 3:
                numero = input("Digite o numero de utilizador que pretende alterar: ")

                while validacao_para_numero(numero) == True:
                    print("Numero de utilizador inválido.")
                    numero = input("Numero de utilizador: ")

                while len(numero) > 9 or len(numero) < 9:
                    print("O numero de telefone tem de ter 9 digitos")
                    numero = input("Numero de utilizador? ")

                numero = valnum(numero)

                modificar(numero, telefone, op)

                pickle.dump(telefone, open("telefone.dat", "wb"))

        else:
            print("Nao existem utilizadores")

    except (OSError, IOError) as e:
        print("Não existem dados")


def eliminarUtilizador():
    print("Eliminar utilizadores")
    try:
        users, email, telefone, idades, palavrapasse = pickleabrir()

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

                    email.pop(users.index(delete))
                    telefone.pop(users.index(delete))
                    idades.pop(users.index(delete))
                    palavrapasse.pop(users.index(delete))
                    users.remove(delete)

                    picklefechar(users, email, telefone, idades, palavrapasse)

                    writehtml(users, email, telefone, idades)
                    break
                except ValueError:
                    print("Utilizador não encontrado")
        else:
            print("Nao existem utilizadores")
    except(OSError, IOError) as e:
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

    except(OSError, IOError) as e:
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
            else:
                if pesquisa in str(telefone):
                    print("==========================================")
                    print("Info sobre", pesquisa)
                    print("Nome:", users[telefone.index(pesquisa)])
                    print("Idade:", idades[telefone.index(pesquisa)])
                    print("Email:", email[telefone.index(pesquisa)])
                    print("==========================================")
                else:
                    if pesquisa in email:
                        print("==========================================")
                        print("Info sobre", pesquisa)
                        print("Nome:", users[email.index(pesquisa)])
                        print("Idade:", idades[email.index(pesquisa)])
                        print("Contacto:", telefone[email.index(pesquisa)])
                        print("==========================================")
                    else:
                        print(pesquisa, "nao encontrado")
        else:
            print("Nao existe ennhum utilizador")
    except(OSError, IOError) as e:
        print("Não existem dados")
