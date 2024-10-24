import os
import subprocess
import time
from shutil import copy
import re
import random

from .menu import clear_screen
# from Modulos.menu import multi_select_menu
from .files import select_dir
from .files import select_dir_wth_keyword
from .files import find_files_wth_ext
from .files import code_name
from .menu import multi_select_menu
from .menu import menu

import concurrent.futures


# def micromegas_files_check(search_path):
#     number_ch_files = len(find_files_wth_ext(search_path, '.mdl'))
def create_micromegas_project(global_dir, dir, sesion_dir, files):
    clear_screen()
    print('Creando Proyecto...\n')
    project_name = code_name('MO')
    os.system(f'cd {dir} && ./newProject {project_name}')
    project_dir = dir + '/' + project_name
    models_dir = project_dir + '/work/models'

    for file in files:
        file_dir = sesion_dir + '/' + file
        copy(file_dir, models_dir)

    copy(global_dir + '/Modulos/main.c', project_dir)

    #input(f'\n\nSe ha creado correctamente el projecto {project_name}')
    return project_dir

def extract_functions(dir_file):
    with open(dir_file, 'r') as file:
        lines = file.readlines()

    functions_in_file = []
    for line in lines:
        if 'define' in line:
            function = line.split("define",1)[1].split()[0].strip()
            functions_in_file.append(function)

    functions_in_file.remove('SHOWPLOTS*/')
    functions_in_file.remove('CLEAN')
    functions_in_file.remove('d(HIGGSBOUNDS)')
    return functions_in_file

def get_PInfo(dir_files):
    oddPrtclsN = []
    oddPrtclsM = []
    oddPrtclsP = []

    with open(dir_files, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if "|" in line: 
            PElements = []
            PElements = re.split(r"[ |]+", line)
            if PElements[1].startswith('~'):
                oddPrtclsN.append(PElements[1] + "/" + PElements[2])
                oddPrtclsM.append(PElements[5])
    oddPrtclsP = list(set(oddPrtclsM))
    return oddPrtclsN, oddPrtclsM, oddPrtclsP

def get_VInfo(dir_file):
    name = []
    value = []
    comment = []
    options = []

    with open(dir_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        option = ''
        V_Elements = []
        if "|" in line:
            if "|>" in line:
                pass
            else:
                V_Elements = re.split(r"[|]", line)
                for i, ele in enumerate(V_Elements):
                    V_Elements[i] = V_Elements[i].strip()
                option = V_Elements[0] + ' | ' + V_Elements[2]
                options.append(option)
                name.append(V_Elements[0])
                value.append(V_Elements[1])
                comment.append(V_Elements[2])
    return name, value, comment, options


def set_functions(dir_file, selected_functions):
    for function in selected_functions:
        with open(dir_file, 'r') as file:
            lines = file.readlines()
        with open(dir_file, 'w') as file:
            for line in lines:
                if "#define" in line and function in line:
                    file.write("#define " + function + "\n")
                else: 
                    file.write(line)


def get_values(list):
    values = []
    for element in list:
        print(element + ": ")
        value = input()
        values.append(value)
    return values


def create_data_files(variables, values, dir):
    with open(dir, 'w') as file:
        for i, var in enumerate(variables):
            file.write(f'{variables[i]} {values[i]}\n')


def getDataVal(variables,RMode, min, max):
    values = []
    if RMode == False:
        print('Ingrese los valores.\n')
        for var in variables:
            values.append(float(input(f'> {var}: ')))
    else:
        for i in range(0, len(variables)):
            values.append(random.uniform(min[i],max[i]))
    return values


def main_micromegas(Global_Dir):
    Sesions_Dir = Global_Dir + '/Sesiones'
    Micromegas_Dir = Global_Dir + '/micromegas_6.1.15'

    menu_info = 'Seleccione la sesión con la que quiere trabajar:'
    Sesion_Dir = Sesions_Dir + '/' + select_dir(Sesions_Dir, menu_info)
    if select_dir_wth_keyword(Sesion_Dir, 'CH') == "":
        input('\nNo se encontró ningún directorio con los archivos requeridos para ejecutar micrOMEGAS.\n\nPresione ENTER para volver.')
        pass
    else:
        CH_Dir = Sesion_Dir + '/' + select_dir_wth_keyword(Sesion_Dir, 'CH')
        mdl_files = find_files_wth_ext(CH_Dir, '.mdl')
        if len(mdl_files) != 5:
            input('\nNo se encontraron los archivos suficientes para poder ejecutar micrOMEGAS.\n\nPresione ENTER para volver.')
            exit
            pass
        else:
            Project_Dir = create_micromegas_project(Global_Dir, Micromegas_Dir, CH_Dir, mdl_files)
    clear_screen()


    functions = extract_functions(Project_Dir + '/main.c')
    menu_info = '¿Qué funciones desea realizar en micrOMEGAS?'
    selected_functions = multi_select_menu(functions, menu_info)
    set_functions(Project_Dir + '/main.c', selected_functions)
    print('\n-> main.c creado')
    time.sleep(3)
    clear_screen()
    
    os.system(f'cd {Project_Dir} && make main=main.c')
    clear_screen()

#    # Detectar Particulas Extrañas
#    # Esto será desde el archivo prtcls.mdl
#    odd_name, odd_mass, odd_par = get_PInfo(Project_Dir + "/work/models/prtcls1.mdl")
#    part_list = ''
#    for i, name in enumerate(odd_name):
#       part_list = part_list + odd_name[i] + '\t| ' + odd_mass[i] + '\n'
    
    #Detectar Parametros
    var_name, var_val, var_comment, var_opt = get_VInfo(Project_Dir + "/work/models/vars1.mdl")
    
    #Seleccionar Parametros
    menu_info = '¿Qué parametros desea variar?'
    selected_var = multi_select_menu(var_opt, menu_info)
    var_name = []
    var_comment = []
    for val in selected_var:
        temp_val = []
        temp_val = re.split(r"[|]", val)
        var_name.append(temp_val[0])
        var_comment.append(temp_val[1])
    var_list = ''
    var_name = [elemento.strip() for elemento in var_name]
    var_comment = [elemento.strip() for elemento in var_comment]
    for i, name in enumerate(var_name):
        var_list = var_list + var_name[i] + '\t| ' + var_comment[i] + '\n'


    parameters_list = var_list
#    parameters_list = part_list + var_list
    parameters_name = list(set(var_name))
#    parameters_name = list(set(odd_par + var_name))
    # 
    head = '--EDICIÓN DE PARAMETROS--\n\n'
    info = f'Se han seleccionado las siguientes variables:\n\nName \t| Variable\n'# {ood_name} como candidatos de DM. ¿Qué masa desea establecer para ellas?'
    quest = '\n¿Qué desea hacer?'
    menu_info = head + info + parameters_list + quest
    optionsPar = ['Dejar los valores ya establecidos en el modelo', 'Ingresar valor(es) de forma manual', 'Usar valor(es) aleatorio(s) con una única salida', 'Hacer un barrido aleatorio para cada valor']

    randomPar =  menu(optionsPar, menu_info)

    Par_Dir = Project_Dir + '/Parameters'
    os.system(f'mkdir {Par_Dir}')

    timesDat = 1
    if randomPar == 0: ## No cambiar el archivo data.par
        create_data_files([],[],Par_Dir+'/data1.par')
    elif randomPar == 1: ## Ingresa 1 de manera manual los parametros
        parameters_values = getDataVal(parameters_name, False, 0, 0)
        create_data_files(parameters_name, parameters_values, Par_Dir+'/data1.par')
    elif randomPar == 2:
        rMin = []
        rMax = []
        for name in parameters_name:
            getRango = input(f'Entre que rango puede estar {name} (rmin,rmax): ')
            rmin, rmax = getRango.split(',')
            rmin = float(rmin)
            rmax = float(rmax)
            rMin.append(rmin)
            rMax.append(rmax)
        parameters_values = getDataVal(parameters_name,True, rMin, rMax)
        create_data_files(parameters_name,parameters_values, Par_Dir+'/data1.par')
    else:
        rMin = []
        rMax = []
        for name in parameters_name:
            getRango = input(f'Entre que rango puede estar {name} (rmin,rmax): ')
            rmin, rmax = getRango.split(',')
            rmin = float(rmin)
            rmax = float(rmax)
            rMin.append(rmin)
            rMax.append(rmax)
        timesDat = int(input('Ingrese tamaño del barrido: ')) 
        for i in range(1, timesDat+1):
            parameters_values = getDataVal(parameters_name,True, rMin, rMax)
            create_data_files(parameters_name, parameters_values, f'{Par_Dir}/data{i}.par')
        
    # Ejecutar ./main data.par y guardar los datos
    clear_screen()
    t_inicio = time.time()
    for j in range(1, timesDat+1):
        with open(Project_Dir+'/tempOut.txt', 'a') as tempfile:
            run_main = f'cd {Project_Dir} && ./main Parameters/data{j}.par'
            tempfile.write(subprocess.run([run_main], shell=True, capture_output=True, text=True).stdout)
    t_final = time.time()
    input('completado')
    input(t_final-t_inicio)

if __name__ == "__main__":
    main_micromegas("/home/harold/Documentos/GitHub/Amalgama")
