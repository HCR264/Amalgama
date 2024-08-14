import os
import sys
import tty
import termios


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


def print_multi_select_menu(options, selected_indices, current_index, menu_info):
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
        print_multi_select_menu(options, selected_indices, current_index, menu_info)
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


def print_menu(options, selected_index, menu_info):
    clear_screen()
    print(menu_info)
    print('\n')
    for i, option in enumerate(options):
        prefix = "> " if i == selected_index else "  "
        print(f"{prefix}{option}")


def menu(options, menu_info):
    selected_index = 0
    while True:
        print_menu(options, selected_index, menu_info)
        key = get_key()

        if key == '\x1b[A':
            selected_index = (selected_index - 1) % len(options)
        elif key == '\x1b[B':
            selected_index = (selected_index + 1) % len(options)
        elif key == '\r':
            return selected_index
