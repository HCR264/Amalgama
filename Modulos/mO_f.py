import os
from shutil import copy

from .menu import clear_screen
from .files import code_name

def create_project(global_dir, dir, sesion_dir, files):
    clear_screen()
    print('Creando Proyecto...\n')
    name = code_name('MO')
    os.system(f'cd {dir} && ./newProject {name}')

    for file in files:
        copy(f'{sesion_dir}/{file}', f'{dir}/{name}/work/models')

    copy(f'{global_dir}/Modulos/main.c', f'{dir}/{name}')

    return f'{dir}/{name}'


def get_funct(dir_file):
    with open(dir_file, 'r') as file:
        lines = file.readlines()
    functions = []
    for line in lines:
        if 'define' in line:
            function = line.split("define",1)[1].split()[0].strip()
            functions.append(function)
    functions.remove('SHOWPLOTS*/')
    functions.remove('CLEAN')
    functions.remove('d(HIGGSBOUNDS)')
    return functions

def set_funct(dir, functions):
    for function in functions:
        with open(dir, 'r') as file:
            lines = file.readlines()
        with open(dir, 'w') as file:
            for line in lines:
                if '#define' in line and function in line:
                    file.write(f'#define {function}\n')
                else:
                    file.write(line)
