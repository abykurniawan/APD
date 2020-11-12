import os
import datetime
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def date_time():
    x = datetime.datetime.now()
    print("\nTanggal saat ini :",x.day,"/",x.month,"/",x.year)
    print("Waktu saat ini   :" ,x.hour,":",x.minute,":",x.second)
    if x.hour >= 1 and x.hour < 12:
        print("\nSelamat Pagi")
    elif x.hour >=12 and x.hour < 15:
        print("\nSelamat Siang")
    elif x.hour >=15 and x.hour < 18:
        print("\nSelamat Sore")
    else:
        print("\nSelamat Malam")
    print ("========================================") 
    bio()

def welcome():
    clear_screen()
    print ("========================================")
    print ("    Program Sederhana Dengan Python    ")
    print ("Selamat Datang di Lobby Kesayangan Anda")
    print ("========================================")
    date_time()

def bio() :
    nama   = input("Masukkan nama   : ")
    alamat = input("Masukkan alamat : ")
    hobi   = input("Masukkan hobi   : ")
    umur   = input("Masukkan umur   : ")
    print ("====================================================================")
    print ("Halo, Saya %s, alamat saya %s, hobi saya %s, dan umur saya %s tahun" % (nama, alamat, hobi, umur))
    print ("====================================================================")
    print ("Terima kasih telah memasukkan biodata Anda")
    perhitungan()

def perhitungan():
    print ("====================================================================")
    print ("\nBerikut contoh Program Operator Aritmatika Sederhana")
    #Aritmatika Perbandingan sama dengan
    print ("=======================================================")
    print ("\tAritmatika Perbandingan sama dengan")
    print ("=======================================================")
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a == b
    print("Hasil %d == %d = %s" % (a,b,c))

    #Aritmatika Perbandingan nilai lebih besar
    print ("=======================================================")
    print ("\tAritmatika Perbandingan nilai lebih besar")
    print ("=======================================================")
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a > b
    print("Hasil %d > %d = %s" % (a,b,c))

    #Aritmatika Perbandingan nilai lebih kecil
    print ("=======================================================")
    print ("\tAritmatika Perbandingan nilai lebih kecil")
    print ("=======================================================")
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a < b
    print("Hasil %d < %d = %s" % (a,b,c))

    #Aritmatika Perkalian
    print ("=======================================================")
    print ("\tAritmatika Perkalian")
    print ("=======================================================")
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a * b
    print("Hasil %d * %d = %d" % (a,b,c))

    #Aritmatika Pembagian
    print ("=======================================================")
    print ("\tAritmatika Pembagian")
    print ("=======================================================")
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a / b
    print("Hasil %d / %d = %d" % (a,b,c))

    #Aritmatika Pengurangan
    print ("=======================================================")
    print ("\tAritmatika Pengurangan")
    print ("=======================================================")
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a - b
    print("Hasil %d - %d = %d" % (a,b,c))

    #Aritmatika Penjumlahan
    print ("=======================================================")
    print ("\tAritmatika Penjumlahan")
    print ("=======================================================")
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a + b
    print("Hasil %d + %d = %d" % (a,b,c))
    exit()
    
if __name__ == "__main__": 
    while True:
        welcome()
