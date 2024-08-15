import os
from Modulos.menu import menu


# Obtener el directorio de trabajo
def get_dir():
    dir = os.getcwd()
    return dir


# Seleccionar un directorio
def select_dir(Search_Dir, Info):
    Dirs = os.listdir(Search_Dir)
    Num_Dir_Selected = menu(Dirs, Info)
    Dir_Selected = Dirs[Num_Dir_Selected]
    return Dir_Selected


# Buscar un directorio con una keyword
def select_dir_wth_keyword(Search_Dir, Keyword):
    find_dir = ""
    for root, dirs, files in os.walk(Search_Dir):
        for dir in dirs:
            if Keyword.lower() in dir.lower():
                find_dir = dir
    if find_dir == "":
        input("No se encontró ningún directorio.") 
    return find_dir
