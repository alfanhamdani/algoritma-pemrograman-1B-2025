# Program Sederhana: Cek Apakah List Dapat Dibagi Menjadi Dua Bagian dengan Jumlah Sama
# Algoritma & Dasar Pemrograman | List & Tuple

data_angka = []

def tambah_data():
    angka = input("Masukkan deretan angka (contoh: 123321): ")
    for a in angka:
        if a.isdigit():
            data_angka.append(int(a))
    print("Data berhasil ditambahkan!")

def tampil_data():
    if not data_angka:
        print("Data masih kosong.")
    else:
        print("Daftar angka:", data_angka)

def ubah_data():
    if not data_angka:
        print("Data masih kosong.")
        return
    tampil_data()
    lama = int(input("Masukkan angka yang ingin diubah: "))
    if lama in data_angka:
        baru = int(input("Masukkan angka baru: "))
        hasil = []
        sudah = False
        for x in data_angka:
            if x == lama and not sudah:
                hasil.append(baru)
                sudah = True
            else:
                hasil.append(x)
        data_angka[:] = hasil
        print("Data berhasil diubah!")
    else:
        print("Angka tidak ditemukan!")

def hapus_data():
    if not data_angka:
        print("Data masih kosong.")
        return
    tampil_data()
    hapus = int(input("Masukkan angka yang ingin dihapus: "))
    if hapus in data_angka:
        hasil = []
        sudah = False
        for x in data_angka:
            if x == hapus and not sudah:
                sudah = True
                continue
            hasil.append(x)
        data_angka[:] = hasil
        print("Data berhasil dihapus!")
    else:
        print("Angka tidak ditemukan!")

def cek_bagian_sama():
    if not data_angka:
        print("Data masih kosong.")
        return

    n = len(data_angka)
    if n % 2 != 0:
        print("Jumlah elemen ganjil, tidak bisa dibagi dua bagian sama besar.")
        return

    tengah = n // 2
    bagian1 = data_angka[:tengah]
    bagian2 = data_angka[tengah:]

    total1 = sum(bagian1)
    total2 = sum(bagian2)

    print(f"Bagian 1: {bagian1}, jumlah = {total1}")
    print(f"Bagian 2: {bagian2}, jumlah = {total2}")

    if total1 == total2:
        print("True (jumlah kedua bagian sama)")
    else:
        print("False (jumlah kedua bagian berbeda)")

# === Menu utama ===
while True:
    print("\n=== PROGRAM PEMERIKSAAN LIST ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cek Dua Bagian Sama")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        tampil_data()
    elif pilih == "3":
        ubah_data()
    elif pilih == "4":
        hapus_data()
    elif pilih == "5":
        cek_bagian_sama()
    elif pilih == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")