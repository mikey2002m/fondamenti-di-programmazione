# -*- coding: utf-8 -*-
import testlib
import os
import sys

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*'*50)
    print(msg)

def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0

###############################################################################


# ----------------------------------- EX.1 ----------------------------------- #

def do_ex1_tests(triangles, expected):
    val = len(triangles) - len(expected)
    res = program.ex1(triangles)
    
    testlib.check(type(res), type(val), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")

    if triangles != expected:
        print(f'''{'*'*50}\n[ERROR] The list triangles should be modified in {expected} instead of {triangles}.\n'''
              f'''[ERROR] La lista triangles dovrebbe essere modificata in {expected} invece che {triangles}.\n{'*'*50}''')
        return 0
    if res != val:
        print(f'''{'*'*50}\n[ERROR] The expected removed element be {expected} instead of {triangles}.\n'''
              f'''[ERROR] In numero di elementi rimosse deve essere {expected} invece che {triangles}.\n{'*'*50}''')
        return 0
    return 2


def test_ex1_1():
    '''
    triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = [(3, 4, 5), (12, 36.05551, 34)]
    '''
    triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = [(3, 4, 5), (12, 36.05551, 34)]
    return do_ex1_tests(triangles, expected)

def test_ex1_2():
    '''
    triangles = [(3, 4, 6), (11, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = []
    '''
    triangles = [(3, 4, 6), (11, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = []
    return do_ex1_tests(triangles, expected)

def test_ex1_3():
    '''
    triangles = [(6.0208, 4.0, 4.5),
             (5.5, 8.74586, 6.8),
             (12.8, 10.2, 16.3704),
             (2.3, 8.51645, 8.2),
             (7.9, 10.29417, 6),
             (12.5873, 8.8, 9.0)]
    expected = [(6.0208, 4.0, 4.5), (5.5, 8.74586, 6.8), (2.3, 8.51645, 8.2), (12.5873, 8.8, 9.0)]
    '''
    triangles = [(6.0208, 4.0, 4.5),
             (5.5, 8.74586, 6.8),
             (12.8, 10.2, 16.3704),
             (2.3, 8.51645, 8.2),
             (7.9, 10.29417, 6),
             (12.5873, 8.8, 9.0)]
    expected = [(6.0208, 4.0, 4.5), (5.5, 8.74586, 6.8), (2.3, 8.51645, 8.2), (12.5873, 8.8, 9.0)]
    return do_ex1_tests(triangles, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1,  test_ex1_2, test_ex1_3,            # lista triangoli
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################
