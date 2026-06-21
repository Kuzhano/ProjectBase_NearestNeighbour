from math_utils import hitung_jarak_euclidean

def ambil_tetangga_terdekat(data_latih, baris_uji, k_tetangga):
    # Fungsi untuk mencari sejumlah K data latih yang memiliki jarak terdekat dengan data uji.
    koleksi_jarak = list()
    
    for baris_latih in data_latih:
        # Kalkulasi jarak spasial antara titik uji dan titik latih saat ini
        jarak = hitung_jarak_euclidean(baris_uji, baris_latih)
        koleksi_jarak.append((baris_latih, jarak))
        
    # Mengurutkan elemen list berdasarkan jarak (elemen indeks ke-1 pada tuple)
    # dari nilai terkecil (terdekat) ke nilai terbesar
    koleksi_jarak.sort(key=lambda x: x[1])
    
    daftar_tetangga = list()
    
    # Mengambil sejumlah K tetangga teratas dari list yang sudah diurutkan
    for i in range(k_tetangga):
        daftar_tetangga.append(koleksi_jarak[i][0])
        
    return daftar_tetangga

def prediksi_kelas(data_latih, baris_uji, k_tetangga):
    # Fungsi untuk menentukan label kelas akhir menggunakan sistem Majority Voting.
    # Memanggil fungsi pencarian tetangga untuk mendapatkan K data terdekat
    tetangga_terdekat = ambil_tetangga_terdekat(data_latih, baris_uji, k_tetangga)
    
    # Mengekstrak label kelas yang selalu berada di kolom paling akhir (indeks -1)
    label_kumpulan_tetangga = [baris[-1] for baris in tetangga_terdekat]
    
    # Mencari modus (nilai yang paling sering muncul) dari daftar label tetangga
    # set() mengambil nilai unik, count() menghitung frekuensi kemunculannya
    label_pemenang = max(set(label_kumpulan_tetangga), key=label_kumpulan_tetangga.count)
    
    return label_pemenang