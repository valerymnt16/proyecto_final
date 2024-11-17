import os
import json
import methods


def read_data(file_path):
    """
    Lee un archivo de texto para extraer una cuadrícula de palabras y una lista de palabras separadas por "---".

    Parámetros:
        file_path (str): Ruta al archivo de texto que contiene los datos de entrada.

    Retorno:
        tuple:
            - word_grid (list of lists): Lista de listas representando la cuadrícula de palabras.
            - words (list): Lista de palabras a buscar en la cuadrícula.
    Excepciones:
        Levanta una excepción si el archivo no existe o no contiene el separador "---".
    """
    with open(file_path, 'r') as file:
        content = file.read().strip().split('\n')

    separator_index = content.index('---')
    word_grid = [row.split() for row in content[:separator_index]]
    words = content[separator_index + 1:]

    return word_grid, words


def save_data(output_path, result):
    """
    Guarda los resultados en un archivo JSON.

    Parámetros:
        output_path (str): Ruta del archivo de salida donde se guardarán los resultados.
        result (dict): Diccionario con las palabras como claves y valores booleanos indicando si se encontraron.

    Retorno:
        str: Ruta absoluta del archivo JSON creado.

    Excepciones:
        Lanza una excepción si no se puede escribir en el archivo.
    """
    with open(output_path, 'w') as json_file:
        json.dump(result, json_file, indent=4)
    return os.path.abspath(output_path)


def main():
    """
    Función principal que coordina la lectura de datos, búsqueda de palabras y almacenamiento de resultados.

    Parámetros:
        Ninguno.

    Retorno:
        Ninguno, pero escribe un archivo JSON con los resultados de la búsqueda.
    """
    input_file = "input.txt"
    output_file = "status.json"

    try:
        word_grid, words = read_data(input_file)
        result = {}
        for word in words:
            result[word] = bool(methods.find_word(word_grid, word))
        report_path = save_data(output_file, result)
        print(f"Resultados guardados en: {report_path}")

    except Exception as e:
        print(f"Error: {e}")


main()