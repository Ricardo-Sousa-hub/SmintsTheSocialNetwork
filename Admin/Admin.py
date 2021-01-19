from Menus import Menu
from Admin.GestaoUtilizadores import MenuGU
from Admin.GestaoMSG import MenuMSG
from Admin.GestaoRede import MenuR


def MenuPrincipalAdmin():
    while True:
        op = Menu.Menu("Gestão de rede social",
                       ["Gestão Utilizadores", "Gestão Mensagens", "Gestão Rede"], 3)
        if op == 1:
            MenuGU.MenuGu()
        elif op == 2:
            MenuMSG.MenuMSG()
        elif op == 3:
            MenuR.MenuRed()
        elif op == 0:
            break
