#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "NME"
cognome     = "CONOME"
matricola   = "MATRCOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla FINE di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# DEBUG=True vi attiva anche lo STACK TRACE degli errori per sapere il numero
# di linea di program.py che genera l'errore.
################################################################################


# %% ----------------------------------- EX.1 ----------------------------------#

"""
Ex1: 6 punti
Si definisca la funzione ex1(triangles) che prende in input una lista
di triple di numeri positivi ed elimina dalla lista tutte le triple
che non possono essere i lati di un triangolo rettangolo. Ogni numero della
tripla puo' essere o cateto o ipotenusa e non vi è alcun ordine
prestabilito.  La funzione deve ritornare il numero di triple
eliminate dalla lista triangles. La lista triangles deve risultare
modificata in-place alla fine dell'esecuzione di ex1. Per valutare se un
triangolo è rettangolo si può usare il teorema di Pitagora, per cui la
somma dei quadrati costruiti sui cateti deve essere uguale al quadrato
costruito sull'ipotenusa.
Per i confronti, si usi la funzione di arrotondamento round(x,3).

Esempio: se triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         la funzione ex1(triangles) resituisce il valore 3 e modifica la lista
         in modo che
            triangles = [(3, 4, 5), (12, 36.05551, 34)].

Infatti, considerando il risultato atteso triangles = [(3, 4, 5), (12, 36.05551, 34)]
vale:

| tripla             | check is True                                  |
| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""


def ex1(triangles: list):
    start_n = len(triangles)
    for el in triangles.copy():
        is_rett = False
        for j in range(3):
            if el[j] < el[(j+1)%3] + el[(j+2)%3] and round(el[j]**2, 3) == round(el[(j+1)%3]**2 + el[(j+2)%3]**2, 3):
                is_rett = True
                break
        if not is_rett:
            triangles.remove(el)
    return start_n - len(triangles)


###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
