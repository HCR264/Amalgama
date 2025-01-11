#Librerias
import os
import subprocess
import time
from shutil import copy
import re
from numpy import random

#Funciones propias
from .menu import clear_screen, multi_select_menu, menu
from .files import select_dir, select_dir_wth_keyword, find_files_wth_ext
from .mO_f import create_project, get_funct, set_funct

#Posible libreria para paralelizar
#import concurrent.futures

menu_info_1 = 'Seleccione la sesió con la que quiere trabajar:'

info_sesion_dir_1 = '\nNo se encontró ningún directorio con los archivos requeridos para ejecutar micrOMEGAS.\n\nPresione ENTER para volver.'
info_sesion_dir_2 = '\nNo se encontraron los archivos necesarios para ejecutar micrOMEGAS.\n\nPresione ENTER para volver.'

menu_info_2 = 'Seleccione las funciones que desea que micrOMEGAS realice.'

info_make = '\n\n\nNo se ha podido crear el programa "main.c"'

def main_micromegas(Global_Dir):
#Definir Directorios principales
    Sesions_Dir = Global_Dir + '/Sesiones'
    Micromegas_Dir = Global_Dir + '/micromegas_6.1.15'

#Seleccionar sesion con la que se va a trabajar
    Sesion_Dir = f'{Sesions_Dir}/{select_dir(Sesions_Dir, menu_info_1)}'
    Select_Sesion_Dir = select_dir_wth_keyword(Sesion_Dir, 'CH')
    if Select_Sesion_Dir == "":
        input(info_sesion_dir_1)
        return
    CH_Dir = f'{Sesion_Dir}/{Select_Sesion_Dir}'
    mdl_files = find_files_wth_ext(CH_Dir, '.mdl')
    if len(mdl_files) != 5:
        input(info_sesion_dir_2)
        return
#Crear el proyecto de micromegas y copia los archivos necesarios
    Project_Dir = create_project(Global_Dir, Micromegas_Dir, CH_Dir, mdl_files)


#Seleccionar las funciones que queremos que micrOMEGAS haga
    all_functions = get_funct(f'{Project_Dir}/main.c')
    set_funct(f'{Project_Dir}/main.c', multi_select_menu(all_functions,menu_info_2))
    clear_screen()


#Ejecutar make
    os.system(f'cd {Project_Dir} && make main=main.c')
#    clear_screen()
    input(Project_Dir)
    if not os.path.exists(f'{Project_Dir}/main'):
        input(info_make)
        return

    
