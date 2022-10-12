# Scrivete una espressione che calcoli il numero di secondi che ci sono in
# 42 minuti e 42 secondi.
# (42*60) + 42


# Scrivete una espressione che calcoli il numero di miglia che ci sono in
# 10 chilometri. (1 miglio=1.61 km).
# 10/1.61


# Scrivete una espressione che calcoli la velocità media e la cadenza media
# (tempo per miglio, in minuti e secondi) di un corridore che corre una gara
# di 10 chilometri in 42 minuti e 42 secondi.
# vel media = (10/1.61)/((42*60)+42)
# cadenza = ((42*60)+42)/(10/1.61)


# Il volume di una sfera di raggio `r` è `4/3 * PI * r ^ 3`.
# Scrivere una espressione che calcoli il volume di una sfera di raggio 5.
# v = (4/3) * 3.14 * 5**3


# Il prezzo di copertina di un libro è 24.95, ma una liberia ottiene il 40%
# di sconto. I costi di spedizione sono 3 euro per la prima copia, e 75
# centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60 copie?
# ((24.95-(24.95*40/100) + 0.75)*60) + (3 - 0.75)


# Se uscite di casa alle 6: 52 di mattina e correte un miglio a ritmo blando
# (8 minuti e 15 secondi al miglio), e poi 3 miglia a ritmo moderato
# (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo blando
# (9 minuti e 45 secondi al miglio), a che ora sarete tornati a casa?
t1 = (8*60) + 15
t2 = ((7*60) + 12)*3
t3 = (9*60) + 45
t = t1 + t2 + t3
print(t//60)
ora = 6 + (((t / 60) + 52) // 60)
minuti = (((t / 60) + 52) % 60)
print(int(ora), int(minuti))
