# DonorWise - Sistem Pakar Skrining Medis Donor Darah

**DonorWise** adalah aplikasi web berbasis **Sistem Pakar (Expert System)** yang mengevaluasi kelayakan donor darah awal menggunakan kaidah produksi pasti (Rule-Based) berdasarkan standar **PMI (Palang Merah Indonesia)** dan protokol kesehatan resmi.

## Daftar Isi
- [Fitur Utama](#fitur-utama)
- [Teknologi Stack](#teknologi-stack)
- [Struktur Project](#struktur-project)
- [Cara Instalasi](#cara-instalasi)
- [Cara Menjalankan](#cara-menjalankan)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Kriteria Evaluasi](#kriteria-evaluasi)

---

## Fitur Utama

### 1. **Skrining Medis 3-Tahap**
Aplikasi menjalankan evaluasi bertahap untuk memastikan kelayakan donor:

- **Tahap 1: Kriteria Demografi Fisik**
  - Validasi usia legal pendonor (17-65 tahun)
  - Verifikasi berat badan minimal (45 kg)
  - Pengecekan jeda donor sebelumnya (minimal 56 hari)

- **Tahap 2: Cek Veto Permanen**
  - Penolakan mutlak atas riwayat penyakit infeksi menular
  - Penyakit yang tercakup: HIV, Hepatitis, Sifilis, Penyakit Jantung, Kanker

- **Tahap 3: Cek Veto Sementara**
  - Penundaan donor akibat kondisi medis terkini
  - Kondisi yang diperiksa: Demam, Konsumsi Obat, Haid, Hamil/Menyusui, Vaksinasi, Tato/Tindik

### 2. **Interface Modern & User-Friendly**
- Design responsif dengan Tailwind CSS
- Dark mode dengan tema cyberpunk
- Form multi-step dengan validasi real-time
- Tooltip informatif untuk setiap kriteria
- Status hasil yang jelas dengan kode warna (Hijau/Kuning/Merah)

### 3. **Hasil Diagnosis Instan**
Sistem memberikan hasil dalam kategori:
- ✅ **LAYAK (LOLOS SKRINING)** - Calon donor lolos skrining medis dasar
- ⚠️ **DITOLAK SEMENTARA** - Perlu menunggu periode tertentu
- ❌ **DITOLAK PERMANEN** - Tidak dapat mendonor karena penyakit menular
- ❌ **TIDAK LAYAK** - Tidak memenuhi standar fisik PMI

---

## Teknologi Stack

| Aspek | Teknologi |
|-------|-----------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML5, Tailwind CSS, JavaScript |
| **Logic Pakar** | Rule-Based Engine (Python) |
| **Port Default** | 5051 |
| **Python Version** | 3.8+ |

---

## Struktur Project

```
donorWise/
├── app.py                 # Flask app utama & routing
├── pakarLogic.py          # Engine logika sistem pakar
├── templates/
│   ├── index.html         # Halaman utama/beranda
│   └── pakar.html         # Form skrining & hasil diagnosis
├── __pycache__/           # Cache Python
└── README.md              # Dokumentasi ini
```

### Penjelasan File Utama:

#### **app.py**
```python
- Route '/' → Menampilkan halaman beranda (index.html)
- Route '/pakar' (GET/POST) → Halaman form dan hasil diagnosis
- Mengumpulkan data dari form dan memanggil evaluasi_pakar()
- Port: 5051 (debug mode)
```

#### **pakarLogic.py**
```python
- Fungsi: evaluasi_pakar(usia, bb, jeda, demam, penyakit_berat, obat, hamil, haid, tato_tindik, vaksin)
- Menjalankan 6 rules berbasis urutan prioritas
- Return: Dictionary {status, pesan, warna}
```

#### **templates/index.html**
- Landing page dengan penjelasan sistem
- Tombol "Mulai Tes Pakar" yang mengarah ke `/pakar`
- Menampilkan tahapan evaluasi secara visual

#### **templates/pakar.html**
- Form skrining dengan 2 tahap:
  1. Input data dasar (usia, BB, jeda)
  2. Pengecekan kondisi medis (8 checkbox)
- Validasi client-side untuk usia & BB
- Progress indicator visual
- Sidebar panduan & syarat PMI

---

## Cara Instalasi

### Prerequisites
- Python 3.8 atau lebih baru
- pip (Python package manager)

### Langkah Instalasi

```bash
# 1. Masuk ke direktori project
cd donorWise

# 2. Buat virtual environment (opsional tapi direkomendasikan)
python -m venv venv

# 3. Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install flask

# 5. Verifikasi instalasi
python -c "import flask; print(flask.__version__)"
```

---

## Cara Menjalankan

```bash
# 1. Pastikan Anda di direktori project
cd donorWise

# 2. Aktifkan virtual environment (jika ada)
venv\Scripts\activate

# 3. Jalankan aplikasi
python app.py

# Output:
# * Running on http://127.0.0.1:5051
# * Press CTRL+C to quit
```

### Akses Aplikasi
- **Beranda:** [http://localhost:5051/](http://localhost:5051/)
- **Form Skrining:** [http://localhost:5051/pakar](http://localhost:5051/pakar)

---

## Panduan Penggunaan

### Langkah-Langkah:

1. **Akses Beranda**
   - Buka [http://localhost:5051/](http://localhost:5051/)
   - Baca penjelasan sistem
   - Klik tombol "Mulai Tes Pakar"

2. **Tahap 1: Input Data Dasar**
   - Masukkan **Usia** (tahun)
   - Masukkan **Berat Badan** (kg)
   - Masukkan **Jeda Donor Terakhir** (hari) - kosongkan jika belum pernah
   - Klik "Lanjut ke Riwayat Medis" setelah validasi

3. **Tahap 2: Pengecekan Medis**
   - Centang kondisi yang berlaku:
     - ☐ Sedang Demam / Flu
     - ☐ Riwayat HIV/Hepatitis
     - ☐ Konsumsi Antibiotik/Aspirin
     - ☐ Sedang Hamil / Menyusui
     - ☐ Sedang Haid (< 7 Hari)
     - ☐ Tato/Operasi (< 1 Tahun)
     - ☐ Baru Menerima Vaksinasi
   - Arahkan kursor ke teks untuk melihat detail/tooltip

4. **Lihat Hasil**
   - Klik "Simpan & Diagnosis"
   - Hasil diagnosis akan ditampilkan dengan status dan pesan detail
   - Klik "Ulangi Pengecekan Baru" untuk melakukan skrining lagi

---

## Kriteria Evaluasi

### Rule Priority (Urutan Pengecekan)

| No. | Kriteria | Syarat | Status Output |
|-----|----------|--------|---------------|
| 1 | Usia | < 17 atau > 65 | ❌ TIDAK LAYAK |
| 2 | Berat Badan | < 45 kg | ❌ TIDAK LAYAK |
| 3 | Jeda Donor | < 56 hari (jika ada riwayat) | ❌ TIDAK LAYAK |
| 4 | Penyakit Berat | HIV/Hepatitis/Sifilis/dst | ❌ DITOLAK PERMANEN |
| 5 | Hamil/Menyusui | Ya | ⚠️ DITOLAK SEMENTARA |
| 6 | Haid | Ya | ⚠️ DITOLAK SEMENTARA |
| 7 | Tato/Tindik | < 1 tahun | ⚠️ DITOLAK SEMENTARA |
| 8 | Vaksinasi | < jeda aman | ⚠️ DITOLAK SEMENTARA |
| 9 | Demam/Obat | Ya | ⚠️ DITOLAK SEMENTARA |
| - | Lolos Semua | - | ✅ LAYAK (LOLOS SKRINING) |

### Referensi Jeda Aman:
- **Vaksin COVID-19/Tetanus:** 3-8 minggu
- **Tato/Tindik/Operasi:** 6 bulan - 1 tahun
- **Haid:** 7 hari pasca haid selesai
- **Donor Sebelumnya:** 56 hari

---

## Logika Sistem Pakar

Sistem menggunakan **Rule-Based Engine** dengan evaluasi bertahap:

```python
def evaluasi_pakar(usia, bb, jeda, demam, penyakit_berat, obat, hamil, haid, tato_tindik, vaksin):
    # Rule 1: Cek usia
    if usia < 17 or usia > 65:
        return TIDAK_LAYAK
    
    # Rule 2: Cek BB
    if bb < 45:
        return TIDAK_LAYAK
    
    # Rule 3: Cek jeda donor
    if jeda != "" and int(jeda) < 56:
        return TIDAK_LAYAK
    
    # Rule 4: Cek penyakit berat (veto permanen)
    if penyakit_berat:
        return DITOLAK_PERMANEN
    
    # Rule 5-9: Cek kondisi sementara
    if hamil or haid or tato_tindik or vaksin or demam or obat:
        return DITOLAK_SEMENTARA
    
    # Jika lolos semua rule
    return LAYAK
```

---

## Catatan Penting

⚠️ **DISCLAIMER:**
- Aplikasi ini hanya untuk skrining medis dasar dan bukan pengganti pemeriksaan medis profesional
- Keputusan final tetap bergantung pada pemeriksaan medis langsung oleh petugas PMI
- Menyembunyikan riwayat penyakit menular dapat membahayakan nyawa penerima darah maupun diri sendiri
- Selalu konsultasikan dengan petugas kesehatan profesional sebelum mendonor

---

## Links Berguna

- [Standar PMI](https://www.pmi.or.id/)
- [Panduan Donor Darah](https://www.pmi.or.id/layanan/donor-darah)
- [Protokol Kesehatan Kemenkes](https://www.kemkes.go.id/)

---