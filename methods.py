def find_word(ls, word):
    """
    Busca una palabra en la sopa de letras (matriz de caracteres) en diferentes direcciones: horizontal, vertical y diagonal.

    Parámetros:
    (ls) (list of list-str): Una lista de listas que representa la sopa de letras, donde cada sublista es una fila de la sopa.
    (word) (str): La palabra que se debe buscar dentro de la sopa de letras.

    Retorno:
    bool: True si la palabra se encuentra en la sopa de letras (horizontalmente, verticalmente o diagonalmente), False si no se encuentra en ninguna dirección.
    """
    answer = False
    # Horizontal (izq-der y der-izq)
    if not answer:
        for row in ls:
            str_word = ''.join(row)
            if word in str_word or word in str_word[::-1]:
                answer = True

    # Vertical (arriba-abajo y abajo-arriba)
    if not answer:
        for col in range(len(ls[0])):
            aux = []
            for row in range(len(ls)):
                aux.append(ls[row][col])
            str_word = ''.join(aux)
            if word in str_word or word in str_word[::-1]:
                answer = True

    # Diagonal (izq-der y der-izq)
    if not answer:
        for d in range(-len(ls) + 1, len(ls[0])):
            aux = []
            for i in range(len(ls)):
                j = i + d
                if 0 <= j < len(ls[0]):
                    aux.append(ls[i][j])
            if aux:
                str_word = ''.join(aux)
                if word in str_word or word in str_word[::-1]:
                    answer = True

        for d in range(-len(ls) + 1, len(ls[0])):
            aux = []
            for i in range(len(ls)):
                j = len(ls[0]) - 1 - i + d
                if 0 <= j < len(ls[0]):
                    aux.append(ls[i][j])
            if aux:
                str_word = ''.join(aux)
                if word in str_word or word in str_word[::-1]:
                    answer = True

    return answer

def find_words(ls, words):
    """
    Verifica si todas las palabras de una lista están presentes en la sopa de letras.

    Parámetros:
    (ls) (list of list-str): Una lista de listas que representa la sopa de letras.
    (words) (list-str): Una lista de palabras que se deben buscar dentro de la sopa de letras.

    Retorno:
    bool: True si todas las palabras están presentes en la sopa de letras,
          False si alguna palabra no se encuentra.
    """
    answer = False
    count_words = 0
    for word in words:
        if find_word(ls, word):
            count_words += 1
    if count_words == len(words):
        answer = True

    return answer


def words_report(ls, words):
    """
    Genera un reporte de las palabras encontradas o no encontradas en la sopa de letras.

    Parámetros:
    (ls) (list of list-str): Una lista de listas que representa la sopa de letras.
    words (list-str): Una lista de palabras que se deben buscar dentro de la sopa de letras.

    Retorno:
    words_dic: Un diccionario donde las llaves son las palabras de la lista (words), y los
          valores son booleanos (True si la palabra se encuentra, False si no).
    """
    words_dic = {}
    for word in words:
        words_dic[word] = find_word(ls, word)

    return words_dic