import csv
from features import konseling
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt

def menu_moodtracker():
    while True:
        print("====================================")
        print("Selamat Datang di fitur mood tracker")
        print("====================================")
        print("Cara menggunakan fitur moodtracker: \n Dalam fitur moodtracker, anda dapat memilih untuk mengisi data mengenai perasaan dan emosimu hari ini atau memilih untuk melihat statistik perkembangan moodmu atau melihat timeline moodmu.")
        print("\n jika anda memilih untuk mengisi data moodmu maka ikutilah dan pahami langkah-langkah berikut.")
        print(" 1. Pilih perasaan yang tersedia. \n 3, Pilih emosi yang paling menggambarkan kamu hari ini. \n 4. kamu boleh bercerita tentang apa yang terjadi hari ini. \n 5. Simpan data mood yang telah kamu isi dan selesai.")
        print("\n Silahkan pilih fitur yang tersedia")
        print("1. Ceritakan tentang keadaanmu hari ini.")
        print("2. Lihat statistik mood.")
        print("3. Lihat timeline moodtracker.")
        print("4. Keluar dari menu moodtracker.")

        input_metode = input("Pilih metode: ")
        if input_metode == "1":
            input_moodtracker()
        elif input_metode == "2":
            lihat_statistik()
        elif input_metode == "3":
            lihat_timeline()
        elif input_metode == "4":
            print("Terima kasih sudah berkunjung ke menu fitur moodtracker, selamat tinggal.")
            break
        else:
            print("Pilihan invalid. Mohon masukkan pilihan yang tersedia!")

#  Fungsi moodTracker berfungsi untuk mengecek perasaan dan emosi pengguna serta mencatat cerita yang terkait.
def input_moodtracker():
    emosi_baik = ["Senang","Bangga","Lega","Optimis","Puas","Percaya diri","Tenang","Bersyukur","Semangat"]
    emosi_lumayan = ["Senang","Oke", "Baik","Lega","Tenang","Bersyukur","cukup puas"]
    emosi_biasa = ["Santai","Tenang","Puas","Bosan","Bingung"]
    emosi_kurang = ["Sedih","Marah","Takut","Kecewa","Malu","Bersalah","Gugup","Bosan"]
    emosi_buruk = ["Sedih","Marah","Takut","Kecewa","Malu","Bersalah","Gugup","Stress","Putus asa","Bosan"]
    emosi_user = []

    while True:
        # Menampilkan header mood tracker
        print("===Ceritakan moodmu===")
        # Menampilkan pilihan perasaan kepada pengguna
        print("\nBagaimana perasaanmu hari ini?")
        print("1. Baik")
        print("2. Lumayan")
        print("3. Biasa")
        print("4. Kurang")
        print("5. Buruk")
        # Meminta input dari pengguna untuk memilih perasaan
        perasaan = input("Pilih keadaan perasaanmu hari ini: ")

        if perasaan not in ["1", "2", "3", "4", "5"]:
            print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")
            continue

        # Mengevaluasi perasaan yang dipilih pengguna
        print("Apa emosi yang kamu rasakan?")
        emosi_pilihan = []
        if perasaan == "1":
            perasaan_user = "Baik"
            emosi_pilihan = emosi_baik
        elif perasaan == "2":
            perasaan_user = "Lumayan"
            emosi_pilihan = emosi_lumayan
        elif perasaan == "3":
            perasaan_user = "Biasa"
            emosi_pilihan = emosi_biasa
        elif perasaan == "4":
            perasaan_user = "Kurang"
            emosi_pilihan = emosi_kurang
        elif perasaan == "5":
            perasaan_user = "Buruk"
            emosi_pilihan = emosi_buruk
        
        for i, x in enumerate(emosi_pilihan, 1):
            print(f"{i}. {x}")

        # Looping untuk meminta pengguna memilih emosi dengan batasan kesempatan
        kesempatan = 3
        while kesempatan >= 1:
            emosi_input = input("Pilih emosi yang paling menggambarkanmu hari ini: ")
            if emosi_input.isdigit() and 1 <= int(emosi_input) <= len(emosi_pilihan):
                emosi_user.append(emosi_pilihan[int(emosi_input)-1])
            else:
                print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")

            pilih_ulang = input("Apakah anda ingin memilih lagi? (y/t)").lower()
            if pilih_ulang == "y":
                kesempatan -=1
                if kesempatan >= 1:
                    print(f"kesempatan anda memilih {kesempatan} kali lagi.")
                else:
                    print(f"Kesempatan sudah habis.")
                    break
            elif pilih_ulang == "t":
                break
            else:
                print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")

        cerita = input("Mau cerita apa yang terjadi hari ini? ")
        konfirmasi = input("Apakah anda ingin menyimpan data yang telah dimasukkan? (ya/tidak): ")
        if konfirmasi.lower() == 'ya':
            # Tambahkan data mooddata_moodtracker ke file CSV
            data_moodtracker = {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'perasaan': perasaan_user,
                'emosi': emosi_user,
                'cerita': cerita
            }

            # Simpan data mooddata_moodtracker ke file CSV
            file_path = './database/data_moodtracker.csv'
            file_exists = os.path.exists(file_path)

            with open(file_path, 'a', newline='') as file:
                fieldnames = ['timestamp', 'perasaan', 'emosi', 'cerita']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                if not file_exists:
                    writer.writeheader()

                writer.writerow(data_moodtracker)

            print("Data moodtracker berhasil disimpan!")
        else:
            print("Data moodtracker batal disimpan.")
        if perasaan in ["4","5"]:
            indikator = input("Apakah anda ingin melakukan konseling? (y/t): ")
            if indikator.lower() == "y":
                konseling.menu_konseling()
                break
            else:
                break
        break
    
def lihat_statistik():
    df = pd.read_csv('./database/data_moodtracker.csv')
    df['timestamp'] = pd.to_datetime(df["timestamp"])

    # Prapemrosesan data untuk mengambil tanggal
    df['Tanggal'] = df['timestamp'].dt.strftime('%d-%m')  # Format hanya hari dan bulan

    # Menghitung jumlah perasaan unik per hari
    perasaan_per_hari = df.groupby(['Tanggal', 'perasaan']).size().unstack(fill_value=0)

    # Membuat grafik garis
    perasaan_per_hari.plot(kind="line", marker='o')
    plt.title("Perkembangan moodmu dalam beberapa hari terakhir")
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah")
    plt.legend(title="perasaan", bbox_to_anchor=(1, 1))
    plt.show()

def lihat_timeline():
    df = pd.read_csv('./database/data_moodtracker.csv')
    while True:
        print("===Timeline Moodtracker===")
        print(df)
        pilihan = input("Ketik 0 jika ingin keluar dari menu timeline moodtracker.")
        if pilihan == "0":
            break

