import os
import pandas as pd

# Membaca dataset
file_path = 'data/raw_data/original/monkeypox.csv'  # Ganti dengan nama file Anda
data = pd.read_csv(file_path)

# Pastikan kolom 'date' dalam format datetime
data['date'] = pd.to_datetime(data['date'])

# Meminta input rentang tahun dari pengguna
while True:
    try:
        start_year = int(input("Masukkan tahun awal (contoh: 2023): "))
        end_year = int(input("Masukkan tahun akhir (contoh: 2024): "))
        if start_year > end_year:
            print("Tahun awal tidak boleh lebih besar dari tahun akhir. Silakan coba lagi.")
        else:
            break
    except ValueError:
        print("Input tidak valid. Masukkan angka tahun (contoh: 2023).")

# Filter data untuk rentang tahun yang dipilih
filtered_data = data[(data['date'].dt.year >= start_year) & (data['date'].dt.year <= end_year)]

# Periksa apakah ada data untuk rentang tahun tersebut
if filtered_data.empty:
    print(f"Tidak ada data untuk rentang tahun {start_year} hingga {end_year}.")
else:
    # Path folder untuk menyimpan hasil
    output_folder = 'data/raw_data/filtered'
    os.makedirs(output_folder, exist_ok=True)  # Buat folder jika belum ada

    # Menyimpan hasil ke file baru di folder filtered
    output_file = os.path.join(output_folder, f'monkeypox_{start_year}_to_{end_year}.csv')
    filtered_data.to_csv(output_file, index=False)

    print(f"Data berhasil difilter untuk rentang tahun {start_year} hingga {end_year} dan disimpan di: {output_file}")
