# SHALOMMITA P
# 71200640
# LAB 10 DICTIONARY

# INPUT
# OPSI PILIHAN
# BARANG YANG AKAN DITAMBAH/DIHAPUS
# JUMLAH BARANG YG AKAN DITAMBAH

# PROSES
# UBAH KE DALAM DICT
# LAKUKAN PERCABANGAN dan Perulangan While

# OUTPUT
import sys

keranjang={}

def utama():
    print("""
    Keranjang Stok Toko Syahdu 5.5 Big Sale
    ========================================
    1. Menambahkan Barang
    2. Menghapus Barang
    3. Melihat Keranjang
    4. Keluar
    """)

def pil():
    opsi=int(input("Pilihan Anda (1/2/3/4): "))
    while opsi != 0:
        if opsi == 1:
            inp=int(input("Jumlah barang yang akan ditambahkan: "))
            for i in range(inp):
                barang=input("Tambahkan barang: ")
                jml=int(input("Jumlah: "))
                keranjang[barang]=jml
            utama()
            pil()
        elif opsi == 2:
            barang=input("Barang yang akan dihapus: ")
            del(keranjang[barang])
            utama()
            pil()
        elif opsi == 3:
            for barang in keranjang:
                print(barang,": ",keranjang[barang])
            utama()
            pil()
        elif opsi == 4:
            print("Anda sudah keluar dari Keranjang Toko Syahdu")
            sys.exit()
        else:
            print("Pilihan Anda tidak tersedia \nSilakan cek ulang.")
            utama()
            pil()

utama()
pil()