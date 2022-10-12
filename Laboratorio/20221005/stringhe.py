# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale.
# Ad esempio, `s = "85721"`. Stampate la somma delle cifre contenute nella stringa.
s = '85721'
somma = 0
for c in s:
    somma += int(c)
print(somma)


# Scrivete una espressione che a partire da una stringa di 5 caratteri,
# rappresentante un numero binario, stampi la sua rappresentazione decimale.
# Ad esempio, `s = "00101" -> 5`.
res = 0
s = '01001'
exp = 0
for c in s[::-1]:
    res += int(c)*2**exp
    exp += 1
print(res)


# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale
# ('.'). Ad esempio, s = "52.29". Stampare il numero decimale rappresentato
# dalla stringa(stamparlo come numero, non come stringa).
s = '52.29'
a = float(s)
print(a, type(a))
