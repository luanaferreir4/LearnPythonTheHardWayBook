def break_words(stuff):
    """Esta função irá dividir palavras para nós."""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """Ordenar as palavras."""
    return sorted(words)


def print_first_word(words):
    """Imprima a primeira palavra."""
    word = words.pop(0)
    return word


def print_last_word(words):
    """Imprima a última palavra."""
    word = words.pop(-1)
    return word


def sort_sentence(sentence):
    """Ordena a frase."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Imprima primeira e última palavra da frase."""
    words = break_words(sentence)
    first = print_first_word(words)
    last = print_last_word(words)
    return first, last


def print_first_and_last_sorted(sentence):
    """Ordene a frase e imprima a primeira e a última palavra da frase."""
    sorted_sentence = sort_sentence(sentence)
    first_sorted = print_first_word(sorted_sentence)
    last_sorted = print_last_word(sorted_sentence)
    return first_sorted, last_sorted

# help(ex25) => mostra as Docstrings escritas por nós. (strings de documentação)
# help(ex25.break_words) => mostra o escrito (Docstrings) na função direcionada.
#
#
# Abrir no terminal e fazer assim sem precisar usar ex25. antes de executar:
#
# python
# from ex25 import * = do arquivo ex25 importar tudo diretamente no arquivo.
# sentence = "All good things come to those who wait."
# print_first_word(sentence) # pode-se executar dessa forma.
#
