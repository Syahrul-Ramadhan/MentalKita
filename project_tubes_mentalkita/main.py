import os
from features import userAccount

def menu_awal():
    while True:
        # variabel untuk mendeteksi sistem operasi
        sistem_operasi = os.name
            
        # mendeteksi sistem operasi
        match sistem_operasi:
            # jika perangkat linux atau macOS maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "posix": os.system("clear")
            # jika perangkat windows maka tampilan terminal ketika awal program dijalankan akan dihapus atau dibersihkan
            case "nt": os.system("cls")
            
        # tampilan awal atau start menu
        print("=====================================")
        print("SELAMAT DATANG DI PROGRAM MENTALKITA.")
        print("=====================================")
        print("Silahkan pilih 3 opsi yang tersedia.")
        print("\n1. Register\n2. Login\n3. Keluar")
        print("=====================================")

        # input dari user untuk memilih 
        user_option = input("\nPilih opsi (1/2/3): ")

        print("\n=================================\n")

        # pengkondisian untuk mengarahkan user ke dalam fitur yang akan dijalankan
        if user_option == "1":
        # user akan diarahkan ke menu register
            userAccount.register()
            break
        elif user_option == "2":
        # user akan diarahkan ke menu login
            userAccount.login()
            break
        elif user_option == "3":
            # user akan diarahkan keluar dari program
            print("\nKeluar dari program.\nTerima kasih sudah berkunjung. Selamat tinggal!\n")
            print("=====================================")
            break
        else:
            # user akan diberitahu bahwa inputan invalid
            print("Pilihan invalid. Mohon masukkan 1, 2, atau 3.")
            menu_awal()


menu_awal()