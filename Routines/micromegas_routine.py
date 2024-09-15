import os
from shutil import copy


from Modulos.menu import clear_screen
# from Modulos.menu import multi_select_menu
from Modulos.files import select_dir
from Modulos.files import select_dir_wth_keyword
from Modulos.files import find_files_wth_ext
from Modulos.files import code_name


Global_Dir = '/home/harold/Documents/Tesis/Programa'


# def micromegas_files_check(search_path):
#     number_ch_files = len(find_files_wth_ext(search_path, '.mdl'))
def create_micromegas_project(dir, sesion_dir, files):
    clear_screen()
    print('Creando Proyecto...\n')
    project_name = code_name('MO')
    os.system(f'cd {dir} && ./newProject {project_name}')
    project_dir = dir + '/' + project_name
    models_dir = project_dir + '/work/models'

    for file in files:
        file_dir = sesion_dir + '/' + file
        copy(file_dir, models_dir)

    input(f'\n\nSe ha creado correctamente el projecto {project_name}')
    return project_dir

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
            Project_Dir = create_micromegas_project(Micromegas_Dir, CH_Dir, mdl_files)
    input(Project_Dir)
    os.system(f'cd {Project_Dir} && make main=main.c && ./main data.par')
    input()
