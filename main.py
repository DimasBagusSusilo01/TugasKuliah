from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import time

import numpy as np
import re
from scipy.linalg import solve

class Proses(Screen):
	def on_enter(self):
		Clock.schedule_interval(self.proses, 0.1)
		
	def proses(self, waktu):
		if self.ids.Progress_Bar.value < 100:
			self.ids.Progress_Bar.value += 4
		else:
			self.manager.current = 'Utama'
			return False
			
class Aljabar(Screen):
	def hitung(self):
		self.user = self.ids.persamaan.text
		self.list_utama = re.split(r',',self.user)
		
		self.listhasil = []
		for item in self.list_utama:
			self.komponen = re.findall(r'-?\d*[a-zA-Z]+|-?\d+', item)
			self.listhasil.append(self.komponen)
			
		self.listbaru = []
		for baris in self.listhasil:
			self.baris_baru = []
			for elemen in baris:
				if re.fullmatch(r'[a-zA-Z]+', elemen):       
					self.baris_baru.append('1')
				elif re.fullmatch(r'-[a-zA-Z]+', elemen):   
					self.baris_baru.append('-1')
				else:                                       
					self.baris_baru.append(re.sub(r'[a-zA-Z]', '', elemen))
            
		self.listbaru.append(self.baris_baru)
		
		self.list_y = []
		for self.ye in self.listbaru:
			self.list_y.append(self.ye[-1])
	
		self.list_x = [sub_list[:-1] for sub_list in self.listbaru]
		self.kesimpulan = solve(self.list_x, self.list_y)
		self.ids.Hasil.text = self.kesimpulan
		
	def kembali(self):
		self.manager.current = 'Utama'
		return False

class Utama(Screen):
	def ganti_halaman(self):
		self.manager.current = 'Aljabar'
		return False
		
class windowManager(ScreenManager):
	pass

class main(App):
	def build(self):
		return windowManager()
		
if __name__ == "__main__":
	main().run()
