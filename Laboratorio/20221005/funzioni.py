# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la
# radice cubica, e la ritorna.
def curt(n: float):
    return n**(1/3)


print(curt(32.33e12))

# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e ritorna la maggiore.
# Modificare poi la funzione per ritornare entrambi i valori.


def quadratica(a: float, b: float, c: float):
    delta = (b**2)-(4*a*c)
    if delta < 0:
        return -999
    r1 = (-b + ((delta)**(1/2)))/(2*a)
    r2 = (-b - ((delta)**(1/2)))/(2*a)
    return r1, r2


print(quadratica(1, 0, -4))


# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e le ritorna entrambe.

# Scrivere una funzione che prende come input cinque numeri e ritorna la somma
# dei numeri pari meno quella dei numeri dispari.

def pari_disp(l: list):
    res = 0
    for i in l:
        res += i if i % 2 == 0 else -i
    return res


print(pari_disp([1, 2, 3, 4, 5]))

# Scrivere una funzione che prende tre valori di input, e ritorna la
# loro somma se i valori sono punteggi di esame validi(`0 <= grade <= 30`),
# e altrimenti ritorna `- 1`. Scriverne poi una variante che legge i valori da
# terminale con `input`.


def esami(l: list):
    res = 0
    for i in l:
        if not 0 <= i <= 30:
            return -1
        res += i
    return res


print(esami([20, 24, 28]))

# Scrivere una funzione che prende tre valori(`d`, `m`, `y`) e ritorna se la
# data è valida o no. Si possono ignorare gli anni bisestili. Ad esempio,
# ritorna `False` per `30/2/2017` e `True` per `1/1/1111`.


def date(d, m, y):
    _31 = [1, 3, 5, 7, 8, 10, 12]
    _30 = [4, 6, 9, 11]
    _28 = [2]
    if m in _31:
        return 1 <= d <= 31
    elif m in _30:
        return 1 <= d <= 30
    elif m in _28:
        return 1 <= d <= 28
    return False


print(date(32, 1, 1111))

# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`.


def no_space(s: str):
    return s.replace(' ', '')


print(no_space('ciasi kjnspnjk ndsk hjd  l'))

# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome letto come input e poi da `Buona giornata!`


def saluto(nome):
    return 'Ciao ' + nome + ' Buona Giornata'


print(saluto(input('Inserisci il tuo nome: ')))