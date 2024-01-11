from features import konseling
from features import moodTracker
from features import chatbot
import pandas as pd

def halaman_utama(username):
    while True:
        print("========================================")
        print(f"Selamat datang, {username}!")
        print("========================================")
        print("Main Menu:")
        print("1. Konseling")
        print("2. Mood Tracker")
        print("3. Chatbot")
        print("4. Riwayat Konseling")
        print("5. Keluar Program")
        print("========================================")

        pilih_fitur = input("Masukkan pilihanmu (1-5): ")

        if pilih_fitur == "1":
            konseling.menu_konseling()
        elif pilih_fitur == "2":
            moodTracker.menu_moodtracker()
        elif pilih_fitur == "3":
            chatbot.menu_chatbot()
        elif pilih_fitur == "4":
            riwayat_konseling()
        elif pilih_fitur == "5":
            print(f"Keluar dari program. Terima kasih sudah menggunakan MentalKita. Selamat tinggal, {username}!")
            break
        else:
            print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")

def riwayat_konseling():
    df = pd.read_csv('./database/data_konseling_user.csv')
    while True:
        print("===Riwayat Konseling===")
        print(df)
        pilihan = input("Ketik 0 jika ingin keluar dari menu riwayat konseling.")
        if pilihan == "0":
            break