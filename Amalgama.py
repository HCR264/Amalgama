#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:30:25 2024

@author: hcr
"""

#   MODULOS
import os
import sys
import termios
import tty
import shutil
#from wolframclient.evaluation import WolframLanguageSession

from Modulos import FeynRules_Rutine_main


#   FUNCIONES
# Limpiar pantalla
def clear_screen():
    os.system('clear')


# Capturar las teclas pulsadas
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == '\x1b':
            ch += sys.stdin.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# Imprimir las opciones del menú
def print_menu(options, selected_index, menu_info):
    clear_screen()
    print(menu_info)
    print('\n')
    for i, option in enumerate(options):
        prefix = "> " if i == selected_index else "  "
        print(f"{prefix}{option}")


# Mostrar menú
def menu(options, menu_info):
    selected_index = 0
    while True:
        print_menu(options, selected_index, menu_info)
        key = get_key()

        if key == '\x1b[A':  # Arriba
            selected_index = (selected_index - 1) % len(options)
        elif key == '\x1b[B':  # Abajo
            selected_index = (selected_index + 1) % len(options)
        elif key == '\r':  # Enter
            return selected_index


# Verificar la existencia de un archivo
def exist_file(file_dir):
    return os.path.isfile(file_dir)


# Buscar archivos
def find_files(filename, search_path):
    matches = []
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            matches.append(os.path.join(root, filename))
    matches.append("Volver a buscar")
    matches.append("Salir")
    return matches


# Mover archivos
def move_files(filename, src_path, dst_path):
    if os.path.isfile(dst_path + "/" + filename) is True:
        print("\nEl archivo ya existe en " + dst_path)
        input("Presione Enter para salir...")
    else:
        shutil.copy2(src_path, dst_path, follow_symlinks=True)
        print("\nEl archivo fue movido con exito a " + dst_path)
        input("Presione Enter para salir...")


# Importar modelos a 'Modelos'
def import_models(dst_path):
    while True:
        os.system('clear')

        filename = input("Ingrese el nombre del modelo: ")
        search_path = "/home"

        matches = find_files(filename, search_path)

        if len(matches) == 2:
            print("No se ha encontrado el archivo.")
            option = input("¿Desea volver a intentarlo? (y/n): ")
            if option == "n":
                break
            else:
                continue

        elif len(matches) == 3:
            selected = menu(matches, f"Se encontró 1 archivo que coincide con el nombre en {matches[0]}")
            if matches[selected] == "Volver a buscar":
                continue
            elif matches[selected] == "Salir":
                break
            else:
                input(matches[selected])
                input(dst_path)
                move_files(filename, matches[selected], dst_path)
                break
        else:
            selected = menu(matches, f"Se encontraron {len(matches)-2} archivos que coinciden con el nombre. Seleccione el archivo que desee importar:")
            if matches[selected] == "Volver a buscar":
                continue
            elif matches[selected] == "Salir":
                break
            else:
                move_files(filename, matches[selected], dst_path)
                break


def find_files_wth_ext(search_path, ext):
    find_files = []
    for file in os.listdir(search_path):
        if file.endswith(".fr"):
            find_files.append(file)
    return find_files


# MENUS
# Lista de los modelos
def model_list():
    clear_screen()

    model_list = find_files_wth_ext(ModelsDir, ".fr")
    print("Modelos importados:\n")

    prefix = "- "
    for i, files in enumerate(model_list):
        print(prefix + files)

    input("\nPresiona Enter para salir...")


# Menu para manipular FeynRules
def FeynRulesMenu():
    clear_screen()

    menu_info = "CREACIÓN DE NOTEBOOK\n"
    options = [""]



# Menu Principal
def main_menu():
    menu_info = "Selecciones la acción que quiere realizar."
    options = ["Importar un modelo", "Ver modelos", "FeynRules", "Nada, nadota", "Salir"]

    while True:
        selected = menu(options, menu_info)
        if options[selected] == "Salir":
            print("Saliendo...")
            break
        elif options[selected] == "Importar un modelo":
            import_models(ModelsDir)
        elif options[selected] == "Ver modelos":
            model_list()
        elif options[selected] == "FeynRules":
            FeynRules_Rutine_main()
        else:
            print(f"Seleccionó: {options[selected]}")
            input("Presiona Enter para continuar...")


def create_dir(src_dir, dir_name):
    os.mkdir(src_dir + "/" + dir_name)


# MAIN
def main():
    # VARIABLES GLOBALES
    global GlogalDir
    global FeynRulesDir
    global ModelsDir
    global Plantilla_FeynRules_NB
    global Sesions_Dir

    # OBTENER EL DIRECTORIO DE TRABAJO
    GlobalDir = os.getcwd()

    # Definir las carpetas de trabajo
    FeynRulesDir = GlobalDir + '/feynrules-current'
    ModelsDir = GlobalDir + '/Modelos'
    Plantilla_FeynRules_NB = GlobalDir + '/.Plantilla_FeynRules_Script'
    Sesions_Dir = GlobalDir + '/Sesiones'

    main_menu()
if __name__ == "__main__":
    main()
