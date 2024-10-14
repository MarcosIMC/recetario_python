import os
from os import remove
from pathlib import Path
from platform import system

from unicodedata import category

from dia6.edition_fichero import archivo

ruta = Path('./Recetas')
num_recetas = 0
selection = 0

def clear_screen():
    system('clear')

def welcome():
    global num_recetas
    for txt in Path(ruta).glob('**/*.txt'):
        num_recetas += 1

    return (f"Bienvenido al recetario, la ruta de las recetas están en {ruta} y\n"
            f"el número de recetas es: {num_recetas}")

def show_menu():
    return ("[1] - Leer receta\n"
            "[2] - Crear receta\n"
            "[3] - Crear categoría\n"
            "[4] - Eliminar receta\n"
            "[5] - Eliminar categoría\n"
            "[6] - Finalizar programa\n")

def select_category():
    category_name = input(f"Seleccione una categoría: \n"
                                f"{os.listdir(ruta)}")
    return category_name

def show_recetas(category_name):
    path = Path(ruta, category_name)

    for txt in Path(path).glob('*.txt'):
        print(txt)
    receta_name = input(f"Seleccione una receta: \n")
    return receta_name

def read_receta(receta_name, category_name):
    file = Path(ruta, category_name, receta_name)
    print(file)
    text = open(file)
    print(text.read())
    text.close()

def create_receta(receta_name, category_name, text_receta):
    receta_name = receta_name+'.txt'
    path = Path(ruta, category_name, receta_name)
    archivo = open(path, "w")
    archivo.write(text_receta)
    archivo.close()

def create_category(category_name):
    path = Path(ruta, category_name)
    os.mkdir(path)

def delete_receta(receta_name, category_name):
    path = Path(ruta, category_name, receta_name)
    remove(path)

def delete_category(category_name):
    path = Path(ruta, category_name)
    os.rmdir(path)

print(welcome())
while selection != 6:
    print(show_menu())
    selection = int(input("Selecciona una opción..."))

    match selection:
        case 1:
            category = select_category()
            receta = show_recetas(category)
            read_receta(receta, category)
        case 2:
            category = select_category()
            name_receta = input("Escribe el nombre de la receta: ")
            text_receta = input("Escribe el texto de la receta: ")
            create_receta(name_receta, category, text_receta)
        case 3:
            category_name = input("Nombre de la nueva categoría: ")
            create_category(category_name)
        case 4:
            category = select_category()
            receta = show_recetas(category)
            delete_receta(receta, category)
        case 5:
            category = select_category()
            delete_category(category)
        case 6:
            break