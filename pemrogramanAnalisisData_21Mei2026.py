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
    
    def __add__(self, total_data):
        print (f"Proses menggabungkan {self.nama_batch}, dan {total_data.nama_batch}")
        nama_batch = self.nama_batch + total_data.nama_batch
        data_list = self.data_list + total_data.data_list
        return BatchData(nama_batch, data_list)
    
#data = BatchData("Batch 1 ", [1,2,3,4,5])
#data2 = BatchData("Periode 1 ", ["Dewa", "Zaki", "Rizky"])
#data3 = BatchData("Kelas 1", ["UNDIP", "UIN", "UIN"])

#print (data, '\n', data2, "\n", data3)

#total_data = data + data2 + data3
#print (total_data)

import time
#tanpa dekorator
#def latih_model(nama_model, jumlah_data):
#    start = time.time()

#    print ("Waktu mulai: ", nama_model, jumlah_data)
#    time.sleep(2)

#    end = time.time()
#    durasi = end - start
#    print(f"{durasi:.2f}")

#hasil = latih_model("Random Forest", jumlah_data=5000)

#Fungsi dekoratif
def hitung_durasi(fungsi_asli):
    def pembungkus(*args, **kwargs):
        start = time.time()

        #print ("Waktu mulai: ", nama_model, jumlah_data)
        #time.sleep(2)
        hasil = fungsi_asli(*args, *kwargs)
        end = time.time()
        durasi = end - start
        print(f"{durasi:.2f}")
        return hasil
    return pembungkus

@hitung_durasi
def latih_model(nama_model, jumlah_data):
    print (nama_model)
    print (jumlah_data)
    time.sleep(2)

if __name__ == "__main__":
    print ("SIMULASI")
    hasil_sistem = latih_model("random forest", jumlah_data=5000)