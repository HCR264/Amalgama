import os


# from Modulos.menu import clear_screen
# from Modulos.menu import multi_select_menu
from Modulos.menu import menu


Global_Dir = '/home/harold/Documents/Tesis/Programa'


def select_dir(Search_Dir, Info):
    Dirs = os.listdir(Search_Dir)
    Num_Dir_Selected = menu(Dirs, Info)
    Dir_Selected = Dirs[Num_Dir_Selected]
    return Dir_Selected


def main_micromegas(Global_Dir):
    Sesion_Dir = Global_Dir + '/Sesiones'

    menu_info = 'Seleccione la sesión con la que quiere trabajar:'
    Sesions = os.listdir(Sesion_Dir)
    Num_Sesion_Selected = menu(Sesions, menu_info)
    Sesion_Selected = Sesions[Num_Sesion_Selected]
    input(Sesion_Selected)

if __name__ == '__main__':
    main_micromegas(Global_Dir)
