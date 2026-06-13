import csv
import random
from knn_model import prediksi_kelas

def muat_data_csv(path_file):
    """
    Fungsi pembaca file CSV yang mengubahnya menjadi struktur list 2 dimensi.
    """
    kumpulan_data = list() # Inisialisasi list kosong untuk menampung data
    
    with open(path_file, 'r') as file:
        # Tambahkan parameter delimiter agar parser tahu cara memotong kolom
        pembaca = csv.reader(file, delimiter=';')
        next(pembaca, None)

        for baris in pembaca:
            if baris:
                kumpulan_data.append(baris)
                
    return kumpulan_data

def konversi_string_ke_angka(dataset):
    """
    Mengubah data CSV yang secara default dibaca sebagai String menjadi Float/Integer.
    Fungsi ini berjalan secara in-place (mengubah objek asli di memori).
    """
    jumlah_kolom = len(dataset[0]) # Mengidentifikasi jumlah dimensi kolom

    for baris in dataset:
        for i in range(jumlah_kolom):
            baris[i] = float(baris[i].strip())


if __name__ == "__main__":
    # 1. Konfigurasi Awal
    nama_file_dataset = 'kc2.csv'
    K_VALUE = 5 # Parameter jumlah tetangga (ditetapkan ganjil untuk cegah seri)
    
    try:
        # 2. Proses Pemuatan dan Pembersihan Data
        print(f"[*] Memuat dataset {nama_file_dataset}...")
        dataset_mentah = muat_data_csv(nama_file_dataset)
        konversi_string_ke_angka(dataset_mentah)
        
        # 3. Pengacakan Data (Mencegah bias dari urutan data asli dari NASA)
        random.seed(42) # Menetapkan seed agar hasil acak konsisten saat diuji ulang
        random.shuffle(dataset_mentah)
        
        # 4. Pembagian Data (Splitting): 80% Training, 20% Testing
        indeks_potong = int(len(dataset_mentah) * 0.8)
        data_training = dataset_mentah[:indeks_potong]
        data_testing = dataset_mentah[indeks_potong:]
        
        print(f"[*] Total Data: {len(dataset_mentah)} baris")
        print(f"[*] Data Latih: {len(data_training)} baris | Data Uji: {len(data_testing)} baris")
        print(f"[*] Menjalankan klasifikasi KNN dengan K={K_VALUE}...\n")
        
        # 5. Siklus Evaluasi
        jumlah_prediksi_tepat = 0
        
        for baris_uji in data_testing:
            label_aktual = baris_uji[-1] # Ground truth berada di kolom terujung
            
            # Memanggil fungsi klasifikasi untuk menebak status cacat kode
            label_tebakan = prediksi_kelas(data_training, baris_uji, K_VALUE)
            
            # Membandingkan hasil tebakan algoritma dengan data historis sebenarnya
            if label_tebakan == label_aktual:
                jumlah_prediksi_tepat += 1
                
        # 6. Komputasi Akurasi Akhir
        persentase_akurasi = (jumlah_prediksi_tepat / float(len(data_testing))) * 100.0
        
        print("=== HASIL EVALUASI MODEL ===")
        print(f"Prediksi Benar : {jumlah_prediksi_tepat} dari {len(data_testing)} data")
        print(f"Akurasi Sistem : {persentase_akurasi:.2f}%")

    except FileNotFoundError:
        print(f"[!] Error Kritis: File {nama_file_dataset} tidak ditemukan di direktori eksekusi.")
    except ValueError as e:
        print(f"[!] Error Parsing: Terdapat data non-numerik yang gagal dikonversi. Detail: {e}")