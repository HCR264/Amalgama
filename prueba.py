import os
import concurrent.futures

from multiprocessing import cpu_count

from Modulos.mO_f import vars_Info
from Modulos.menu import multi_select_menu
from Modulos.mO_f import parRand, seedsGen

Project_Dir = '/home/harold/Documentos/Repositorios/Proyectos/Amalgama/micromegas_6.1.15/MO_Sesion_20250123211914'

varName, varVal, varCom, varOpt = vars_Info(f'{Project_Dir}/work/models/vars1.mdl')
varSelect = multi_select_menu(varOpt, 'Seleccione parámetros.')
delIndex = [i for i, element in enumerate(varOpt) if element not in varSelect]
for index in sorted(delIndex, reverse=True):
    varName.pop(index)
    varVal.pop(index)
    varCom.pop(index)
    varOpt.pop(index)

Results_Dir = f'{Project_Dir}/Results'
resultFile = f'{Results_Dir}/results.txt'
header = list(varName) + ['omega']
#os.system(f'mkdir {Results_Dir}')

varRange = []
print('\nIngrese el rango de los valores.')
for name in varName:
    while True:
        try:
            rmin, rmax = map(float, input(f'\t> {name}: ').split(','))
            varRange.append([rmin,rmax])
            break
        except ValueError:
            print('\nIngrese datos válidos.')
while True:
    try:
        randSize = int(input('\nBarrido: '))
        break
    except ValueError:
        print('\nIngrese datos válidos.')

#Semillas precomputadas
seeds = seedsGen(randSize)
input(seeds)

num_cores = max(cpu_count()//2, 1)
input(f'\nUsando {num_cores} nucleos.')

intsParallel = (Project_Dir, varName, varRange)
with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:
    futures = [executor.submit(parRand, *intsParallel, seed) for seed in seeds]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

input(futures)
