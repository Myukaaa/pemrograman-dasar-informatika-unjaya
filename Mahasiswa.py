class Mahasiswa:
    def __init__(self, nama, nim, prodi, hobi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.hobi = hobi

    def display_profile(self):
        print("Profil Mahasiswa:")
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Program Studi:", self.prodi)
        print("Hobi:", self.hobi)

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("Puji Winar Cahyo", "17000040", "Teknik Informatika", "Coding")

# Menampilkan profil mahasiswa
mahasiswa1.display_profile()
