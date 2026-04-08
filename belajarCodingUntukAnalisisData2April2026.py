#Numerical Python (Numpy)
import numpy as np

#data_list = [1,2,3,4,5]
#data_array0 = np.array([[data_list]])
#print (f"ini adalah data list: {data_list}.\nini adalah data numpy{data_array}.")
#data_array = np.zeros((2,5))#membuat sejumlah kolom array bernilai 0.
#print (data_array.ndim) #menghitung jumlah dimensi array
#data_satu = np.ones((6,8))
#print (data_satu.ndim)
#Sama halnya dengan np.ones((2,3)). Namun isinya diganti angka 1
#print (data_array)
#print (data_satu)
#print (data_array0.shape)

#urutan = np.arange(8) #output urut 1 - 7
#urutan2 = np.arange(1, 20, 3) #parameter 1=angkapertama, 2= angkaterakhir, 3=lompatan angka
#print(f"{urutan}\n{urutan2}")
#baru = np.linspace(7,25,10)
#print (baru)

#acak2 = np.random.randint(1,100,5)
#print (f"{acak2}")

#matriksnol = np.zeros((5,6))
#print (matriksnol.shape)
#print (matriksnol.size)
#print (matriksnol.dtype)

#arr = np.arange(6)
#print (arr.reshape(2,1,3))

#Ada beda antara perkalian matriks dengan * dan np.dot. Kalau
#* berarti matriks dikalikan per elemen.
#Kalau np.dot(A, B) maka perkalian aljabar diterapkan.
A = np.array([[2,3], [4,5]])
B = np.array([[6,7], [8,9]])
print (np.dot(A,B))

#Untuk pangkat pakai np.square(array) atau array ** angka
#Untuk akar pakai np.sqrt(array)

#np.min(array) berguna untuk mencari nilai terkecil array
#np.max(array) berguna untuk mencari nilai terbesar array
#array.argmin() berguna untuk mencari lokasi nilai terkecil array
#array.argmax() berguna untuk mencari lokasi nilai terbesar array

#np.mean(array) untuk mencari rata rata
#np.mean(array, axis=0) sama namun secara menurun. untuk mendatar axis = 1
#np.median(array) mencari nilai tengah elemen array
#np.std(array) untuk mencari standar deviasi/sebaran data

#np.sum(data) digunakan untuk menjumlahkan semua data array
