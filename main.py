import csv
import random
from knn_model import prediksi_kelas

def muat_data_csv(path_file):
    kumpulan_data = list() 
    with open(path_file, 'r') as file: 
        pembaca = csv.reader(file, delimiter=';') 
        next(pembaca, None) 
        for baris in pembaca: 
            if baris: 
                kumpulan_data.append(baris) 
    return kumpulan_data

def konversi_string_ke_angka(dataset):
    jumlah_kolom = len(dataset[0])
    for baris in dataset:
        for i in range(jumlah_kolom):
            baris[i] = float(baris[i].strip())

if __name__ == "__main__":
    nama_file_dataset = 'kc2.csv' 
    K_VALUE = 5 
    
    try:
        print(f"[*] Memuat dataset {nama_file_dataset}...")
        dataset_mentah = muat_data_csv(nama_file_dataset)
        konversi_string_ke_angka(dataset_mentah)
        
        random.seed(42) 
        random.shuffle(dataset_mentah)
        
        indeks_potong = int(len(dataset_mentah) * 0.8)
        data_training = dataset_mentah[:indeks_potong]
        data_testing = dataset_mentah[indeks_potong:]
        
        print(f"[*] Menjalankan klasifikasi KNN dengan K={K_VALUE}...\n")
        
        # Inisialisasi variabel Confusion Matrix
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        
        for baris_uji in data_testing:
            label_aktual = baris_uji[-1]
            label_tebakan = prediksi_kelas(data_training, baris_uji, K_VALUE)
            
            # Klasifikasi ke dalam Confusion Matrix
            # Asumsi: 1.0 adalah Positif (Cacat), 0.0 adalah Negatif (Aman)
            if label_tebakan == 1.0 and label_aktual == 1.0:
                TP += 1
            elif label_tebakan == 0.0 and label_aktual == 0.0:
                TN += 1
            elif label_tebakan == 1.0 and label_aktual == 0.0:
                FP += 1
            elif label_tebakan == 0.0 and label_aktual == 1.0:
                FN += 1
                
        # Menghitung Metrik Performa dengan penanganan ZeroDivisionError
        total_uji = TP + TN + FP + FN
        
        akurasi = (TP + TN) / total_uji if total_uji > 0 else 0
        tpr = TP / (TP + FN) if (TP + FN) > 0 else 0
        fpr = FP / (FP + TN) if (FP + TN) > 0 else 0
        tnr = TN / (FP + TN) if (FP + TN) > 0 else 0
        fnr = FN / (TP + FN) if (TP + FN) > 0 else 0
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        
        f1_measure = (2 * precision * tpr) / (precision + tpr) if (precision + tpr) > 0 else 0
        
        # Menampilkan Laporan Metrik
        print("=== CONFUSION MATRIX ===")
        print(f"True Positif (TP)  : {TP}")
        print(f"True Negatif (TN)  : {TN}")
        print(f"False Positif (FP) : {FP}")
        print(f"False Negatif (FN) : {FN}\n")
        
        print("=== PERFORMANCE METRICS ===")
        print(f"Accuracy                 : {akurasi * 100:.2f}%")
        print(f"True Positif Rate (TPR)  : {tpr * 100:.2f}%")
        print(f"True Negatif Rate (TNR)  : {tnr * 100:.2f}%")
        print(f"False Positif Rate (FPR) : {fpr * 100:.2f}%")
        print(f"False Negatif Rate (FNR) : {fnr * 100:.2f}%")
        print(f"Precision                : {precision * 100:.2f}%")
        print(f"F1-Measure               : {f1_measure * 100:.2f}%")

    except FileNotFoundError:
        print(f"[!] Error: File {nama_file_dataset} tidak ditemukan.")
    except Exception as e:
        print(f"[!] Error Eksekusi: {e}")