class Sekolah:
    def __init__(self, nama_sekolah, jumlah_siswa, akreditasi, tahun_berdiri):
        self.nama_sekolah = nama_sekolah
        self.__jumlah_siswa = jumlah_siswa   
        self.__akreditasi = akreditasi       
        self.tahun_berdiri = tahun_berdiri

    def get_jumlah_siswa(self):
        return self.__jumlah_siswa

    def set_jumlah_siswa(self, jumlah):
        self.__jumlah_siswa = jumlah

    def get_akreditasi(self):
        return self.__akreditasi

    def set_akreditasi(self, akreditasi):
        self.__akreditasi = akreditasi

    def menerima_murid(self):
        print('-----------------------------------------------------------------------------')
        print(f'{self.nama_sekolah} telah membuka PPDB tahun pelajaran 2045/2046!')
        print(f'Sekolah ini memiliki akreditasi {self.__akreditasi} dan berdiri sejak tahun {self.tahun_berdiri}')
        print('-----------------------------------------------------------------------------')

    def mengeluarkan_murid(self):
        print(f'Maaf anda telah gagal dalam seleksi untuk memasuki {self.nama_sekolah}')
        print(f'Jumlah peserta didik tahun ini adalah {self.__jumlah_siswa}, Semoga bisa menjadi bagian dari {self.nama_sekolah} di kesempatan berikutnya')
        print('-----------------------------------------------------------------------------')

    def merekrut_guru(self):
        print(f'Telah dibuka lowongan guru untuk sekolah {self.nama_sekolah}')
        print('-----------------------------------------------------------------------------')
        print(' ')

sekolah_baru = Sekolah("SMK Python Hebat", 120, "B+", 2010)


print("Jumlah siswa awal:", sekolah_baru.get_jumlah_siswa())
print("Akreditasi awal:", sekolah_baru.get_akreditasi())

sekolah_baru.set_jumlah_siswa(135)
sekolah_baru.set_akreditasi("A")

print("Jumlah siswa setelah diubah:", sekolah_baru.get_jumlah_siswa())
print("Akreditasi setelah diubah:", sekolah_baru.get_akreditasi())

sekolah_baru.menerima_murid()
