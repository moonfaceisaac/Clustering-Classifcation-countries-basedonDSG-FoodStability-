# Clustering-Classifcation-countries-basedonDSG-FoodStability-
Pembagian Tugas:
1.Thobias Zandisko Panjaitan: Preprocessing data, EDA, Data Modelling, Evaluasi Data, Deployment, Laporan, Video
2. Alfajar Alvin Permana Tambunan: Laporan Projek
3. Dimas Marbun: Laporan Projek

Model yang diterapkan:
1.Hierarichal Clustering
2.FNN Deep Learning (Untuk klasifikasi negara berdasarkan yang sudah di cluster

INPUT DATA:
Volatilitas: Simpangan baku dari perubahan harga (semakin tinggi = semakin volatil)
Periode Volatilitas Tinggi: Jumlah periode dengan volatilitas yang sangat tinggi
Peristiwa Positif Ekstrem: Jumlah lonjakan harga besar
Peristiwa Negatif Ekstrem: Jumlah penurunan harga besar
Peristiwa Krisis: Jumlah peristiwa harga pada tingkat krisis
Total Peristiwa Ekstrem: Jumlah seluruh peristiwa ekstrem (positif + negatif)
Ekstrem Positif Maksimum: Lonjakan harga positif terbesar yang teramati
Ekstrem Negatif Maksimum: Penurunan harga negatif terbesar yang teramati
Rata-rata Besaran Ekstrem: Ukuran rata-rata dari peristiwa ekstrem
Skor Stabilitas: Ukuran kebalikan dari volatilitas (semakin tinggi = semakin stabil)
Waktu dalam Rentang Normal: Persentase waktu harga berada dalam batas normal
Kecepatan Pemulihan: Seberapa cepat harga kembali normal setelah guncangan
Skor Konsistensi: Ukuran konsistensi harga dari waktu ke Waktu

OUTPUT DATA:
Cluster 0 (Stable Market)
Cluster 1 (Volatile Market)

LINK PENTING:
[DATASET](https://data.worldbank.org/)
[DEPLOYMENT]([https://data.worldbank.org/](https://foodstability.streamlit.app))

