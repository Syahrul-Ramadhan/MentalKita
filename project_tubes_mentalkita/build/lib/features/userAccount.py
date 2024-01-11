# import modul csv agar dapat mengelola file csv
import csv
from features import menuHalaman
# fungsi untuk register
def register():
    """
    Fungsi ini memungkinkan pengguna untuk mendaftar (register) dengan
    memasukkan username dan password. Data yang dimasukkan akan
    disimpan dalam file CSV 'data_akun.csv'. Fungsi ini memiliki
    mekanisme pemeriksaan username yang sudah digunakan dan kecocokan
    antara password dan konfirmasi password.
    """

    # perulangan agar program terus berjalan
    while True:
        print("=== Register ===")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        # Membaca data akun yang sudah terdaftar
        data_akun = []

        with open('./database/data_akun.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=",")
            for row in csv_reader:
                data_akun.append({"username": row[0], "password": row[1]})
        
        # Mengecek apakah username sudah digunakan
        akun_sesuai = False

        for akun in data_akun:
            if username == akun['username']:
                print("Username sudah digunakan, silahkan gunakan username lain!")
                akun_sesuai = True
                break

        # Mengecek kecocokan password dan konfirmasi password
        if password != confirm_password:
            print("Password tidak sesuai, silahkan masukkan kembali")
            akun_sesuai = True

        # Jika semua kondisi terpenuhi, data baru ditambahkan ke file CSV
        if akun_sesuai == False:
            data_baru = {'username': username, 'password': password}
            with open('./database/data_akun.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data_baru.keys())
                writer.writerow(data_baru)
                # Memastikan data ditulis ke file secara instan
                file.flush()
                # Menutup file setelah penulisan
                file.close()
                print("Pendaftaran berhasil!")
                # masuk ke menu login
                from main import menu_awal
                menu_awal()
                break

# fungsi untuk login
def login():
    """
    Fungsi ini memungkinkan pengguna untuk login dengan memasukkan
    username dan password. Data yang dimasukkan akan dibandingkan
    dengan data yang telah terdaftar dalam file CSV 'data_akun.csv'.
    Fungsi ini memberikan pilihan untuk menyerah atau mencoba login
    ulang jika akun tidak ditemukan.
    """

    print("=== Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Membaca data akun yang sudah terdaftar
    data_akun = []

    with open('./database/data_akun.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_akun.append({"username": row[0], "password": row[1]})

    # list untuk mengetahui siapa yang login
    data_login = []

    # Mengecek kecocokan username dan password untuk login
    for i in data_akun:
        if username == i['username'] and password == i['password']:
            data_login.append(i)
            print("Berhasil login.")
            menuHalaman.halaman_utama(username)

    # Jika akun tidak ditemukan, memberikan opsi untuk menyerah atau mencoba lagi
    if len(data_login) == 0:
        print("Akun tidak ditemukan.")
        pilih = input("Apakah anda ingin menyerah? \n 1. Ya \n 2. Tidak \npilih: ")
        if pilih == "1":
            print("Terima kasih sudah mencoba, selamat tinggal.")
        elif pilih == "2":
            login()
        else:
            print("Pilihan invalid, silahkan masukkan pilihan yang sesuai.")
            pilih = input("Apakah anda ingin menyerah? \n 1. Ya \n 2. Tidak \npilih: ")
