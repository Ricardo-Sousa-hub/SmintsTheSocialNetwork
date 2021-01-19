from Menus import Menu
from Admin.GestaoMSG import Gestao_de_mensagens


def MenuMSG():
    while True:

        op = Menu.Menu("Gestão de Mensagens",
                       ["Inserir", "Alterar", "Eliminar", "Listar todas", "Pesquisa filtrada"], 5)
        if op == 1:
            Gestao_de_mensagens.addpublicacao()
        elif op == 2:
            Gestao_de_mensagens.alterarpublicacao()
        elif op == 3:
            Gestao_de_mensagens.eliminarpublicacao()
        elif op == 4:
            Gestao_de_mensagens.gestaodemensagens()
        elif op == 5:
            Gestao_de_mensagens.pesquisafiltrada()
        elif op == 0:
            break
