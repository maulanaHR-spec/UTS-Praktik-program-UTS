# Program aplikasi antrian klinik
antrian = []

while True:
    print("\n==== MENU ANTRIAN KLINIK ====")
    print("1. Tambah Pasien")
    print("2. Lihat Antrian Pasien")
    print("3. Layani Pasien")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")

    # tambah pasien
    if pilihan == "1":
        nama = input("Nama pasien : ")
        keluhan = input("Keluhan : ")
        antrian.append([nama, keluhan])
        print("Pasien berhasil ditambahkan.")

    # lihat antrian
    elif pilihan == "2":
        if len(antrian) == 0:
            print("Antrian kosong.")
        else:
            print("\nDaftar Antrian:")
            for i, p in enumerate(antrian, 1):
                print(f"{i}. {p[0]} - {p[1]}")

    # layani pasien terdepan
    elif pilihan == "3":
        if len(antrian) == 0:
            print("Tidak ada pasien untuk dilayani.")
        else:
            pasien = antrian.pop(0)
            print(f"Melayani pasien: {pasien[0]} (keluhan: {pasien[1]})")

            # jika antrian habis, beri pesan akhir
            if len(antrian) == 0:
                print("Semua pasien telah dilayani.")

    # keluar program
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")

