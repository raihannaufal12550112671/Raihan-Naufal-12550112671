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
                f"Buku '{buku.judul}' berhasil dipinjam oleh "
                f"{self.nama} dengan NIM '{self.nim}' ID {self.id_anggota}"
            )
        else:
            print(f"Buku '{buku.judul}' sedang dipinjam.")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_pinjam:
            buku.kembalikan()
            self.daftar_pinjam.remove(buku)
            print(
                f"Buku '{buku.judul}' telah dikembalikan oleh "
                f"{self.nama} dengan NIM '{self.nim}' ID {self.id_anggota}"
            )
            
    def daftar_anggota(self):
        #status = "Dipinjam" if self.status_dipinjam else "Tersedia"
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
anggota2 = Anggota("Reno", 12550126172, "A005")

print("\n----- DAFTAR ANGGOTA PERPUSTAKAAN -----\n")
anggota1.daftar_anggota()
anggota2.daftar_anggota()

# Proses pinjam & kembalikan
print()
anggota1.pinjam_buku(buku1)
print()
anggota1.kembalikan_buku(buku1)
print()
anggota2.pinjam_buku(buku3)

print("\n----- DAFTAR BUKU PERPUSTAKAAN -----\n")
buku1.daftar_buku()
buku2.daftar_buku()
buku3.daftar_buku()
