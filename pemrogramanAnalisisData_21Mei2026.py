#magic method digunakan untuk merespon secara otomatis terhadap operasi sistem
#magic method __new__ untuk menciptakan objek baru
#kalau __init__ untuk menginisialisasi atribut ke objek yg dibuat
#__repr__ untuk teknisi atau debugging
#__add__ untuk menggabungkan 2 dataframe atau operasi
#__len__ menghitung panjang data
#__getitem__ memungkinkan akses data spesifik dengan index

class BatchData:
    def __new__(cls, *args):
        print(f"Mengalokasikan memori untuk {cls.__name__}")
        return super().__new__(cls)

    def __init__(self, nama_batch, data_list):
        print (f"menginisialisasi untuk {nama_batch}\n dengan data {data_list}")
        self.nama_batch = nama_batch
        self.data_list = data_list

    def __str__(self):
        return f"Batch {self.nama_batch} memiliki {len(self)} data"
    
    def __len__(self):
        return len(self.data_list)
    
data = BatchData("Batch 1", [1,2,3,4,5])
data2 = BatchData("Periode 1", ["Dewa", "Zaki", "Rizky"])

print (data, '\n', data2)