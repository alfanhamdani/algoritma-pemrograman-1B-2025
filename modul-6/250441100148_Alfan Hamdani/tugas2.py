# Program menggabungkan dua tuple tanpa duplikat dan mengurutkannya secara menurun (tanpa sorted)

def gabung_tuple(t1, t2):

    gabungan = t1 + t2

    tanpa_duplikat = []
    for angka in gabungan:
        if angka not in tanpa_duplikat:
            tanpa_duplikat.append(angka)

    for i in range(len(tanpa_duplikat)):
        for j in range(i + 1, len(tanpa_duplikat)):
            if tanpa_duplikat[i] < tanpa_duplikat[j]:
                tanpa_duplikat[i], tanpa_duplikat[j] = tanpa_duplikat[j], tanpa_duplikat[i]

    return tuple(tanpa_duplikat)

t1 = (3, 1, 4)
t2 = (1, 5, 9)

hasil = gabung_tuple(t1, t2)
print("Hasil akhir:", hasil)