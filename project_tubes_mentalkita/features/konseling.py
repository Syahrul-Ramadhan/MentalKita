from features import konselingOnline
from features import konselingOffline
import os

# fungsi menu konseling
def menu_konseling():
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")

        print("==================================")
        print("Selamat datang di fitur konseling!")
        print("==================================")
        print("Cara menggunakan fitur konseling: \n 1. Tentukan metode yang diinginkan. \n 2. Cari dan Pilih psikolog yang tersedia \n 3, Lihat profil psikolog. \n 4. Pesan sesi yang anda inginkan. \n 5. Bayar dan konfirmasi pemesanan")
        print("\n Silahkan pilih metode konseling yang tersedia")
        print("1. Konseling Online")
        print("2. konseling Offline")
        print("3. keluar dari menu konseling")

        # pilihan untuk metode konseling
        input_metode = input("Pilih metode: ")
        if input_metode == "1":
            konseling_online()
        elif input_metode == "2":
            konseling_offline()
        elif input_metode == "3":
            print("Terima kasih sudah berkunjung ke menu konseling, selamat tinggal.")
            break
        else:
            print("Pilihan invalid. Mohon masukkan pilihan yang tersedia!")

# fungsi untuk menu konseling online 
def konseling_online():
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")

        print("=== Konseling Online ===")
        print("1. Search Psikolog.")
        print("2. Lihat daftar Psikolog yang tersedia.")
        print("3. Keluar dari menu konseling online.")

        # pilihan untuk fitur di konseling online
        pilih_fitur = input("Pilih fitur yang tersedia di konseling online (1-3): ")
        if pilih_fitur == "1":
            konselingOnline.menu_cari_psikolog_online()
        elif pilih_fitur == "2":
            konselingOnline.lihat_daftar_psikolog_online()
        elif pilih_fitur == "3":
            print("Keluar dari menu konseling online.")
            break
        else:
            print("Pilihan invalid. Mohon masukkan pilihan yang tersedia!")

# fungsi menu konseling offline
def konseling_offline():
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")
            
        print("=== Konseling Offline ===")
        print("1. Search Psikolog.")
        print("2. Lihat daftar Psikolog yang tersedia.")
        print("3. Keluar dari menu konseling offline.")

        # pilihan fitur di menu konseling offline
        pilih_fitur = input("Pilih fitur di konseling offline (1-3): ")

        if pilih_fitur == "1":
            konselingOffline.menu_cari_psikolog_offline()
        elif pilih_fitur == "2":
            konselingOffline.lihat_daftar_psikolog_offline()
        elif pilih_fitur == "3":
            print("Keluar dari menu konseling offline.")
            break
        else:
            print("Pilihan invalid. Mohon masukkan pilihan yang tersedia!")
