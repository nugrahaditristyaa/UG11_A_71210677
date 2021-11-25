print("======== Calculator Sederhana ========")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")

#Mengambil inputan
menu = int(input("Masukan pilihan: "))
bil1 = int(input("Masukan bilangan 1: "))
bil2 = int(input("Masukan bilangan 2: "))

def calculator(menu):
    return menu
def tambah(bil1, bil2):
    return bil1 + bil2
def kurang (bil1, bil2):
    return bil1 - bil2
def kali(bil1, bil2):
    return bil1 * bil2
def bagi(bil1, bil2):
    return bil1/bil2
def pangkat(bil1, bil2):
    return bil1 ** bil2

if menu == 1:
    print("Hasilnya:", tambah(bil1,bil2))
elif menu == 2:
    print("Hasilnya:", kurang(bil1,bil2))
elif menu == 3:
    print("Hasilnya:", kali(bil1,bil2))
elif menu == 4:
    print("Hasilnya:", bagi(bil1,bil2))
elif menu == 5:
    print("Hasilnya:", pangkat(bil1,bil2))
else:
    print("Hasilnya: Maaf input operasi antara 1-5")
