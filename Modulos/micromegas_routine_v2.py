#Librerias 
import os
import subprocess
import time
from shutil import copy
import re
from numpy import random
from tabulate import tabulate
from multiprocessing import cpu_count, Manager, Pool
from tqdm import tqdm

#Funciones propias
from .menu import clear_screen, multi_select_menu, menu
from .files import select_dir, select_dir_wth_keyword, find_files_wth_ext
from .mO_f import create_project, get_funct, set_funct, vars_Info, parNone, parManual, parRand, seedsGen
import concurrent.futures

#Posible libreria para paralelizar
#import concurrent.futures

menu_info_1 = 'Seleccione la sesió con la que quiere trabajar:'

info_sesion_dir_1 = '\nNo se encontró ningún directorio con los archivos requeridos para ejecutar micrOMEGAS.\n\nPresione ENTER para volver.'
info_sesion_dir_2 = '\nNo se encontraron los archivos necesarios para ejecutar micrOMEGAS.\n\nPresione ENTER para volver.'

menu_info_2 = 'Seleccione las funciones que desea que micrOMEGAS realice.'

info_make = '\n\n\nNo se ha podido crear el programa "main.c"'

info_var = 'Seleccione los parametros con los que desea trabajar.'

info_random_1 = '--EDICIÓN DE PARAMETROS--\n\nSe han seleccionado las siguientes variables:\n\n\t'
info_random_2 = ['Dejar los valores establecidos en el modelo.', 'Ingresar un valor para cada parámetro.', 'Usar un valor aleatorio para cada parámetro.', 'Usar valores aleatorios en un rago para cada parámetro.']
info_random_3 = 'Ingrese los nuevos valores.\n'
info_random_4 = '\nIngrese el rango de los valores\nEjemplo.\n\t> parameterName: min_val, max_val'
info_random_5 = '\n\t> Tamaño del barrido: '

error_random_1= '\nError. Ingrese datos válidos.'

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
    clear_screen()
    if not os.path.exists(f'{Project_Dir}/main'):
        input(info_make)
        return

#Obtener la información del archivo vars.mdl
    varName, varVal, varCom, varOpt = vars_Info(f'{Project_Dir}/work/models/vars1.mdl')



#Elejir que variables se van a cambiar
    varSelect = multi_select_menu(varOpt, info_var)
    delIndex = [i for i, element in enumerate(varOpt) if element not in varSelect]
    for index in sorted(delIndex, reverse=True):
        varName.pop(index)
        varVal.pop(index)
        varCom.pop(index)
        varOpt.pop(index)


#Elejir el tipo de edición de parametros
    randomOpt = menu(info_random_2, f'{info_random_1}'+'\n\t'.join(varOpt))


#Escritura de parámetros
    Results_Dir = f'{Project_Dir}/Results'
    resultFile = f'{Results_Dir}/results.txt'
    header = list(varName) + ['omega']
    os.system(f'mkdir {Results_Dir}')
    #Caso 1: Dejar los datos igual
    if randomOpt==0:
        data = parNone(Project_Dir, varName, varVal)
        with open(f'{resultFile}', 'a') as file:
            file.write(tabulate(data,headers=header, tablefmt='plain'))
    #Caso 2: Editar los datos manualmente
    if randomOpt==1:
        print(info_random_3)
        varVal = []
        for name in varName:
            varVal.append(float(input(f'> {name}: ')))
        data = parManual(Project_Dir, varName, varVal)
        with open(f'{resultFile}', 'a') as file:
            file.write(tabulate(data, headers=header, tablefmt='plain'))
    #Caso 3: Editar aleatoriamente una vez
    if randomOpt==2:
        varRange = []
        print(info_random_4)
        for name in varName:
            while True:
                try:
                    rmin, rmax = map(float, input(f'\t> {name}: ').split(','))
                    varRange.append([rmin, rmax])
                    break
                except ValueError:
                    print(error_random_1)
        data = parRand(Project_Dir, varName, varRange, seedsGen(1))
        with open(f'{resultFile}', 'a') as file:
            file.write(tabulate(data, headers=header, tablefmt='plain'))
    #Caso 4: Hacer un barrido de parámetros aleatorios
    if randomOpt==3:
        varRange = []
        print(info_random_4)
        for name in varName:
            while True:
                try:
                    rmin, rmax = map(float, input(f'\t> {name}: ').split(','))
                    varRange.append([rmin, rmax])
                    break
                except ValueError:
                    print(error_random_1)
        while True:
            try:
                randSize = int(input(info_random_5))
                break
            except ValueError:
                print(error_random_1)
        num_cores = max(cpu_count()-1,1)
        input(f'\nSe usarán {num_cores} nucleos de {max(cpu_count(),1)} dispibles.\nPresione ENTER para iniciar el barrido.')
        clear_screen()

        #Iniciar la paraleización
        data = []
        seeds = seedsGen(randSize)
        intsParallel = (Project_Dir, varName, varRange)
        with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:
            with tqdm(total=len(seeds)) as progress:
                futures = []
                for seed in seeds:
                    future = executor.submit(parRand, *intsParallel, seed)
                    future.add_done_callback(lambda p: progress.update())
                    futures.append(future)

            #futures = [executor.submit(parRand, *intsParallel, seed) for seed in seeds]
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    data.append(result)


        #Inicia la paralelización
#        intsParallel = [(Project_Dir, varName, varRange) for _ in range(randSize)]
#
#        print('Amalgama está ejecutando el barrido con parámetros aleatorios...')
#        with Pool(processes=num_cpus) as pool:
#            data = pool.starmap(parRand, intsParallel)

        with open(f'{resultFile}', 'a') as file:
            file.write(tabulate(data,headers=header, tablefmt='plain'))

#        input(data)
#        input('\nEjecución completa.')

