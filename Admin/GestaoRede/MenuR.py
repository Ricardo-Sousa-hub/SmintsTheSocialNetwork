from Menus import Menu
from Admin.GestaoRede import Gestao_de_rede


def MenuRed():
    while True:

        op = Menu.Menu("Gestão de Rede",
                       ["IP", "DNS", "Pesquisa por nome"], 3)

        if op == 1:
            Gestao_de_rede.IP()
        elif op == 2:
            Gestao_de_rede.DNS()
        elif op == 3:
            Gestao_de_rede.pesquisa()
        elif op == 0:
            break
