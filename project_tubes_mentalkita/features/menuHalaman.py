from features import konseling
from features import moodTracker
from features import chatbot
import pandas as pd
import os

# fungsi halaman utama 
def halaman_utama(username):
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")

        print("========================================")
        print(f"Selamat datang, {username}!")
        print("========================================")
        print("Main Menu:")
        print("1. Konseling")
        print("2. Mood Tracker")
        print("3. Chatbot")
        print("4. Keluar Program")
        print("========================================")

        # pilihan fitur
        pilih_fitur = input("Masukkan pilihanmu (1-5): ")

        if pilih_fitur == "1":
            konseling.menu_konseling()
        elif pilih_fitur == "2":
            moodTracker.menu_moodtracker()
        elif pilih_fitur == "3":
            chatbot.menu_chatbot()
        # jika user memasukkan 5 maka akan keluar dari program
        elif pilih_fitur == "4":
            print(f"Keluar dari program. Terima kasih sudah menggunakan MentalKita. Selamat tinggal, {username}!")
            break
        # jika user memasukkan pilihan yang tidak tersedia, maka akan ada pemberitahuan invalid
        else:
            print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")
