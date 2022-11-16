import testlib
import program

#################################################################################
################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST ######
################### E' VIETATO USARLE NELLA SOLUZIONE                      ######
################### THESE FUNCTIONS BELOW ARE USED IN TESTS                ######
################### IT'S FORBIDDEN TO USE THEM IN YOUR PROGRAM             ######
#################################################################################

def error_message(res, expected, msg=None):
    bold = '\033[1m'
    bolde = '\033[0m'

    msg_std = f"{bold}Return value incorrect | Valore NON corretto! [NOT OK]{bolde}\n YOUR ANSWER | TUO RISULTATO = {res} \n    EXPECTED | ATTESO        = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print(bold+'*'*50+bolde)
    print(msg)
    print(bold+'*'*50+bolde)


def do_test_es1(tabella, colonne, elimina, expected):
    res = program.ex1(tabella, colonne, elimina)
    testlib.check(tabella, expected)
    testlib.check(res, len(elimina))
    return 2

def test_es1_1():
    r'''
        Tabella EX1 caso 1
    '''

    tabella = [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
        ]
    colonne=['Nome', 'Cognome']
    elimina=['Telefono']
    expected= [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Indirizzo': 'via degli Angeli 17' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Indirizzo': 'via degli Angeli 14' },
        ]
    return do_test_es1(tabella, colonne, elimina, expected)

def test_es1_2():
    r'''
        Tabella EX1 caso 2
    '''
    tabella = [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
        ]
    colonne=['Telefono', 'Nome', 'Indirizzo']
    elimina=[]
    expected= [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
        ]
    return do_test_es1(tabella, colonne, elimina, expected)

def test_es1_3():
    r'''
        Tabella EX1 caso 3
    '''
    tabella = [   
            { 'Nome': 'Andrea',  'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni',  'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni',  'Cognome': 'Paperino', 'Telefono': 137487469, 'Indirizzo': 'via degli Angeli 17' },
            { 'Nome': 'Paolino', 'Cognome': 'Paperino', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 313' },
        ]
    colonne=['Cognome', 'Telefono', 'Indirizzo']
    elimina=['Nome', 'Cognome']
    expected= [   
            { 'Telefono': 137487468, 'Indirizzo': 'via del Pero 313' },
            { 'Telefono': 137487469, 'Indirizzo': 'via degli Angeli 17' },
            { 'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
        ]
    return do_test_es1(tabella, colonne, elimina, expected)
#################################################################################

# ----------------------------------- EX.2 ----------------------------------- #
def do_ex2_tests(D, D_rm, to_remove, expected, score=2, total=2):
    res = program.ex2(D, to_remove)
    if res == expected:
        score = 1
    else:
        error_message(res, expected, "> LEGGIMI: Il dizionario tornato non e' corretto.\n")
        score = 0

    if D == D_rm:
        score += 1
    else:
        error_message(D, D_rm, "> LEGGIMI: Il dizionario di ritorno e' corretto, ma gli interi nelle liste dentro D non sono stati tolti in maniera distruttiva\n\n")
    return score

def test_ex2_1():
    r'''
    Dizionario inverso con ripetizioni CASO 1
    '''
    D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}
    D_rm = {2: [6]}
    to_remove = [4, 3, 2, 5]
    expected = {6: [2], 4: [2, 1, 1, 1], 2: [1], 3: [2, 1], 5: [2]}
    return do_ex2_tests(D, D_rm, to_remove, expected)

def test_ex2_2():
    r'''
    Dizionario inverso con ripetizioni CASO 2
    '''
    D = {0: [2, 2, 3, 3],
         10: [0],
         5: [5],
         6: [5, 1, 4, 5, 0, 3, 1, 3, 2, 3],
         9: [0],
         3: [4],
         2: [4, 3, 2, 4, 5]}

    D_rm = {0: [2, 2], 6: [1, 1, 2], 2: [2]}
    to_remove = [4, 3, 0, 5]
    expected = {4: [6, 2, 2, 3], 2: [6, 2, 0, 0], 0: [10, 6, 9], 1: [6, 6], 3: [6, 6, 6, 2, 0, 0], 5: [6, 6, 2, 5]}
    return do_ex2_tests(D, D_rm, to_remove, expected)

def test_ex2_3():
    r'''
    Dizionario inverso con ripetizioni CASO 3
    '''

    D = {0: [1],
         1: [2, 0, 0, 0, 0, 1, 2, 0, 1, 2, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
         3: [2, 1, 2, 2, 1, 0, 1, 0, 1],
         7: [0, 1, 2, 1, 0, 1, 2, 1, 1, 0, 2, 2, 2, 2, 0, 2, 0],
         6: [0, 0, 2, 1, 2, 0, 1, 0, 1, 0, 2, 1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0],
         4: [1, 1, 0, 2, 0, 1, 1, 0, 0, 2, 1, 1, 1, 2],
         2: [1, 2],
         5: [0, 1, 2]}
    D_rm = {}
    expected = {2: [6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 2, 1, 1, 1, 3, 3, 3, 5, 7, 7, 7, 7, 7, 7, 7], 0: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 5, 7, 7, 7, 7, 7], 1: [6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 4, 4, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 5, 7, 7, 7, 7, 7]}
    to_remove = [2, 1, 0]
    return do_ex2_tests(D, D_rm, to_remove, expected)

###################################################################################

def test_nome_cognome_matricola():
    assert program.matricola != 'MATRICOLA', "Inserisci la tua matricola all'inizio del file"
    assert program.cognome   != 'COGNOME',   "Inserisci il tuo cognome all'inizio del file"
    assert program.nome      != 'NOME',      "Inserisci il tuo nome all'inizio del file"

###################################################################################

tests = [
    # PER DISATTIVARE ALCUNI TEST BASTA COMMENTARE LE RIGHE CHE SEGUONO
    test_es1_1, test_es1_2, test_es1_3,      # tabella
    test_ex2_1, test_ex2_2, test_ex2_3,      # Dizionario inverso
    test_nome_cognome_matricola,
    ]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

###############################################################################
