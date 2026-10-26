data = {"nama": "Ayu", "nilai": 85}

# 1. Menambah pasangan key-value baru
data["kelas"] = "A"

# 2. Mengubah value dari key yang sudah ada
data["nilai"] = 90
print("Setelah ditambah & diubah:", data)

# 3. Menghapus key menggunakan pop()
kelas_dihapus = data.pop("kelas")
print("Kelas yang dihapus:", kelas_dihapus)
print("Dictionary akhir:", data)