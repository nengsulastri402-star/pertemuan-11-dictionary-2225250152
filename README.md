# Pertemuan 11: Dictionary/Map dan Pasangan Key-Value

**Nama:** SULASTRI
**NIM:** 2225250152
**Kelas:** B
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** Pendidikan Matematika

---

## 1. Tujuan Praktikum
* Memodelkan data pendidikan menggunakan struktur data `dictionary` (pasangan *key-value*) di Python.
* Mengakses dan memodifikasi data berbasis *key* unik (seperti NIM) secara aman tanpa menyebabkan error.
* Mengintegrasikan *dictionary* dengan *list*, *string*, perulangan, dan fungsi modular.
* Menguji program menggunakan Visual Studio Code dan mendokumentasikan hasil pengujian ke repositori GitHub.

---

## 2. Struktur Data
Struktur data yang digunakan pada sistem ini adalah **Nested Dictionary** (Dictionary Bersarang):
* **Key Utama:** NIM (`string`, contoh: `"A001"`), berfungsi sebagai pengenal unik (*unique identifier*).
* **Value Utama:** `dict` (dictionary bersarang) yang menyimpan atribut mahasiswa:
  * `nama` (`string`)
  * `kelas` (`string`)
  * `nilai` (`int`)

**Contoh Struktur:**
```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 82}
}
```

---

## 3. Cara Menjalankan Program
Pastikan Anda telah berada di direktori utama proyek (`pertemuan-11-dictionary-NIM`). Jalankan perintah berikut di Terminal VS Code:

```bash
python3 praktik/data_mahasiswa.py
```

---

## 4. Tabel Test Case Wajib

| No | Kasus Uji | Input / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|:--:|---|---|---|---|:--:|
| 1 | Pencarian NIM tersedia | `A003` | Menampilkan data mahasiswa a.n. Citra (`nama: Citra, kelas: B, nilai: 92`) | `Pencarian A003: Ditemukan -> {'nama': 'Citra', 'kelas': 'B', 'nilai': 92}` | **PASS** |
| 2 | Pencarian NIM tidak tersedia | `A999` | Menampilkan pesan `'Data tidak ditemukan'` tanpa memicu `KeyError` | `Pencarian A999: Pesan 'Data tidak ditemukan'` | **PASS** |
| 3 | Pembaruan Nilai | Ubah nilai `A002` menjadi `82` | Nilai `A002` berhasil diperbarui dari `78` menjadi `82` | `Nilai A002 diperbarui -> {'nama': 'Budi', 'kelas': 'A', 'nilai': 82}` | **PASS** |
| 4 | Penambahan Data Baru | Tambah `A006` (`Fajar`, `B`, `80`) | Key `A006` terdaftar di dictionary utama | `Status: Berhasil ditambahkan.` | **PASS** |
| 5 | Rekap Seluruh Data | Iterasi `items()` | Menampilkan seluruh 6 data mahasiswa beserta detailnya | Seluruh 6 data ditampilkan secara terstruktur | **PASS** |
| 6 | Perhitungan Rata-rata | Fungsi `rata_rata_nilai()` | Menghitung rata-rata nilai ($85+82+92+74+88+80)/6 = 83.17$ | `Rata-rata Nilai Seluruh Mahasiswa: 83.17` | **PASS** |

---

## 5. Refleksi Pembelajaran

### Kesalahan Akses Key yang Ditemukan
Saat awal mencoba mengakses key yang tidak terdaftar (misalnya `data_mahasiswa["A999"]`), Python menghentikan eksekusi program dan melempar error `KeyError: 'A999'`. Hal ini terjadi karena sintaks kurung siku (`[]`) mengasumsikan key pasti ada dalam dictionary.

### Solusi dan Penanganan Error
1. **Penggunaan Method `.get()`:** Mengganti sintaks akses langsung dengan `data.get("A999")`. Method ini mengembalikan nilai `None` atau pesan fallback kustom secara aman tanpa menghentikan program.
2. **Pengecekan Keberadaan Key:** Menggunakan operator `in` (seperti `if "A002" in data:`) sebelum melakukan update nilai agar tidak membuat key yang salah secara tidak sengaja.