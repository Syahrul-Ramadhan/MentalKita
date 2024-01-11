# import modul csv agar dapat mengelola file csv
import csv
import os
from datetime import datetime


def menu_cari_psikolog_offline():
    while True:
        print("\n=== Cari Psikolog offline ===")
        search_input = input("Masukkan nama, topik, atau lokasi psikolog yang ingin dicari: ")
        hasil = cari_psikolog(search_input)

        if hasil:
            print("\nHasil Pencarian: ")
            for i, psikolog in enumerate(hasil, start=1):
                print(f"{i}. Nama: {psikolog['nama']}, Topik: {psikolog['topik']}, Lokasi: {psikolog['lokasi']}")

            pilihan = input("Pilih nomor psikolog yang ingin anda lihat profilnya (ketik 0 untuk kembali): ")
            if pilihan .isdigit() and 0 < int(pilihan) <= len(hasil):
                tampilkan_profil_psikolog_offline(hasil[int(pilihan)-1])
                break
            elif pilihan == "0":
                break
            else:
                print("Pilihan invalid. Silahkan masukkan nomor yang sesuai!")
                continue
        else:
            print("Psikolog tidak ditemukan.")
            print("Pilihan:")
            print("1. Cari lagi")
            print("2. Keluar dari menu cari psikolog.")
            pilihan = input("Masukkan pilihan (1/2): ")

            if pilihan == "1":
                continue
            elif pilihan == "2":
                break
            else:
                print("Pilihan invalid. Silahkan cari dan pilih opsi yang tersedia.")


def cari_psikolog(search_input):
    with open('./database/data_psikolog_offline.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        psikolog_ditemukan = []
        for row in csv_reader:
            if search_input.lower() in row['nama'].lower() or search_input.lower() in row['topik'].lower() or search_input.lower() in row['lokasi'].lower():
                psikolog_ditemukan.append(row)
    return psikolog_ditemukan

def lihat_daftar_psikolog_offline():
    with open('./database/data_psikolog_offline.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        daftar_psikolog = []
        for row in csv_reader:
            daftar_psikolog.append(row)

    while True:
            print("\n === Daftar Psikolog ===")
            for i, psikolog in enumerate(daftar_psikolog, start=1):
                print(f"{i}. Nama: {psikolog['nama']}, Topik: {psikolog['topik']}, Lokasi: {psikolog['lokasi']}")

            pilihan = input("Pilih nomor psikolog yang ingin anda lihat profilnya (ketik 0 untuk kembali): ")
            if pilihan .isdigit() and 0 < int(pilihan):
                tampilkan_profil_psikolog_offline(daftar_psikolog[int(pilihan)-1])
                break
            elif pilihan == "0":
                break
            else:
                print("Pilihan invalid. Silahkan masukkan nomor yang sesuai!")

def tampilkan_profil_psikolog_offline(psikolog):
    while True:
        print("\n ===Profil psikolog===")
        print(f"Nama: {psikolog['nama']}")
        print(f"Topik: {psikolog['topik']}")
        print(f"Lokasi: {psikolog['lokasi']}")
        print(f"Hari ketersediaan: {psikolog['hari']}")
        print(f"Bio: {psikolog['bio']}")
        print(f"Sesi: {psikolog['sesi']}")
        print(f"Harga: {psikolog['harga']}")
        print("-"*30)
        print("Pilihan:")
        print("1. Pesan sesi konsultasi")
        print("2. keluar dari menu profil")

        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == "1":
            pesan_sesi_konseling_offline(psikolog)
        elif pilihan == "2":
            break
        else:
            print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")

def pesan_sesi_konseling_offline(psikolog):
    print("\n ===Pesan sesi konseling===")
    print("sesi konseling yang tersedia:")
    for i, sesi in enumerate(eval(psikolog['sesi']), start=1):
        print(f"{i}. {sesi}")
    
    # pilih sesi
    pilihan_sesi = input("Pilih nomor sesi yang diinginkan (1,2,dst): ")
    if not pilihan_sesi.isdigit() or int(pilihan_sesi) < 1 or int(pilihan_sesi) > len(eval(psikolog['sesi'])):
        print("Pilihan sesi tidak valid.")
        return
    
    sesi_terpilih = eval(psikolog['sesi'])[int(pilihan_sesi) -1]
    metode_konseling = "Konseling Offline"
    
    # Pilih metode Pembayaran
    while True:
        print("\nMetode Pembayaran:")
        print("1. Transfer Bank")
        print("2. E-wallet")
        pilihan_metode = input("Pilih nomor metode Pembayaran yang diinginkan (1/2): ")
        if pilihan_metode == "1":
            metode_pembayaran = "Transfer Bank"
            break
        elif pilihan_metode == "2":
            metode_pembayaran = "E-wallet"
            break
        else:
            print("Pilihan metode Pembayaran tidak valid. Silahkan masukkan pilihan yang tersedia!")
    
    # Konfirmasi pesanan
    konfirmasi = input(f"\nAnda akan memesan sesi {sesi_terpilih} dengan {psikolog['nama']} menggunakan {metode_konseling} dan melakukan pembayaran menggunakan {metode_pembayaran}. Konfirmasi (ya/tidak): ")
    if konfirmasi.lower() == 'ya':
        # Tambahkan data pesanan ke file CSV
        data_pesanan = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'psikolog': psikolog['nama'],
            'sesi': sesi_terpilih,
            'metode konseling': metode_konseling,
            'metode pembayaran': metode_pembayaran
        }
        # Simpan data pesanan ke file CSV
        file_path = './database/data_konseling_user.csv'
        file_exists = os.path.exists(file_path)

        with open(file_path, 'a', newline='') as file:
            fieldnames = ['timestamp', 'psikolog', 'sesi', 'metode konseling', 'metode pembayaran']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(data_pesanan)

        print("Pesan sesi konsultasi berhasil!")
    else:
        print("Pesan sesi konsultasi dibatalkan.")