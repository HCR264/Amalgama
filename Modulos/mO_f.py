import os
import re
import subprocess
from multiprocessing import Pool, cpu_count, Manager
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


def vars_Info(varFile):
    names = []
    values = []
    comments = []
    options = []
    with open(varFile, 'r') as file:
        lines = file.readlines()

    for line in lines:
        option = ''
        elements = []
        if '|' in line:
            if '|>' in line:
                pass
            else:
                elements = re.split(r'[|]', line)
                elements = [element.strip() for element in elements]
                if len(elements) > 2:
                    elements[2] = ' '.join(elements[2].split())
                options.append(f'{elements[0]} | {elements[2]}')
                names.append(elements[0])
                values.append(elements[1])
                comments.append(elements[2] if len(elements) > 2 else '')
    return names, values, comments, options


def getOmega(data):
    omega = data.split('Omega=')[1].split('\n')[0].strip()
    return omega
    

def parNone(dir, name, value):
    run_main = f'cd {dir} && ./main data.par'
    resultFile = f'{dir}/Results/results.txt'
    input(f'{run_main}, {resultFile}')
    resultData = subprocess.run([run_main], shell=True, capture_output=True, text=True).stdout
    omega = getOmega(resultData)
    input(omega)
    #with open(resultFile, 'a') as file:

