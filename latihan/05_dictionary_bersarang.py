# Dictionary yang berisi dictionary lain (Nested Dictionary)
mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

# Akses data dua tingkat
print("Nama A001 :", mahasiswa["A001"]["nama"])
print("Nilai A002:", mahasiswa["A002"]["nilai"])