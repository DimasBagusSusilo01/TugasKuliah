#listdata = [7,20,25,36,42,51,64,76,83,99,100]

import random

demand = int(input('Berapa banyak permintaan data? '))
angka_acak = random.sample(range(1,100),demand)
listdata = sorted(angka_acak)
print (f'list datanya: {listdata}')
subjek = int(input('Ingin nyari lokasi angka berapa? '))

def bst_simulasi(data, level=0):
    if len(data) == 0:
        return
    
    tengah = len(data) // 2
    root = data[tengah]

    print("   " * level + f"Root: {root}")

    kiri = data[:tengah]
    kanan = data[tengah+1:]

    print("   " * level + f"Kiri : {kiri}")
    print("   " * level + f"Kanan: {kanan}")
    print()

    bst_simulasi(kiri, level + 1)
    bst_simulasi(kanan, level + 1)

bst_simulasi(listdata)

def cari_bst(data, target, level=0, parent=None, posisi="Root"):
    if not data:
        print ('data tidak ada')
    
    mid = len(data) // 2
    root = data[mid]

    if root == target:
        print(f"Nilai ditemukan: {target}")
        print(f"Level : {level}")
        print(f"Posisi: {posisi}")
        print(f"Parent: {parent}")
        return

    if target < root:
        cari_bst(data[:mid],target,level + 1,root,
            "Kiri")

    else:
        cari_bst(data[mid+1:],target,level + 1,root,
            "Kanan")

cari_bst(listdata, subjek)
