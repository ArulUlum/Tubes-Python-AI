import pandas as pd

resto = pd.read_excel("restoran.xlsx")
resto

id = resto["id"]
pelayanan = resto["pelayanan"]
makanan = resto["makanan"]

y = []

for x in range(100):
  nilaiM = [0, 0, 0, 0, 0]
  nilaiP = [0, 0, 0, 0, 0]
  sangatburuk = buruk = baik = sangatbaik = jelek = biasa = enak = 0

  if pelayanan[x] <= 25:
      sangatburuk = 1
      nilaiP[0] = sangatburuk
  elif pelayanan[x] > 25 and pelayanan[x] < 30:
      sangatburuk = (30 - pelayanan[x]) / 5
      buruk = (pelayanan[x] - 25) / 5
      nilaiP[0] = sangatburuk
      nilaiP[1] = buruk
  elif pelayanan[x] >= 30 and pelayanan[x] <= 50:
      buruk = 1
      nilaiP[1] = buruk
  elif pelayanan[x] > 50 and pelayanan[x] < 55:
      buruk = (55 - pelayanan[x]) / 5
      baik =  (pelayanan[x] - 50) / 5
      nilaiP[1] = buruk
      nilaiP[2] = baik
  elif pelayanan[x] >= 55 and pelayanan[x] <= 75:
      baik = 1
      nilaiP[2] = baik
  elif pelayanan[x] > 75 and pelayanan[x] < 80:
      baik = (80 - pelayanan[x]) / 5
      sangatbaik = (pelayanan[x] - 75) / 5
      nilaiP[2] = baik
      nilaiP[3] = sangatbaik
  elif pelayanan[x] >= 80:
      sangatbaik = 1
      nilaiP[3] = sangatbaik
  
  if makanan[x] <= 2:
      jelek = 1
      nilaiM[0] = jelek
  elif makanan[x] > 2 and makanan[x] < 4:
      jelek = (4 - makanan[x]) / 2
      biasa = (makanan[x] - 2) / 2
      nilaiM[0] = jelek
      nilaiM[1] = biasa
  elif makanan[x] >= 4 and makanan[x] <= 6:
      biasa = 1
      nilaiM[1] = biasa
  elif makanan[x] > 6 and makanan[x] < 8: 
      biasa = (8 - makanan[x]) / 2
      enak = (makanan[x] - 6) / 2
      nilaiM[1] = biasa
      nilaiM[2] = enak
  elif makanan[x] >= 8 and makanan[x] <= 10:
      enak = 1
      nilaiM[2] = enak

  NR = []
  i = 0
  if nilaiM[0] == jelek and nilaiP[0] == sangatburuk :
    i = i + 1
    NR.append(min(nilaiP[0], nilaiM[0]))
  if nilaiM[1] == biasa and nilaiP[0] == sangatburuk :
    i = i + 1
    NR.append(min(nilaiP[0], nilaiM[1]))
  if nilaiM[0] == jelek and nilaiP[1] == buruk :
    i = i + 1
    NR.append(min(nilaiP[1], nilaiM[0]))
  if nilaiM[0] == jelek and nilaiP[2] == baik :
    i = i + 1
    NR.append(min(nilaiP[2], nilaiM[0]))
  nilaiNR = max(NR)
    
  R = []
  i = 0
  if nilaiM[2] == enak and nilaiP[0] == sangatburuk :
    i = i + 1
    R.append(min(nilaiP[0], nilaiM[2]))
  if nilaiM[1] == biasa and nilaiP[1] == buruk :
    i = i + 1
    R.append(min(nilaiP[1], nilaiM[1]))
  if nilaiM[1] == biasa and nilaiP[2] == baik :
    i = i + 1
    R.append(min(nilaiP[2], nilaiM[1]))
  if nilaiM[0] == jelek and nilaiP[3] == sangatbaik :
    i = i + 1
    R.append(min(nilaiP[3], nilaiM[0]))
  nilaiR = max(R)

  SR = []
  i = 0
  if nilaiM[2] == enak and nilaiP[1] == buruk :
    i = i + 1
    SR.append(min(nilaiP[1], nilaiM[2]))
  if nilaiM[2] == enak and nilaiP[2] == baik :
    i = i + 1
    SR.append(min(nilaiP[2], nilaiM[2]))
  if nilaiM[1] == biasa and nilaiP[3] == sangatbaik :
    i = i + 1
    SR.append(min(nilaiP[3], nilaiM[1]))
  if nilaiM[2] == enak and nilaiP[3] == sangatbaik :
    i = i + 1
    SR.append(min(nilaiP[3], nilaiM[2]))
  nilaiSR = max(SR)

  pembagi = nilaiNR+nilaiR+nilaiSR
  z = ((nilaiNR*25)+(nilaiR*50)+(nilaiSR*100)) / pembagi
  print(id[x], z)
  y.append([id[x], z])

hasil_akhir = sorted(y, key = lambda x: x[1], reverse=True)
hasil_csv = {'restoran terbaik': hasil_akhir[:10]}

result_csv = pd.DataFrame(hasil_csv, columns = ['restoran terbaik'])
result_csv.to_csv('Peringkat.csv')
print(hasil_akhir)
