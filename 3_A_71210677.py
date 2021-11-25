#Mengambil inputan
a1 = input("Masukan Kalimat: ")
b2 = int(input("Index Start: "))
c3 = int(input("Index Stop: "))

def hitung_hapus(a1,b2,c3):
    h1 = len(a1)
    h2 = len(a1[b2-1:c3])
    hasil = (h2 / h1)*100
    return hasil
print(hitung_hapus(a1,b2,c3))
