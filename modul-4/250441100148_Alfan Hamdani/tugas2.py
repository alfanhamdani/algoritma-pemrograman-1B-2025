total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    while True:
        jam_lembur = input("Masukkan jumlah jam lembur: ")

        if not jam_lembur.isdigit():
            print("Input harus berupa angka!")
            continue

        jam_lembur = int(jam_lembur)

        if jam_lembur < 0:
            print("Jam lembur tidak boleh negatif!")
            continue

        break

    shift = input("Apakah shift malam? (y/n): ").lower()

    gaji_harian = 100000  # gaji pokok per hari

    # Hitung lembur
    if jam_lembur >= 1 and jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_harian += 100000
    elif jam_lembur == 5:
        gaji_harian += 125000
    elif jam_lembur == 6:
        gaji_harian += 200000
    elif jam_lembur == 7:
        gaji_harian += 225000
    elif jam_lembur == 8:
        gaji_harian += 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    # Tambah bonus shift malam
    if shift == 'y':
        gaji_harian += 50000
        total_bonus += 50000

    total_gaji += gaji_harian
    total_lembur += jam_lembur

print("\n=== Rangkuman Mingguan ===")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus}")
print(f"Total gaji seminggu: Rp{total_gaji}")