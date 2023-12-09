import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
print(df)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
peningkatan = lambda gaji: gaji * 0.05
gajibaru = lambda gaji: gaji + peningkatan(gaji)
gaji_baru = []
for index, row in df.iterrows():
    gaji_baru.append(gajibaru(row['Gaji']))

df['GajiBaru'] = gaji_baru

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print(df)

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
peningkatan_lansia = lambda GajiBaru: GajiBaru * 0.02
gajibaru_lansia = lambda GajiBaru: GajiBaru + peningkatan_lansia(GajiBaru)
gaji_baru_lansia = []

for index, row in df.iterrows():
    if row['Usia'] > 30:
        gaji_baru_lansia.append(gajibaru_lansia(row['GajiBaru']))
    else:
        gaji_baru_lansia.append(row['GajiBaru'])

df['GajiLansia'] = gaji_baru_lansia


# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print(df)

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.