stok = []

def tambah_data():
    nama_barang = input("Masukkan nama barang: ")
    jumlah_barang = int(input("Masukkan stok barang: "))
    
    stok_baru = {"nama": nama_barang, "jml": jumlah_barang}
    stok.append(stok_baru)
    print("Data berhasil ditambahkan")

def edit_data():
    if not stok:
        print("Tidak ada data barang yang tersedia untuk diedit.")
        return
    
    try:
        index = int(input("Masukkan indeks data yang ingin diedit: "))
        if index < 0 or index >= len(stok):
            print("Indeks tidak valid.")
            return
    except ValueError:
        print("Indeks harus berupa angka.")
        return

    nama_barang = input("Masukkan nama barang baru: ")
    jumlah_barang = int(input("Masukkan jumlah barang baru: "))

    stok[index] = {'nama': nama_barang, 'jml': jumlah_barang}
    print(f"Barang pada indeks {index} berhasil diubah.")

def hapus_data():
    if not stok:
        print("Tidak ada data barang yang tersedia untuk dihapus.")
        return
    
    try:
        hapus = int(input("Hapus data index ke: "))
        if hapus < 0 or hapus >= len(stok):
            print("Indeks tidak valid.")
            return
    except ValueError:
        print("Indeks harus berupa angka.")
        return
    
    stok.pop(hapus)
    print("Data berhasil dihapus")

def cari_data():
    if not stok:
        print("Tidak ada data barang yang tersedia untuk dicari.")
        return

    nama_barang = input("Cari nama barang: ")
    hasil = [item for item in stok if nama_barang.lower() in item['nama'].lower()]

    if hasil:
        print("===== Hasil Pencarian =====")
        for item in hasil:
            print(f"Nama: {item['nama']}, Stok: {item['jml']}")
    else:
        print("Barang tidak ditemukan.")

def tampil_data():
    if not stok:
        print("===== Toko Elektronik =====")
        print("----- Data Barang Kosong -----")
    else:
        print("===== Data Barang =====")
        for item in stok:
            print(f"Nama: {item['nama']}, Jumlah: {item['jml']}")

def tampil_jumlah_data():
    jumlah = len(stok)
    print(f"Jumlah data tersimpan: {jumlah} barang")
