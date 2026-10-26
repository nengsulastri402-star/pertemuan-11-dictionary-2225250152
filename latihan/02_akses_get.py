data = {"nama": "Ayu", "nilai": 85}

# Akses key yang ada
print("Nama:", data.get("nama"))

# Akses key yang TIDAK ada menggunakan get() -> mengembalikan None atau nilai default
print("Kelas (default None):", data.get("kelas"))
print("Kelas (dengan fallback):", data.get("kelas", "Belum ada"))

# Catatan: Jika menggunakan data["kelas"], program akan mengalami KeyError!