import random #untuk merandom angka
import math #untuk proses matematika

lower_x1 = -1 #batas chromosome
upper_x1 = 2
lower_x2 = -1
upper_x2 = 1
populasi = [] #array dari populasi, populasi genetic
generasi = 1 #inisiasi generasi

def h(x,y): #rumus dari soal
    cosx = math.cos(x*x)
    cosy = math.sin(y*y)
    return (cosx * cosy) + (x+y)

class chromosome: #untuk buat chromosome
    def __init__(self, bit = None):
        if bit == None:
            self.bit = random.choices([0, 1], k=6) #ngerandom bit chromosome
        else:
            self.bit = bit
        self.x1 = self.encoding(upper_x1, lower_x1, self.bit[:3]) #untuk posisi bit 1 pada 3 bit pertama
        self.x2 = self.encoding(upper_x2, lower_x2, self.bit[3:]) #untuk 3 bit terakhir
    def encoding(self, rangeatas, rangebawah, g): #untuk representasi biner chromosome
        tp = [2**-i for i in range(1, len(g) + 1)]
        return rangebawah + ((rangeatas-rangebawah)/sum(tp) * sum([g[i]*tp[i] for i in range(len(g))]))

def f(x1, x2):
    return h(x1,x2) #fungsi fitness untuk maksimasi

def seleksi_orangtua(k): #
    orangtua = []
    fitness = list(map(lambda c: f(c.x1, c.x2),populasi)) #untuk menentukan fitness
    weight = [fitness[i]/sum(fitness)for i in range(len(populasi))] #presentase fitness 
    while len(orangtua) != k: #roulette wheel
        kandidat = random.choices(populasi, weights=weight)[0]
        orangtua.append(kandidat)
    return orangtua

def kawin(ortu1, ortu2):
    posisi = random.randint(1, len(ortu1.bit) - 2)
    bit_anak1 = ortu1.bit[:posisi]+ortu2.bit[posisi:] #crossover bit ortu ke anak
    bit_anak2 = ortu1.bit[posisi:]+ortu2.bit[:posisi]
    range_mutasi = random.uniform(0, 100)
    if range_mutasi > (100 - 0.5):#range mutasi
        posisi_mutasi = random.randint(0, len(bit_anak1))
        if bit_anak1[posisi_mutasi] == 1: #mutasi biner
            bit_anak1[posisi_mutasi] = 0
        else:
            bit_anak1[posisi_mutasi] = 1
    range_mutasi = random.uniform(0, 100)
    if range_mutasi > (100 - 0.5):
        posisi_mutasi = random.randint(0, len(bit_anak2))
        if bit_anak2[posisi_mutasi] == 1:
            bit_anak2[posisi_mutasi] = 0
        else:
            bit_anak2[posisi_mutasi] = 1
    populasi.append(chromosome(bit_anak1))
    populasi.append(chromosome(bit_anak2))

def seleksi_survivor():
    populasi.sort(key= lambda c: h(c.x1, c.x2)) #sort fitness
    populasi.pop(0)
    populasi.pop(1)

while len(populasi) != 5:
    c = chromosome()
    populasi.append(c)

def cetak_populasi():
    for i in populasi:
        print("Generasi: ", generasi)
        print("Bit chromosome: ", i.bit)
        print("Populasi: ", populasi)
        print("Anak1: ", i.x1)
        print("Anak2: ", i.x2)
        print("Fitness: ", f(i.x1, i.x2))
        print("\n")
while generasi <= 5:
    orangtua = seleksi_orangtua(2)
    print("chromosome orang tua: ", orangtua)
    kawin(orangtua[0], orangtua[1]) 
    seleksi_survivor()
    cetak_populasi()
    generasi = generasi + 1