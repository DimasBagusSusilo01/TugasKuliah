from pynput import keyboard
import threading as th
import sys

class MyDiary():
	def __init__(self):#Menginisialisasi semua variabel yang dibutuhkan
		self.kalimat = ""
		self.HistoryStack = []
		self.RedoStack = []
		self.buffer_kata = ""
		self.kursor = 0
		self.HistoryStack.append(self.buffer_kata)#Menambahkan kosong ke kata sementara supaya kata pertama bisa dihapus.
		
	def updateTulisan(self):
		self.kalimat = self.buffer_kata[:self.kursor]#menulis tiap kata ke jendela
		sys.stdout.write(f"\r{self.kalimat}")
		sys.stdout.flush()

	def simpan(self):
		self.HistoryStack.append(self.buffer_kata)#Menyimpan data ke list HIstoryStack
	
	def pembaca (self, huruf):#fungsi utama dengan beberapa logika:
		self.huruf = huruf
		if self.huruf == keyboard.Key.left:#sensor panah kiri
			if self.HistoryStack:
				self.RedoStack.append(self.buffer_kata)
				self.buffer_kata = self.HistoryStack.pop()
				self.kursor = len(self.buffer_kata)
				self.updateTulisan()
		elif self.huruf == keyboard.Key.right:#sensor panah kanan
			if self.RedoStack:
				self.HistoryStack.append(self.buffer_kata)
				self.buffer_kata = self.RedoStack.pop()
				self.updateTulisan()
		elif self.huruf == keyboard.Key.space:#snesor spasi
			self.simpan()
			self.buffer_kata = self.buffer_kata[:self.kursor] + " " + self.buffer_kata[self.kursor:]
			self.kursor += 1
			self.updateTulisan()
		elif self.huruf == keyboard.Key.esc:#sensor escape
			self.simpan()
			return False
		elif hasattr(self.huruf, 'char') and self.huruf.char is not None:#sensor ketikan per kata
			self.buffer_kata = self.buffer_kata[:self.kursor] + self.huruf.char + self.buffer_kata[self.kursor:]
			self.kursor += 1
			self.updateTulisan()

print ("="*11,"\nMy Diary\n", "="*10)
print ("Tekan panah kiri untuk undo, panah kanan untuk redo dan esc untuk keluar.")

jalankan = MyDiary()
pengamat = keyboard.Listener(on_press=jalankan.pembaca)
pengamat.daemon = True#Multi Threading dengan daemon
pengamat.start()
pengamat.join() #Listener yang akan menghentikan daemon jika ada pemberhenti program yaitu di line 42

print (f"\nHistory Stack: {jalankan.HistoryStack}\nRedo Stack{jalankan.RedoStack}")
