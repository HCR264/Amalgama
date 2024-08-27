import os
from Modulos.menu import menu
from datetime import datetime


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
    return find_dir


# Encontrar archivos con extensión
def find_files_wth_ext(search_path, ext):
    find_files = []
    for file in os.listdir(search_path):
        if file.endswith(ext):
            find_files.append(filter)
    return find_files


# Codigo de archivo
def code_name(key):
    code = datetime.now()
    sesion_name = key + '_Sesion_' + code.strftime('%Y%m%d%H%M%S')
    return sesion_name
