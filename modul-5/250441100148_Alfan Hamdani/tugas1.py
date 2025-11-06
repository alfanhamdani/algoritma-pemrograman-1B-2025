# Program menghitung faktorial secara rekursif
def faktorial(n):

    if n == 0 or n == 1:
        return 1
    elif n < 0 :
        return "Angka tidak valid!"
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan bulat non-negatif: "))

print(f"Faktorial dari", n, "adalah :", faktorial(n))