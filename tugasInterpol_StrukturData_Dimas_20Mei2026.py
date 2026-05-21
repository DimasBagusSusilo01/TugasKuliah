#listdata = [7,20,25,36,42,51,64,76,83,99,100]
import random

print("="*8,'\n', "Interpolator",'\n',"="*8)
demand = int(input('Berapa data yang ingin dibuat? '))
data_acak = random.sample(range(1,100),demand)
list_data = sorted(data_acak)
print (list_data)
subjek = int(input("Masukkan angka target: "))
rumus = list_data.index(min(list_data)) + ((subjek - list_data[0])/(list_data[-1]-list_data[0])) * (list_data.index(max(list_data)) - list_data.index(min(list_data)))

print (round(rumus))
