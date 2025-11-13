# Program Sistem Kunjungan Santri

data_kunjungan = []
id_kunjungan = 1

def hanya_huruf(teks):
    """Fungsi untuk memastikan input hanya huruf dan spasi"""
    return all(char.isalpha() or char.isspace() for char in teks)

def tambah_pengunjung(data_kunjungan, id_kunjungan):
    print("\n=== Tambah Data Pengunjung ===")

    # Input nama pengunjung
    while True:
        nama_pengunjung = input("Masukkan nama pengunjung: ")
        if hanya_huruf(nama_pengunjung) and nama_pengunjung.strip() != "":
            break
        else:
            print("Nama pengunjung tidak boleh berupa angka atau karakter khusus!")

    # Input nama santri
    while True:
        nama_santri = input("Masukkan nama santri yang dijenguk: ")
        if hanya_huruf(nama_santri) and nama_santri.strip() != "":
            break
        else:
            print("Nama santri tidak boleh berupa angka atau karakter khusus!")

    # Input daerah asal dengan validasi huruf dan pilihan
    while True:
        daerah_asal = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if not hanya_huruf(daerah_asal):
            print("Daerah asal tidak boleh berupa angka atau karakter khusus!")
        elif daerah_asal not in ["Sumatra", "Kalimantan", "Jawa"]:
            print("Daerah asal tidak valid! Harus 'Sumatra', 'Kalimantan', atau 'Jawa'.")
        else:
            break

    # Tambahkan data ke list utama
    data_kunjungan.append([id_kunjungan, nama_pengunjung, nama_santri, daerah_asal])
    print(f"Data berhasil ditambahkan dengan ID antrian: {id_kunjungan}")

    return id_kunjungan + 1

def tampilkan_pengunjung(data_kunjungan):
    print("\n=== Daftar Pengunjung Berdasarkan Daerah Asal ===")
    if not data_kunjungan:
        print("Belum ada data pengunjung.")
        return

    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan_daerah:
        print(f"\n--- Pengunjung dari {daerah} ---")
        ada_data = False
        for data in data_kunjungan:
            if data[3] == daerah:
                ada_data = True
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
        if not ada_data:
            print("Tidak ada pengunjung dari daerah ini.")

def hapus_pengunjung(data_kunjungan):
    print("\n=== Hapus Data Pengunjung ===")
    if not data_kunjungan:
        print("Belum ada data yang bisa dihapus.")
        return

    id_hapus_input = input("Masukkan ID antrian yang akan dihapus: ")

    if not id_hapus_input.isdigit():
        print("ID harus berupa angka!")
        return

    id_hapus = int(id_hapus_input)
    ditemukan = False

    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print(f"Data dengan ID {id_hapus} berhasil dihapus.")
            ditemukan = True
            break

    if not ditemukan:
        print(f"Data dengan ID {id_hapus} tidak ditemukan.")

# === Program Utama ===
while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    # Validasi menu agar hanya angka
    if not pilihan.isdigit():
        print("Pilihan tidak boleh berupa karakter dan huruf! Harus angka 1-4.")
        continue

    pilihan = int(pilihan)

    if pilihan == 1:
        id_kunjungan = tambah_pengunjung(data_kunjungan, id_kunjungan)
    elif pilihan == 2:
        tampilkan_pengunjung(data_kunjungan)
    elif pilihan == 3:
        hapus_pengunjung(data_kunjungan)
    elif pilihan == 4:
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan pilih antara 1 sampai 4.")