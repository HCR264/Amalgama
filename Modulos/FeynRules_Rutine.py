import os
import sys
import termios
import tty
import shutil
from datetime import datetime


def clear_screen():
    os.system('clear')


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


def print_menu(options, selected_indices, current_index, menu_info):
    clear_screen()
    print(menu_info)
    print('\n')
    for i, option in enumerate(options):
        preprefix = "> " if i == current_index else "  "
        prefix = "[X]" if i in selected_indices else "[ ]"
        print(f"{preprefix}{prefix}{option}")
    print('\n')
    print("Seleccionar: Space \t Finalizar: Enter")


def multi_select_menu(options, menu_info):
    selected_indices = set()
    current_index = 0

    while True:
        print_menu(options, selected_indices, current_index, menu_info)
        key = get_key()

        if key == '\x1b[A':
            current_index = (current_index - 1) % len(options)
        elif key == '\x1b[B':
            current_index = (current_index + 1) % len(options)
        elif key == ' ':
            if current_index in selected_indices:
                selected_indices.remove(current_index)
            else:
                selected_indices.add(current_index)
        elif key == '\r':
            return [options[i] for i in selected_indices]


def extract_lagrangians(model_path):
    with open(model_path, 'r') as file:
        lines = file.readlines()

    lagrangians_in_model = []
    capturing = False

    for line in lines:
        line = line.strip()
        if line == "(***Lagrangians***)":
            capturing = True
            continue
        elif line == "(***End***)":
            capturing = False
            break
        if capturing:
            cleaned_line = line.replace("(*", "").replace("*)", "").strip()
            if cleaned_line:
                lagrangians_in_model.append(cleaned_line)
    return lagrangians_in_model


def obtain_lagrangians(ModelsSelected):
    lagrangians = []
    for models in ModelsSelected:
        for lagrangian in extract_lagrangians(ModelsDir + '/' + models):
            lagrangians.append(lagrangian)
    return lagrangians


# EDITAR PLANTILLA
def create_script(Models, Lagrangians, Interfaces):
    global Current_Sesion_Dir
    global Current_Script_Name
    global Current_Sesion_Code
    with open(Plantilla_FeynRules_Dir, 'r') as file:
        lines = file.readlines()


    Models_Str = ", ".join(f'"{m_item}"' for m_item in Models)
    Lagrangians_Str = ", ".join(f'{l_item}' for l_item in Lagrangians)

    for i, line in enumerate(lines):
        if '$FeynRulesPath = SetDirectory[]' in line:
            lines[i] = f'$FeynRulesPath = SetDirectory["{FeynRulesDir}"]\n'
        if 'SetDirectory[ ]' in line:
            lines[i] = f'SetDirectory["{ModelsDir}"]\n'
        if 'LoadModel[]' in line:
            lines[i] = f'LoadModel[{Models_Str}]\n'
        if 'FeynmanRules[]' in line:
            lines[i] = f'FeynmanRules[{Lagrangians_Str}]\n'
        if '(*WriteCHOutput[]*)' in line:
            if 'CalcHep/CompHep' in Selected_Interfaces:
                lines[i] = f'WriteCHOutput[{Lagrangians_Str}]\n'
        if '(*WriteFeynArtsOutput[]*)' in line:
            if 'FeynArts/FormCalc' in Selected_Interfaces:
                lines[i] = f'WriteFeynArtsOutput[{Lagrangians_Str}]\n'
        if '(*WriteSHOutput[]*)' in line:
            if 'Sherpa' in Selected_Interfaces:
                lines[i] = f'WriteSHOutput[{Lagrangians_Str}]\n'
        if '(*WriteLaTeXOutput[]*)' in line:
            if 'TEX' in Selected_Interfaces:
                lines[i] = f'WriteLaTeXOutput[{Lagrangians_Str}]\n'
        if '(*WriteUFO[]*)' in line:
            if 'UFO' in Selected_Interfaces:
                lines[i] = f'WriteUFO[{Lagrangians_Str}]\n'
        if '(*WriteWOOutput*)' in line:
            if 'Whizard/Omega)' in Selected_Interfaces:
                lines[i] = f'WriteWOOutput[{Lagrangians_Str}]\n'

    code = datetime.now()
    Current_Sesion_Code = code.strftime('%Y%m%d%H%M%S')

    Current_Sesion_Dir = Sesions_Dir + f'/Sesion_{Current_Sesion_Code}'
    os.mkdir(Current_Sesion_Dir)
    Current_Script_Name = f'FeynRules_{Current_Sesion_Code}.m'

    with open(Current_Sesion_Dir + '/' + Current_Script_Name, 'w') as file:
        file.writelines(lines)

    run_mathematica_script()

    move_dirs()
    
    clear_screen()

    input(f'Finalizado. Los archivos se han guardado dentro de {Current_Sesion_Dir}')


def run_mathematica_script():
    clear_screen()
    print(f'Ejecutando {Current_Script_Name} ...\n')
    code = f'math -script {Current_Sesion_Dir}/{Current_Script_Name}'
    os.system(code)


def move_dirs():
    clear_screen()
    matches = []
    for element in os.listdir(ModelsDir):
        element_dir = ModelsDir + '/' + element
        if os.path.isdir(element_dir):
            matches.append(element_dir)

    for dir in matches:
        shutil.move(dir, Current_Sesion_Dir)


# FUNCIONES QUE ESTÁN EN OTRO ARCHIVO
def find_files_wth_ext(search_path, ext):
    find_files = []
    for file in os.listdir(search_path):
        if file.endswith('.fr'):
            find_files.append(file)
    return find_files


def FeynRules_Rutine_main():

    global GlobalDir
    global ModelsDir
    global FeynRulesDir
    global Plantilla_FeynRules_Dir
    global Selected_Interfaces
    global Sesions_Dir
    global Current_Sesion_Dir
    global Current_Script_Name

    Current_Sesion_Dir = ''
    Current_Script_Name = ''

    GlobalDir = '/home/harold/Documents/Tesis/Programa'
    ModelsDir = GlobalDir + '/Modelos'
    FeynRulesDir = GlobalDir + '/feynrules-current'
    Plantilla_FeynRules_Dir = GlobalDir + '/.Plantilla_FeynRules_Script/Plantilla_FeynRules_Script.m'
    Sesions_Dir = GlobalDir + '/Sesiones'

    Models_List = find_files_wth_ext(ModelsDir, '.fr')
    ModelSelected_Info = "Seleccione los modelos que quiere incluir en el Notebook de Mathematica:"
    Selected_Models = multi_select_menu(Models_List, ModelSelected_Info)

    Lagrangians_List = obtain_lagrangians(Selected_Models)

    Selected_Lagrangians_Menu_Info = "Seleccione los lagrangianos que quiere incluir en el Notebook de Mathematica:"
    Selected_Lagrangians = multi_select_menu(Lagrangians_List, Selected_Lagrangians_Menu_Info)

    Interfaces = ["CalcHep/CompHep", "FeynArts/FormCalc", "Sherpa", "TEX", "UFO", "Whizard/Omega"]
    Selected_Interfaces_Menu_Info = "Seleccione las interfaces en los que deseé que FeynRules exporte:"
    Selected_Interfaces =  multi_select_menu(Interfaces, Selected_Interfaces_Menu_Info)

    create_script(Selected_Models, Selected_Lagrangians, Selected_Interfaces)


if __name__ == '__main__':
    FeynRules_Rutine_main()
