import pandas as pd

df0 = pd.read_csv("data_mahasiswa_mentah.csv")
#Untuk menentukan isi pemisah antar sel, bisa:
#pd.read_csv('',sep='(bisa , atau spasi atau ;)', skiprows=angka, index_col='nama judul kolom')

#Jika ingin membaca excel, maka:
#df0 = pd.read_excel()
df = pd.DataFrame({
	"Nama" : [
		"Andika Dewa Priyana",
		"Dimas Bagus Susilo",
		"Muhammad Maslah Rozaqi",
		"Muhammad Hasan Qulub"],
	"Nilai" : [
		80, 100, 90, 85
	],	
})

#df.to_csv('Belajar16April.csv', index=False)
#Series dalam pandas adalah satu baris atau kolom
#Kumpulan series yang membentuk tabel(tabular) disebut DataFrame
#print (df)
#print(df)
print (df0)
#print(df0.head())#Pilih head untuk 5 baris dari atas, dan tail untuk 5 baris dari bawah
#head dan tail bisa dicustom berapa baris dengan mengisi angka di head(angka)
#print(df0.info())#Untuk mencari info dari dataframe. Ada output
#Non-null count untuk mencari berapa missing values dalam kolom. Caranya dengan
#mengurangi index dengan non-null count

#print (df0.describe())#Untuk melihat secara ringkas informasi matematika nya. Seperti mean, min, max
#Dan standar Deviasi

#print(df0['Nama'])
#df_baru = df0[['Nama', 'NIM', 'Jurusan']]
#print (df_baru)
#print (df_baru.dtypes)
#print (df0.iloc[6:])
#iloc digunakan untuk mencetak baris tertentu.
#Gunakan iloc[angka] untuk spesifik baris mana,
#gunakan iloc[angka1:angka2] untuk range dari angka1 ke angka2
#gunakan iloc[:angka1] untuk mencetak baris dari atas sebanyak angka1
#gunakan iloc[angka2:] untuk mencetak baris dari bawah sebanyak angka2
#print (df0[['Nama', 'NIM', 'Jurusan']].iloc[:6])

#print(df0['Nilai_Tugas'] > 88) Untuk memfilter angka yang lebih dari 88
#print(df0.loc[:, 'NIM'])#Untuk mencari baris atau kolom spesifik ke judul atau nama baris/kolom.

#print (df.shape)

#print (df0.isna().sum())#Menghitung jumlah nilai kosong atau missingvalue dari dataframe

#print(df0.dropna(subset=('Kehadiran')))#Menghapus baris missing values
print (df0['Nilai_Ujian'].fillna('Null')) #Mengisi NaN dengan yang diinginkan
print (df0.drop_duplicates()) #menghapus duplikasi
