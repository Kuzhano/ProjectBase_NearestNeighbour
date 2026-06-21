import math

def hitung_jarak_euclidean(baris_a, baris_b):
    jarak_total = 0.0 # Menginisialisasi variabel jarak dengan tipe float 0.0
    
    # Looping melalui semua dimensi (kolom fitur), mengabaikan kolom indeks terakhir (-1)
    for i in range(len(baris_a) - 1):
        # Menghitung selisih nilai fitur, dikuadratkan, lalu ditambahkan ke total
        jarak_total += (baris_a[i] - baris_b[i]) ** 2 
        
    return math.sqrt(jarak_total)