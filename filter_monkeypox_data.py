import os
import pandas as pd

# Membaca dataset
file_path = 'data/raw_data/original/monkeypox.csv'  # Ganti dengan nama file Anda
data = pd.read_csv(file_path)

# Pastikan kolom 'date' dalam format datetime
data['date'] = pd.to_datetime(data['date'])

# Meminta input rentang tahun dan bulan dari pengguna
while True:
    try:
        # Input untuk tahun dan bulan awal
        start_year = int(input("Masukkan tahun awal (contoh: 2022): "))
        start_month = int(input("Masukkan bulan awal (1-12): "))

        # Input untuk tahun dan bulan akhir
        end_year = int(input("Masukkan tahun akhir (contoh: 2024): "))
        end_month = int(input("Masukkan bulan akhir (1-12): "))

        # Validasi input
        if start_month < 1 or start_month > 12 or end_month < 1 or end_month > 12:
            print("Bulan harus antara 1 dan 12. Silakan coba lagi.")
        elif start_year > end_year or (start_year == end_year and start_month > end_month):
            print("Tanggal awal tidak boleh lebih besar dari tanggal akhir. Silakan coba lagi.")
        else:
            break
    except ValueError:
        print("Input tidak valid. Masukkan angka tahun dan bulan (contoh: 2022 dan 5 untuk Mei).")

# Filter data untuk rentang tahun dan bulan yang dipilih
filtered_data = data[
    (data['date'].dt.year > start_year) | 
    ((data['date'].dt.year == start_year) & (data['date'].dt.month >= start_month)) & 
    (data['date'].dt.year < end_year) | 
    ((data['date'].dt.year == end_year) & (data['date'].dt.month <= end_month))
]

# Periksa apakah ada data untuk rentang tahun dan bulan tersebut
if filtered_data.empty:
    print(f"Tidak ada data untuk rentang {start_month}/{start_year} hingga {end_month}/{end_year}.")
else:
    # Path folder untuk menyimpan hasil
    output_folder = 'data/raw_data/filtered'
    os.makedirs(output_folder, exist_ok=True)  # Buat folder jika belum ada

    # Menyimpan hasil ke file baru di folder filtered
    output_file = os.path.join(output_folder, f'monkeypox_{start_year}_{start_month}_to_{end_year}_{end_month}_filtered.csv')
    filtered_data.to_csv(output_file, index=False)

    print(f"Data berhasil difilter untuk rentang {start_month}/{start_year} hingga {end_month}/{end_year}, dan disimpan di: {output_file}")
