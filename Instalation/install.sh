#!/usr/bin/env bash
#
#  __    _       __    _     __     __    _       __         ___   _    
# / /\  | |\/|  / /\  | |   / /`_  / /\  | |\/|  / /\   __  | |_) \ \_/ 
#/_/--\ |_|  | /_/--\ |_|__ \_\_/ /_/--\ |_|  | /_/--\ (_() |_|    |_|
#
# Script para instalar Amalgama.py
# Author: Harold Cruz Ramirez
# Año: 2024
# URL: https://github.com/HCR264/Amalgama

# Definir colores
CRE=$(tput setaf 1) # Rojo
CGR=$(tput setaf 2) # Verde
CYE=$(tput setaf 3) # Amarillo
CBL=$(tput setaf 4) # Azul
CCY=$(tput setaf 6) # Cyan
CMG=$(tput setaf 5) # Magenta
BLD=$(tput bold) # Negrita
CNC=$(tput sgr0) # Reiniciar 

MCheck="["$CGR"\u2713"$CNC"]"
MCross="["$CRE"\u2717"$CNC"]"


# LOGO
logo () {
  clear
  local text="${1:?}"
  echo -en $CYE '
    __    _       __    _     __     __    _       __         ___   _    
   / /\  | |\/|  / /\  | |   / /`_  / /\  | |\/|  / /\   __  | |_) \ \_/
  /_/--\ |_|  | /_/--\ |_|__ \_\_/ /_/--\ |_|  | /_/--\ (_() |_|    |_|\n'

  echo -en $BLD $CCY 'Autor: Harold Cruz Ramirez.\n\n'
  printf '%s%s[ %s%s%s %s%s]%s
  \n' "${BLD}" "${CRE}" "${CNC}" "${CYE}" "${text}" "${BLD}" "${CRE}" "${CNC}"
}

# VERIFICAR SI ES SUPERUSUARIO
if [ $(whoami) = 'root' ]; then
  echo "Este script no debe ejecutarse como super usuario."
  exit 1
fi

# BIENVENIDA

logo "Bienvenido al instalador de Amalgama"

printf "%sEste script se encargará de copiar mi repositorio de GitHub donde se encuentra Amalgama, así como verificar que todos los programas, lenguajes y/o módulos están instalados en tu ordenador.\n\n%s" "${CRE}" "${CNC}"

while true; do
  read -rp "¿Desea continuar? [y/N]: " yn
  case $yn in
    [Yy]* ) break ;;
    [Nn]* ) exit ;;
    * ) printf "Error. Escriba 'y' o 'n'\n\n" ;;
  esac
done

# Verificar programas instalados
logo "Verificando que los programas requeridos/lenguajes/módulos estén instalados..."
sleep 2 

paquetes=(mathematica python gcc gfortran git error_prueba)

is_installed() {
  command -v "$1" &> /dev/null
}

for paquete in "${paquetes[@]}"; do
  if is_installed "$paquete"; then
    printf "%b %s está instalado.\n" "$MCheck" "$paquete"
  else
    printf "%b %s no está instalado.\n" "$MCross" "$paquete"
  fi
  sleep 1
done
