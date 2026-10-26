"""
Program: Sistem Data Mahasiswa (Praktik Pertemuan 11)
File: praktik/data_mahasiswa.py
 Deskripsi: Mengelola data mahasiswa menggunakan Dictionary bersarang dan Fungsi.
"""

def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM."""
    return data.get(nim)

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai dari seluruh mahasiswa."""
    if not data:
        return 0.0
    total = sum(mhs["nilai"] for mhs in data.values())
    return total / len(data)

# 1. Inisialisasi Data Mahasiswa (Minimal 5 Data)
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

if __name__ == "__main__":
    print("=== SISTEM PENGELOLAAN DATA MAHASISWA ===")
    
    # 2. Pengujian Pencarian Data (Key Ada & Tidak Ada)
    print("\n[1] Uji Pencarian Data:")
    target_nim = "A003"
    hasil = cari_mahasiswa(data_mahasiswa, target_nim)
    if hasil:
        print(f"  Pencarian {target_nim}: Ditemukan -> {hasil}")
    else:
        print(f"  Pencarian {target_nim}: Data tidak ditemukan")

    target_nim = "A999"
    hasil = cari_mahasiswa(data_mahasiswa, target_nim)
    if hasil:
        print(f"  Pencarian {target_nim}: Ditemukan -> {hasil}")
    else:
        print(f"  Pencarian {target_nim}: Pesan 'Data tidak ditemukan'")

    # 3. Penambahan Mahasiswa Baru
    print("\n[2] Menambahkan Data Mahasiswa Baru (A006):")
    data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "B", "nilai": 80}
    print("  Status: Berhasil ditambahkan.")

    # 4. Pembaruan Nilai Mahasiswa
    print("\n[3] Memperbarui Nilai Mahasiswa (A002 menjadi 82):")
    if "A002" in data_mahasiswa:
        data_mahasiswa["A002"]["nilai"] = 82
        print(f"  Status: Nilai A002 diperbarui -> {data_mahasiswa['A002']}")

    # 5. Rekap Data Menggunakan items()
    print("\n[4] Rekap Seluruh Data Mahasiswa (items()):")
    for nim, info in data_mahasiswa.items():
        print(f"  NIM: {nim} | Nama: {info['nama']:<8} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

    # 6. Menghitung Rata-rata Nilai
    rata_rata = rata_rata_nilai(data_mahasiswa)
    print(f"\n[5] Rata-rata Nilai Seluruh Mahasiswa: {rata_rata:.2f}")
