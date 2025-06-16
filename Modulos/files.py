import os
from .menu import menu
from datetime import datetime
from shutil import move


# Obtener el directorio de trabajo
def get_dir():
    dir = os.getcwd()
    return dir


# Seleccionar un directorio
def select_dir(Search_Dir, Info):
    Dirs = os.listdir(Search_Dir)
    Dirs.sort()
    Num_Dir_Selected = menu(Dirs, Info)
    Dir_Selected = Dirs[Num_Dir_Selected]
    return Dir_Selected


# Buscar un directorio con una keyword
def select_dir_wth_keyword(Search_Dir, Keyword):
    find_dir = ""
    for root, dirs, files in os.walk(Search_Dir):
        for dir in dirs:
            if Keyword.lower() in dir.lower():
                find_dir = dir 
    return find_dir

# Buscar un archivo con una keyword
def find_files_wth_keyword(Search_Dir, Keyword):
    find_files = []
    for root, dirs, files in os.walk(Search_Dir):
        for file in files:
            if Keyword.lower() in file.lower():
                find_files.append(os.path.join(root,file)) 
    return find_files


# Encontrar archivos con extensión
def find_files_wth_ext(search_path, ext):
    find_files = []
    for file in os.listdir(search_path):
        if file.endswith(ext):
            find_files.append(file)
    return find_files


# Codigo de archivo
def code_name(key):
    code = datetime.now()
    sesion_name = key + '_Sesion_' + code.strftime('%Y%m%d%H%M%S')
    return sesion_name


# Mover archivos
def move_files(dir_src, dir_dst, file_name): 
   input()

# Escribir script de Mathematica para graficar
def plotScript(dataDir, dataCols):
    with open(
        os.path.dirname(dataDir) + '/plotScript.m', 'w') as file:
        file.write(f'"data = Import[{dataDir}", "Table"][[All,{dataCols}]];\n')
        file.write('interpolData = Interpolation[data, InterpolationOrder -> 1];\n')
        file.write('plot =ContourPlot[interpolData[x, y], {x, xmin, xmax}, {y, logYmin, logYmax}, Contours -> {0.12}, ContourShading -> Automatic, ColorFunction -> "Rainbow", FrameLabel -> {"m_χ [GeV]", "log₁₀(σ_eff)"}, PlotRange -> All, PlotPoints -> 100, Mesh -> None, Frame -> True, GridLines -> None]')
