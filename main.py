import modul as mod

def main():
    while True:
        print("\nSelamat datang di program Manajemen Stok Barang!")
        print("Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data")
        print("3. Hapus Data Barang")
        print("4. Cari Data")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Pilihan harus berupa angka.")
            continue

        if pilihan == 1:
            mod.tambah_data()
        elif pilihan == 2:
            mod.edit_data()
        elif pilihan == 3:
            mod.hapus_data()
        elif pilihan == 4:
            mod.cari_data()
        elif pilihan == 5:
            mod.tampil_data()
        elif pilihan == 6:
            mod.tampil_jumlah_data()
        elif pilihan == 7:
            print("Terimakasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
