def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM secara aman"""
    return data.get(nim, "Data tidak ditemukan")

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

print("Cari A002:", cari_mahasiswa(mahasiswa, "A002"))
print("Cari A003:", cari_mahasiswa(mahasiswa, "A003"))
