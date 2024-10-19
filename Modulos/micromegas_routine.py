import os
from shutil import copy


from menu import clear_screen
# from Modulos.menu import multi_select_menu
from files import select_dir
from files import select_dir_wth_keyword
from files import find_files_wth_ext
from files import code_name
from menu import multi_select_menu


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

    input(f'\n\nSe ha creado correctamente el projecto {project_name}')
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
    os.system(f'cd {Project_Dir} && make main=main.c')
    clear_screen()


    functions = extract_functions(Project_Dir + '/main.c')
    menu_info = '¿Qué funciones desea realizar en micrOMEGAS?'
    selected_functions = multi_select_menu(functions, menu_info)
    input(selected_functions)
    clear_screen()
    set_functions(Project_Dir + '/main.c', selected_functions)
    input('main creado')

    os.system(f'cd {Project_Dir} && ./main data.par')

if __name__ == "__main__": 
    main_micromegas("/home/harold/Documents/GitHub/Amalgama")
