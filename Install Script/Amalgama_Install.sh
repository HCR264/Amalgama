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

MCheck="[ "$CGR"\u2713"$CNC" ]" # Palomita
MCross="[ "$CRE"\u2717"$CNC" ]" # Tache
MTime="[ "$CYE"\u23F3"$CNC"]" # Reloj


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
  echo "Este script no debe ejecutarse como superusuario."
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

# OBTENER DIRECTORIO
actual_dir=$PWD

# VERIFICAR LA DISTRIBUCIÓN DE LINUX
logo "Identificando sistema operativo..."
sleep 2

if [ -f /etc/os-release ]; then
  . /etc/os-release
  DISTRO=$ID
  logo "Hecho"
  printf "%s%sSistema Operativo:%s %s\n\n" "${BLD}" "${CYE}" "${CNC}" "$DISTRO"
  if [[ "$DISTRO" != "arch" && "$DISTRO" != "ubuntu" && "$DISTRO" != "fedora" ]]; then
    printf "%sEste script solo funciona en Arch, Fedora o Ubuntu.\n\n" "${CRE}"
    exit 1
  fi
  sleep 2
else
  logo "Error"
  printf "%sNo se pudo identificar el sistema operativo."
  exit 1
fi

# Verificar programas instalados
logo "Verificando que los programas requeridos/lenguajes/módulos estén instalados..."
sleep 2 

paquetes_privativos=(mathematica)

if [ "$DISTRO" == "ubuntu" ]; then
  paquetes_libres=(gcc gfortran git python3)
  librerias=(python3-tqdm python3-tabulate python3-numpy)
else
  paquetes_libres=(gcc gfortran git python)
  librerias=(python-tqdm python-tabulate python-numpy)
fi

is_installed() {
  command -v "$1" &> /dev/null
}

install() {
  case "$DISTRO" in
    "arch") 
      sudo pacman -S "$1" --noconfirm >/dev/null
      ;;
    "ubuntu")
      sudo apt-get update >/dev/null 
      sudo apt-get install -y "$1" >/dev/null
      ;;
    "fedora")
      sudo dnf install -y "$1" >/dev/null
      ;;
  esac
}

for paquete in "${paquetes_libres[@]}"; do
  if ! is_installed "$paquete"; then
    printf "%b %s no está instalado." "$MCross" "$paquete"
    sleep 3

    printf "\033[2K\r%b %s se está intentando instalar." "$MTime" "$paquete"
    sleep 1
    printf "\033[2K\r%b " "$MTime"
    install "$paquete"

    if is_installed "$paquete"; then
      printf "\033[1A\033[2K\r%b %s está instalado.\n" "$MCheck" "$paquete"
    else
      printf "\033[1A\033[2K\r%b %s no se ha podido instalar.\n\n%sInstalación interrumpida.%s" "$MCross" "$paquete" "${CRE}" "${CNC}"
      exit 1
    fi
  else
    printf "%b %s está instalado.\n" "$MCheck" "$paquete"
  fi
  sleep 1
done

# Verificar si las librerías de Python están instaladas
is_library_installed() {
    case "$DISTRO" in 
        "ubuntu")
            python3 -c "import $1" &> /dev/null
            ;;
        "arch")
            python -c "import $1" &> /dev/null
            ;;
        "fedora")
            python -c "import $1" &> /dev/null
            ;;
        esac
}

for libreria in "${librerias[@]}"; do
    if ! is_library_installed "$libreria"; then
        printf "%b %s no está instalado." "$MCross" "$libreria"
        sleep 3

        printf "\033[2K\r%b %s se está intentando instalar." "$MTime" "$libreria"
        sleep 1
        printf "\033[2K\r%b " "$MTime"
        install "$libreria"

        if is_library_installed "$libreria"; then
            printf "\033[1A\033[2K\r%b %s está instalado.\n" "$MCheck" "$libreria"
        else
            printf "\033[1A\033[2K\r%b %s no se ha podido instalar.\n\n%sInstalación interrumpida.%s" "$MCross" "$libreria" "${CRE}" "${CNC}"
        exit 1
        fi
    else
        printf "%b %s está instalado.\n" "$MCheck" "$paquete"
    fi
    sleep 1
done


for paquete in "${paquetes_privativos[@]}"; do
  if is_installed "$paquete"; then
    printf "%b %s está instalado.\n" "$MCheck" "$paquete"
  else
    printf "%b %s no está instalado. %s%sAquiera una licencia oficial.%s\n\n%sInstalación interrumpida.\n" "$MCross" "$paquete" "${CRE}" "${BLD}" "${CNC}" "${CRE}"
    exit 1
  fi
  sleep 1
done

# DESCARGAR REPOSITORIO DE GITHUB 
logo "Copiando repositorio de GitHub."

command git clone "https://github.com/HCR264/Amalgama"
sleep 3

# INSTALAR MICROMEGAS
logo "Instalando micrOMEGAS..."
sleep 3
command cd Amalgama
command wget https://zenodo.org/records/13376690/files/micromegas_6.1.15.tgz
command tar -zxvf micromegas_6.1.15.tgz
command cd micromegas_6.1.15/
command make
sleep 3

logo "Finalizado."

exit 1
