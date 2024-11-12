# Meminta input jumlah siswa
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# Inisialisasi variabel untuk menyimpan total nilai
total_nilai = 0

# Loop untuk meminta nilai setiap siswa
for i in range(jumlah_siswa):
    nilai = float(input(f"Masukkan nilai ujian siswa ke-{i+1}: "))
    total_nilai += nilai

# Menghitung rata-rata nilai
rata_rata = total_nilai / jumlah_siswa

# Menampilkan hasil rata-rata
print(f"Rata-rata nilai dari seluruh siswa adalah: {rata_rata:.2f}")
