import MySQLdb as save

db = save.connect(
host = '127.0.0.1',
user = 'root',
password = '',
db = 'Dimaskun'
)
#mengkoneksikan diri dengan localhost atau server lokal (bagian host = '127.0.0.1')
#nama user nya sudah pasti root karena server lokal
#password dikosongi karena emang ngga ada password
cursor = db.cursor()#sebagai penunjuk alias pointer
cursor.execute("CREATE DATABASE Dimaskun")#Membuat database baru bernama #Dimaskun
print ("Database Dimaskun sukses dibuat!")#Konfirmasi
print ('db terkoneksi')
cursor.execute('''
CREATE TABLE dataku(
id INT AUTO_INCREMENT,
nama VARCHAR(20) NOT NULL,
prodi VARCHAR(20) NOT NULL,
PRIMARY KEY(id)
);
''')
print('Tabel berhasil dibuat')

cursor.execute(
'''
INSERT INTO dataku (id, nama, prodi)
VALUES 
	(1, "Dimas Bagus", "Sains data"),
	(2, "Sabrina Rindu", "Psikologi Islam"),
	(3, "Vina Ayu Puspita", "Bahasa Inggris")
''')
print('Data Berhasil Dimasukkan')
