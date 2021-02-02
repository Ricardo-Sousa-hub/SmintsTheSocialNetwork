from Menus import Menu
from Admin.GestaoRede import Gestao_de_rede


def MenuRed():
    while True:

        op = Menu.Menu("Gestão de Rede",
                       ["IP", "DNS"], 2)

        if op == 1:
            Gestao_de_rede.IP()
        elif op == 2:
            Gestao_de_rede.DNS()
        elif op == 0:
            break
