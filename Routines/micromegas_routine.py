import os


# from Modulos.menu import clear_screen
# from Modulos.menu import multi_select_menu
from Modulos.files import select_dir
from Modulos.files import select_dir_wth_keyword


Global_Dir = '/home/harold/Documents/Tesis/Programa'


def main_micromegas(Global_Dir):
    Sesions_Dir = Global_Dir + '/Sesiones'

    menu_info = 'Seleccione la sesión con la que quiere trabajar:'
    Sesion_Dir = Sesions_Dir + '/' + select_dir(Sesions_Dir, menu_info)
    CH_Dir = Sesion_Dir + '/' + select_dir_wth_keyword(Sesion_Dir, 'CH')
    input(CH_Dir)

if __name__ == '__main__':
    main_micromegas(Global_Dir)
