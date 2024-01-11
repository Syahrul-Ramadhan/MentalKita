import csv
from features import konseling
from datetime import datetime
import os
import pandas as pd
# modul matplotlib untuk menampilkan diagram
import matplotlib.pyplot as plt

# fungsi menu moodtracker
def menu_moodtracker():
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")
            
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

        # pilihan fitur
        pilih_fitur = input("Pilih fitur: ")
        if pilih_fitur == "1":
            input_moodtracker()
        elif pilih_fitur == "2":
            lihat_statistik()
        elif pilih_fitur == "3":
            lihat_timeline()
        elif pilih_fitur == "4":
            print("Terima kasih sudah berkunjung ke menu fitur moodtracker, selamat tinggal.")
            break
        else:
            print("Pilihan invalid. Mohon masukkan pilihan yang tersedia!")

#  Fungsi input data moodtracker
def input_moodtracker():
    # list yang berisi daftar emosi
    emosi_baik = ["Senang","Bangga","Lega","Optimis","Puas","Percaya diri","Tenang","Bersyukur","Semangat"]
    emosi_lumayan = ["Senang","Oke", "Baik","Lega","Tenang","Bersyukur","cukup puas"]
    emosi_biasa = ["Santai","Tenang","Puas","Bosan","Bingung"]
    emosi_kurang = ["Sedih","Marah","Takut","Kecewa","Malu","Bersalah","Gugup","Bosan"]
    emosi_buruk = ["Sedih","Marah","Takut","Kecewa","Malu","Bersalah","Gugup","Stress","Putus asa","Bosan"]
    # list untuk menyimpan data emosi user
    emosi_user = []

    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")
            
        # Menampilkan header menu input moodtracker
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

        # pengkondisian jika user menginputkan pilihan yang tidak sesuai maka akan ada pemberitahuan invalid dan user akan mengisi ulang  karena ada continue yang akan mengabaikan semua kondisi setelahnya 
        if perasaan not in ["1", "2", "3", "4", "5"]:
            print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")
            continue

        # Mengevaluasi perasaan yang dipilih pengguna lalu akan menampilkan emosi berdasarkan kondisi perasaan user
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
        
        # perulangan untuk menampilkan pilihan emosi yang berada di list
        for i, x in enumerate(emosi_pilihan, 1):
            print(f"{i}. {x}")

        # Looping untuk meminta pengguna memilih emosi dengan batasan kesempatan
        kesempatan = 3
        while kesempatan >= 1:
            emosi_input = input("Pilih emosi yang paling menggambarkanmu hari ini: ")
            # pengkondisian jika emosi yang diinputkan merupakan angka, lebih dari sama dengan 1 dan angka yang diinputkan tersedia di pilihan emosi berdasarkan index
            if emosi_input.isdigit() and 1 <= int(emosi_input) <= len(emosi_pilihan):
                # menambahkan pilihan emosi ke list emosi user
                emosi_user.append(emosi_pilihan[int(emosi_input)-1])
            # jika user memasukkan pilihan yang tidak tersedia maka akan ada pemberitahuan invalid
            else:
                print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")

            # pilihan untuk user jika ingin memilih lagi atau tidak
            pilih_ulang = input("Apakah anda ingin memilih lagi? (y/t)").lower()
            # jika iya, maka kesempatan berkurang 1 dan user dapat memilih lagi selama kesempatan masih ada
            if pilih_ulang == "y":
                kesempatan -=1
                if kesempatan >= 1:
                    print(f"kesempatan anda memilih {kesempatan} kali lagi.")
                else:
                    print(f"Kesempatan sudah habis.")
                    break
            # jika user memilih tidak, maka akan user akan keluar dari menu pilih emosi
            elif pilih_ulang == "t":
                break
            # pemberitahuan invalid jika user memasukkan pilihan yang tidak tersedia
            else:
                print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")

        # inputan untuk menerima cerita dari user
        cerita = input("Mau cerita apa yang terjadi hari ini? ")
        # konfirmasi penyimpanan
        konfirmasi = input("Apakah anda ingin menyimpan data yang telah dimasukkan? (ya/tidak): ")
        # jika setuju untuk konfirmasi akan menambahkan data ke file csv
        if konfirmasi.lower() == 'ya':
            # Dictionary untuk menyimpan sementara inputan user
            data_moodtracker = {
                # timestamp untuk menyimpan data waktu saat user menyimpan data
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'perasaan': perasaan_user,
                'emosi': emosi_user,
                'cerita': cerita
            }

            # mengecek apakah file untuk menyimpan data moodtracker ada
            file_path = './database/data_moodtracker.csv'
            file_exists = os.path.exists(file_path)

            # membuka file dengan operasi file dan dengan metode 'a' atau append untuk menambahkan data
            with open(file_path, 'a', newline='') as file:
                # header
                fieldnames = ['timestamp', 'perasaan', 'emosi', 'cerita']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # jika file data moodtracker tidak ada maka akan membuat baru dan akan menambahkan header
                if not file_exists:
                    writer.writeheader()

                # jika file ada, maka data akan ditambahkan
                writer.writerow(data_moodtracker)

            # konfirmasi data berhasil disimpan
            print("Data moodtracker berhasil disimpan!")
        # jika user memasukkan selain 'ya' maka data akan batal disimpan
        else:
            print("Data moodtracker batal disimpan.")
        # jika perasaan memiliki nilai 4 atau 5 maka akan ditawarkan untuk melakukan konseling
        if perasaan in ["4","5"]:
            # pilihan 
            indikator = input("Apakah anda ingin melakukan konseling? (y/t): ")
            # jika user ingin melakukan konseling maka user akan diarahkan ke menu konseling
            if indikator.lower() == "y":
                konseling.menu_konseling()
                break
            # jika tidak maka user akan keluar dari menu moodtracker
            else:
                break
        break
    
# fungsi lihat statistik
def lihat_statistik():
    # membaca file csv dengan modul pandas
    df = pd.read_csv('./database/data_moodtracker.csv')
    df['timestamp'] = pd.to_datetime(df["timestamp"])

    # Pemrosesan data untuk mengambil tanggal (hanya hari dan bulan saja)
    df['Tanggal'] = df['timestamp'].dt.strftime('%d-%m')  

    # Menghitung jumlah perasaan per hari dan mengubahnya hasilnya ke dalam dataframe
    perasaan_per_hari = df.groupby(['Tanggal', 'perasaan']).size().unstack(fill_value=0)

    # Membuat grafik garis
    # Membuat plot garis untuk menampilkan perkembangan jumlah perasaan per hari
    perasaan_per_hari.plot(kind="line", marker='o')
    # menambahkan judul plot
    plt.title("Perkembangan moodmu dalam beberapa hari terakhir")
    # menambahkan label untuk sumbu x, yaitu tanggal
    plt.xlabel("Tanggal")
    # menambahkan label untuk sumbu y, yaitu jumlah
    plt.ylabel("Jumlah")
    # Menambahkan legenda dengan judul "Perasaan" di luar plot (di posisi kanan atas).
    plt.legend(title="perasaan", bbox_to_anchor=(1, 1))
    # menampilkan plot
    plt.show()

# fungsi lihat timeline
def lihat_timeline():
    # membaca file csv dengan modul pandas
    df = pd.read_csv('./database/data_moodtracker.csv')
    while True:
        print("===Timeline Moodtracker===")
        # menampilkan dataframe
        print(df)
        # pilihan, jika 1 maka akan keluar dari menu timeline moodtracker
        pilihan = input("Ketik 1 jika ingin keluar dari menu timeline moodtracker.")
        if pilihan == "1":
            break

