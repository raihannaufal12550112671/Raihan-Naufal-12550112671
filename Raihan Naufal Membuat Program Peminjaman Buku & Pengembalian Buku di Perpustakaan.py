# Nama      : Raihan Naufal
# NIM       : 12550112671
# Kelas     : H
# Dosen     : Muhammad Affandes, S.T., M.T.

class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status_dipinjam = False

    def pinjam(self):
        self.status_dipinjam = True

    def kembalikan(self):
        self.status_dipinjam = False

    def daftar_buku(self):
        status = "Dipinjam" if self.status_dipinjam else "Tersedia"
        print(f"Judul Buku      : {self.judul}")
        print(f"Nama Penulis    : {self.penulis}")
        print(f"Tahun Terbit    : {self.tahun}")
        print(f"Status Dipinjam : {status}")
        print()

class Anggota:
    def __init__(self, nama, nim, id_anggota):
        self.nama = nama
        self.nim = nim
        self.id_anggota = id_anggota
        self.daftar_pinjam = []

    def pinjam_buku(self, buku):
        if not buku.status_dipinjam:
            buku.pinjam()
            self.daftar_pinjam.append(buku)
            print(
                f"\033[92mBuku '{buku.judul}' berhasil dipinjam oleh "
                f"{self.nama} dengan NIM '{self.nim}' ID {self.id_anggota}\033[0m"
            )
        else:
            print(f"\033[91mBuku '{buku.judul}' tidak tersedia karena sedang dipinjam.\033[0m")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_pinjam:
            buku.kembalikan()
            self.daftar_pinjam.remove(buku)
            print(
                f"\033[94mBuku '{buku.judul}' telah dikembalikan oleh "
                f"{self.nama} dengan NIM '{self.nim}' ID {self.id_anggota}\033[0m"
            )
            
    def daftar_anggota(self):
        print(f"Nama            : {self.nama}")
        print(f"NIM             : {self.nim}")
        print(f"ID Anggota      : {self.id_anggota}")
        print()
        
# Data buku
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku2 = Buku("Laut Bercerita", "Leila S. Chudori", 2017)
buku3 = Buku("Pemrograman Python", "Guido van Rossum", 2020)

# Data anggota
anggota1 = Anggota("Raihan", 12550112671, "A001")
anggota2 = Anggota("Naufal", 12550123081, "A030")
anggota3 = Anggota("Reno", 12550136172, "A100")

print("\n\033[38;5;208m----- DAFTAR ANGGOTA PERPUSTAKAAN -----\033[0m\n")
anggota1.daftar_anggota()
anggota2.daftar_anggota()
anggota3.daftar_anggota()

# Proses peminjaman & pengembalian buku
print()
anggota1.pinjam_buku(buku1)
print()
anggota1.kembalikan_buku(buku1)
print()
anggota2.pinjam_buku(buku3)
print()
anggota3.pinjam_buku(buku3)

# Daftar Buku yang ada di Perpustakaan
print("\n\033[33m----- DAFTAR BUKU PERPUSTAKAAN -----\033[0m\n")
buku1.daftar_buku()
buku2.daftar_buku()
buku3.daftar_buku()
