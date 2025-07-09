import time

from .files import find_files_wth_keyword, select_dir, plotScript
from .menu import menu, clear_screen
import os
import subprocess
import sys

#Información de menús
menu_info_1 = 'Seleccione el archivo que desea graficar'

def main_plot(micromegas_dir):
#Buscar los archivos results_XXXXXX.txt
    result_files = find_files_wth_keyword(micromegas_dir, 'results')
    data_file = result_files[menu(result_files,menu_info_1)]

# Detectar los encabezados del archivo
    with open(data_file) as file:
        info = file.readline().split()

# Establecer los ejes y el parámetro de contorno
    x_column = menu(info,'Seleccione quien actuará como eje "x".')+1
    y_column = menu(info,'Seleccione quien actuará como eje "y".')+1
    contour_column = menu(info, 'Seleccione quien actuará como contorno.')+1

# Establecer el directorio y nombre del script
    plot_file_dir = os.path.dirname(data_file) + '/plotScript.m'

# Crear el script y ejecutarlo
    with open(plot_file_dir, 'w') as file:
        file.write(f'data = Import["{data_file}", "Table"][[All,{{{x_column},{y_column},{contour_column}}}]];\n')
        file.write('data = Rest[data];\n')
        file.write('interpolData = Interpolation[data, InterpolationOrder -> 1];\n')
        file.write(f'plot = ContourPlot[interpolData[x,y], {{x,{input('Especifica x_min: ')},{input("Especifica x_max: ")}}}, {{y,{input("Especifica y_min: ")},{input("Especifica y_max: ")}}}, Contours -> {{{input("Especifica la condición de contorno: ")}}}, ContourShading -> True, ColorFunction -> (Blend[{{White, Green, Gray}}, #] &), ScalingFunctions -> {{"Linear", "Log"}}, PlotRange -> All, PlotLegends -> Automatic] \n')
        file.write('Export["Plot.pdf",plot]\n')

    clear_screen()
    print(f'Ejecutando {plot_file_dir} ...\n')
    code = f'cd {os.path.dirname(data_file)} && math -script plotScript.m'
    os.system(code)

# Mostrar gráfica
    print('Mostrando gráfica...')
    time.sleep(2)
    subprocess.Popen(['xdg-open', os.path.dirname(data_file) + '/Plot.pdf'])

    #time.sleep(1)
    input()