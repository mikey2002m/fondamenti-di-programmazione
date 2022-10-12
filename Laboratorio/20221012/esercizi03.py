from typing import Any, Callable, List


# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')


################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return 'Ciao ' + name + 'Buona giornata!'


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    while string[0] == ' ':
        if string == ' ':
            return ''
        string = string[1:]
    while string[string.__len__() - 1] == ' ':
        if string == ' ':
            return ''
        string = string[:(string.__len__() - 1)]
    return string


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    bkp = string
    f = characters.__len__()
    i = 0
    l = []
    while i+f < string.__len__():
        if string[i:i+f] == characters:
            l.append(string[0:i])
            string = string[i+f:]
            i = 0
        i += 1
    if l.__len__() == 0:
        return [bkp]
    else:
        l.append(string)
    return l


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    f = find.__len__()
    i = 0
    while i + f < string.__len__():
        if string[i:i + f] == find:
            string = string[:i] + replace + string[i+f:]
            i += replace.__len__() + 1
        i += 1
    return string


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    offset *= -1 if decrypt else 1
    res = ''
    for c in string:
        if c != ' ':
            res += chr((((ord(c)-97)+offset)%26)+97)
        else:
            res += ' '
    return res


# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', 'P')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 17, False)
print_test(caesar_cypher, 'tzrf gzggf', 17, True)

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    res = 0
    for el in elements:
        res += el**2
    return res


# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    _max = elements[0]
    for el in elements:
        if el > _max:
            _max = el
    return _max


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    for i, el1 in enumerate(elements):
        if i+1 < elements.__len__():
            for j, el2 in enumerate(elements[i+1:]):
                if el1 == el2:
                    elements.pop(i+j+1)
    return elements


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    res = []
    for el in elements:
        res = [el] + res
    return res


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e ritorna una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    res = []
    for el in elements:
        if isinstance(el, list):
            res.extend(flatten_list(el))
        else:
            res.append(el)
    return res


# Test funzioni
print_test(sum_squares, [1, 2, 3])
print_test(max_element, [1, 2, 3, -1, -2])
print_test(remove_duplicates, [1, 2, 3, 2, 3])
print_test(reverse_list, [1, 2, 3])
print_test(flatten_list, [1, [2, 3]])
