#import data
import pandas as pd
import math

mobil = pd.read_excel('Mobil.xls')
mobil

#definisi data
nama = mobil['Nama Mobil']
ukuran = mobil['Ukuran']
kenyamanan = mobil['Kenyamanan']
irit = mobil['Irit']
kecepatan = mobil['Kecepatan']
harga = mobil['Harga (Ratus Juta)']

print('Masukkan ciri-ciri mobil')
inukur = input('Ukuran: ')
inken = input('Kenyamanan: ')
inir = input('Irit: ')
inkec = input('Kecepatan: ')
inhar = input('Harga: ')
print('')
n = len(mobil)

#Euclidean
x = []
for i in range(n):
  fixukur = (ukuran[i] - float(inukur)) ** 2
  fixken = (kenyamanan[i] - float(inken)) ** 2
  fixir = (irit[i] - float(inir)) ** 2
  fixkec = (kecepatan[i] - float(inkec)) ** 2
  fixhar = (harga[i] - float(inhar)) ** 2

  jarak = math.sqrt(fixukur+fixken+fixir+fixkec+fixhar)
  print(nama[i], jarak)
  x.append([nama[i] ,jarak])

#Manhattan
x = []
for i in range(n):
  fixukur = (ukuran[i] - float(inukur)) ** 2
  fixken = (kenyamanan[i] - float(inken)) ** 2
  fixir = (irit[i] - float(inir)) ** 2
  fixkec = (kecepatan[i] - float(inkec)) ** 2
  fixhar = (harga[i] - float(inhar)) ** 2
  
  jarak = abs(fixukur+fixken+fixir+fixkec+fixhar)
  print(nama[i], jarak)
  x.append([nama[i] ,jarak])

#Minkowski
x = []
p = 3
for i in range(n):
  fixukur = (ukuran[i] - float(inukur)) ** p
  fixken = (kenyamanan[i] - float(inken)) ** p
  fixir = (irit[i] - float(inir)) ** p
  fixkec = (kecepatan[i] - float(inkec)) ** p
  fixhar = (harga[i] - float(inhar)) ** p

  jarak = abs(fixukur+fixken+fixir+fixkec+fixhar)**(1/p)
  print(nama[i], jarak)
  x.append([nama[i] ,jarak])

#supremum
x = []
for i in range(n):
  fixukur = abs(ukuran[i] - float(inukur))
  fixken = abs(kenyamanan[i] - float(inken))
  fixir = abs(irit[i] - float(inir))
  fixkec = abs(kecepatan[i] - float(inkec))
  fixhar = abs(harga[i] - float(inhar))

  jarak = max(fixukur, fixken, fixir, fixkec, fixhar)
  print(nama[i], jarak)
  x.append([nama[i] ,jarak])

terurut = sorted(x, key = lambda x: x[1], reverse=False)
merek = [x[0] for x in terurut[:3]]
hasil_csv = {'Mobil yang direkomendasikan': merek}
result_csv = pd.DataFrame(hasil_csv, columns = ['Mobil yang direkomendasikan'])
result_csv.to_csv('Rekomendasi.csv')
print(hasil_csv)