import csv
import os
from datetime import datetime

# fungsi menu cari psikolog offline
def menu_cari_psikolog_offline():
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")
            
        print("=== Cari Psikolog offline ===")
        search_input = input("Masukkan nama, topik, atau lokasi psikolog yang ingin dicari: ")
        # menjalankan fungsi cari psikolog lalu hasilnya dimasukkan ke variabel hasil
        hasil = cari_psikolog(search_input)

        # pengkondisian jika hasil ada/bernilai atau psikolog ditemukan
        if hasil:
            print("\nHasil Pencarian: ")
            # perulangan untuk menampilkan daftar psikolog yang ada di hasil pencarian psikolog
            for i, psikolog in enumerate(hasil, start=1):
                print(f"{i}. Nama: {psikolog['nama']}, Topik: {psikolog['topik']}, Lokasi: {psikolog['lokasi']}")

            # pilihan untuk memilih psikolog yang tersedia, sedangkan 0 untuk kembali
            pilihan = input("Pilih nomor psikolog yang ingin anda lihat profilnya (ketik 0 untuk kembali): ")
            # pengecekan apakah pilihan merupakan angka dan lebih dari 0 dan tidak melebihi dari isi yang ada di variabel hasil
            if pilihan .isdigit() and 0 < int(pilihan) <= len(hasil):
                # jika true maka tampilkan daftar psikolognya
                tampilkan_profil_psikolog_offline(hasil[int(pilihan)-1])
                break
            # jika user memasukkan angka 0, maka user akan kembali dari menu cari psikolog
            elif pilihan == "0":
                break
            # jika user memasukkan pilihan selain 0 dan angka yang tersedia ataupun huruf, maka akan invalid
            else:
                print("Pilihan invalid. Silahkan masukkan nomor yang sesuai!")
                continue
        # pengkondisian jika hasil tidak bernilai atau psikolog tidak ditemukan
        else:
            print("Psikolog tidak ditemukan.")
            print("Pilihan:")
            print("1. Cari lagi")
            print("2. Keluar dari menu cari psikolog.")
            # pilihan untuk memilih cari lagi atau keluar dari menu cari psikolog
            pilihan = input("Masukkan pilihan (1/2): ")

            if pilihan == "1":
                continue
            elif pilihan == "2":
                break
            # jika user memasukkan angka yang tidak tersedia, huruf, atau simbol lainnya
            else:
                print("Pilihan invalid. Silahkan cari dan pilih opsi yang tersedia.")

# fungsi cari psikolog
def cari_psikolog(search_input):
    # membuka file data psikolog online dengan menggunakan operasi file
    with open('./database/data_psikolog_offline.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        # list untuk menyimpan data psikolog yang ditemukan
        psikolog_ditemukan = []
        # perulangan untuk mencari psikolog yang sesuai dengan inputan user
        for row in csv_reader:
            # pengkondisian jika terdapat kesesuaian dalam data maka data psikolog tersebut akan ditambahkan ke list psikoloh_ditemukan 
            if search_input.lower() in row['nama'].lower() or search_input.lower() in row['topik'].lower() or search_input.lower() in row['lokasi'].lower():
                psikolog_ditemukan.append(row)
    # mengembalikkan nilai list data psikolog yang ditemukan
    return psikolog_ditemukan

# fungsi lihat daftar psikolog offline
def lihat_daftar_psikolog_offline():
    # membuka file dengan menggunakan operasi file
    with open('./database/data_psikolog_offline.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        # list untuk menyimpan daftar psikolog
        daftar_psikolog = []
        # perulangan untuk menambahkan semua data psikolog ke list daftar_psikolog
        for row in csv_reader:
            daftar_psikolog.append(row)

    # perulangan untuk melihat daftar psikolog 
    while True:
            print("\n === Daftar Psikolog ===")
            # perulangan untuk menampilkan daftar psikolog yang berada di list dan ditambahkan nomor yang dimulai dari 1 di depan nama psikolog 
            for i, psikolog in enumerate(daftar_psikolog, start=1):
                print(f"{i}. Nama: {psikolog['nama']}, Topik: {psikolog['topik']}, Lokasi: {psikolog['lokasi']}")

            # pilihan untuk memilih psikolog yang ingin dilihat profilnya
            pilihan = input("Pilih nomor psikolog yang ingin anda lihat profilnya (ketik 0 untuk kembali): ")
            # pengkondisian jika pilihan merupakan angka dan lebih dari 0
            if pilihan .isdigit() and 0 < int(pilihan):
                # menjalankan fungsi untuk menampilkan profil psikolog offline yang sesuai dengan pilihan user
                tampilkan_profil_psikolog_offline(daftar_psikolog[int(pilihan)-1])
                break
            # pengkondisian jika user memasukkan angka 0, maka akan keluar dari menu daftar psikolog
            elif pilihan == "0":
                break
            # jika inputan user tidak sesuai maka akan muncul pemberitahuan invalid dan menu daftar psikolog akan diulang 
            else:
                print("Pilihan invalid. Silahkan masukkan nomor yang sesuai!")

# fungsi untuk menampilkan profil psikolog offline sesuai dengan pilihan user
def tampilkan_profil_psikolog_offline(psikolog):
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")
            
        print("===Profil psikolog===")
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

        # pilihan untuk pesan sesi atau keluar dari menu profil
        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == "1":
            pesan_sesi_konseling_offline(psikolog)
        elif pilihan == "2":
            break
        # jika user memasukkan pilihan yang tidak tersedia maka akan ada pemberitahuan invalid
        else:
            print("Pilihan invalid. Silahkan masukkan pilihan yang tersedia!")

# fungsi untuk pesan sesi konseling offline
def pesan_sesi_konseling_offline(psikolog):
    print("\n ===Pesan sesi konseling===")
    print("sesi konseling yang tersedia:")
    # perulangan untuk menampilkan sesi dari psikolog yang dipilih (menggunakan eval karena digunakan untuk mengeksekusi string yang berisi list)
    for i, sesi in enumerate(eval(psikolog['sesi']), start=1):
        print(f"{i}. {sesi}")
    
    # pilih sesi yang tersedia
    pilihan_sesi = input("Pilih nomor sesi yang diinginkan (1,2,dst): ")
    # jika pilihan tidak sesuai maka akan ada pemberitahuan invalid dan tidak akan mengembalikkan nilai
    if not pilihan_sesi.isdigit() or int(pilihan_sesi) < 1 or int(pilihan_sesi) > len(eval(psikolog['sesi'])):
        print("Pilihan sesi tidak valid.")
        return
    # variabel untuk menyimpan data sesi yang dipilih (menggunakan eval untuk mengecek list yang berada dalam string)
    sesi_terpilih = eval(psikolog['sesi'])[int(pilihan_sesi) -1]
    # variabel untuk menyimpan metode konseling offline
    metode_konseling = "Konseling Offline"
    
    # Pilih metode Pembayaran
    while True:
        print("\nMetode Pembayaran:")
        print("1. Transfer Bank")
        print("2. E-wallet")
        pilihan_metode = input("Pilih nomor metode Pembayaran yang diinginkan (1/2): ")
        # pengkondisian jika pilihan metode == 1, maka metode_pembayaran akan menyimpan data string "Transfer Bank"
        if pilihan_metode == "1":
            metode_pembayaran = "Transfer Bank"
            print("No. Rek/Virtual Account \n 781 1234 5678 9012 \nSilahkan transfer ke nomor tersebut dan pastikan jumlah pembayaran sudah benar.")
            break
        # pengkondisian jika pilihan metode == 2, maka metode_pembayaran akan menyimpan data string "E-wallet"
        elif pilihan_metode == "2":
            metode_pembayaran = "E-wallet"
            print("No. E-wallet \n 081 2345 6789 \nSilahkan transfer ke nomor tersebut dan pastikan jumlah pembayaran sudah benar.")
            break
        # jika user memasukkan pilihan yang tidak tersedia maka akan memunculkan pemberitahuan invalid
        else:
            print("Pilihan metode Pembayaran tidak valid. Silahkan masukkan pilihan yang tersedia!")
    
    # Konfirmasi pesanan
    konfirmasi = input(f"\nAnda akan memesan sesi {sesi_terpilih} dengan {psikolog['nama']} menggunakan {metode_konseling} dan melakukan pembayaran menggunakan {metode_pembayaran}. Konfirmasi (ya/tidak): ")
    # pengkondisian jika user memasukkan ya maka akan menambahkan data pesanan ke database
    if konfirmasi.lower() == 'ya':
        # Dictionary untuk menyimpan data yang telah dipilih user sebelumnya
        data_pesanan = {
            # timestamp akan menyimpan data waktu ketika user memasukkan data pesanan
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'psikolog': psikolog['nama'],
            'sesi': sesi_terpilih,
            'metode konseling': metode_konseling,
            'metode pembayaran': metode_pembayaran
        }
        # mengecek apakah file data konseling user ada 
        file_path = './database/data_konseling_user.csv'
        file_exists = os.path.exists(file_path)

        # membuka file csv dan menggunakan metode 'a' atau append untuk menambahkan data
        with open(file_path, 'a', newline='') as file:
            # header di file data konseling
            fieldnames = ['timestamp', 'psikolog', 'sesi', 'metode konseling', 'metode pembayaran']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # jika file tidak ada maka akan membuat file baru dengan menambahkan header
            if not file_exists:
                writer.writeheader()

            # jika file ada maka akan menambahkan data pesanan yang telah diinputkan oleh user
            writer.writerow(data_pesanan)

        # konfirmasi pesan sesi konsultasi berhasil
        print("Pesan sesi konsultasi berhasil!")
    # jika user memilih selain ya, maka data tidak akan ditambahkan dan muncul konfirmasi pesan sesi konsultasi dibatalkan
    else:
        print("Pesan sesi konsultasi dibatalkan.")