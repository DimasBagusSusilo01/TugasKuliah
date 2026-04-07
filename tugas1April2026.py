from pynput import keyboard
import threading as th
import sys

HistorySTack = []
RedoStack = []
buffer_kata = ""
kursor = 0

HistorySTack.append(buffer_kata)

def updateTulisan():
	kalimat = ""
	kalimat += buffer_kata[:kursor]
	sys.stdout.write(f"\r{kalimat}")
	sys.stdout.flush()

def simpan():
	HistorySTack.append(buffer_kata)
	
def pembaca (huruf):
	global buffer_kata, kursor
	if huruf == keyboard.Key.left:
		if HistorySTack:
			RedoStack.append(buffer_kata)
			buffer_kata = HistorySTack.pop()
			kursor = len(buffer_kata)
			updateTulisan()
	elif huruf == keyboard.Key.right:
		if RedoStack:
			HistorySTack.append(buffer_kata)
			buffer_kata = RedoStack.pop()
			updateTulisan()
	elif huruf == keyboard.Key.space:
		simpan()
		buffer_kata = buffer_kata[:kursor] + " " + buffer_kata[kursor:]
		kursor += 1
		updateTulisan()
	elif huruf == keyboard.Key.esc:
		simpan()
		return False
	elif hasattr(huruf, 'char') and huruf.char is not None:
		buffer_kata = buffer_kata[:kursor] + huruf.char + buffer_kata[kursor:]
		kursor += 1
		updateTulisan()

print ("="*11,"\nMy Diary\n", "="*10)
print ("Tekan panah kiri untuk undo, panah kanan untuk redo dan esc untuk keluar.")
	
pengamat = keyboard.Listener(on_press=pembaca)
pengamat.daemon = True
pengamat.start()

pengamat.join()
print (f"\nHistory Stack: {HistorySTack}\nRedo Stack{RedoStack}")
