def evaluasi_pakar(usia, bb, jeda, demam, penyakit_berat, obat, hamil, haid, tato_tindik, vaksin):
    if usia < 17 or usia > 65:
        return {"status": "TIDAK LAYAK", "pesan": "Usia tidak memenuhi standar PMI (17 - 65 Tahun).", "warna": "text-red-500"}
    if bb < 45:
        return {"status": "TIDAK LAYAK", "pesan": "Berat badan minimal untuk mendonor adalah 45 Kg.", "warna": "text-red-500"}
    if jeda != "" and int(jeda) < 56:
        return {"status": "TIDAK LAYAK", "pesan": f"Jeda dari donor sebelumnya minimal 56 hari. (Baru {jeda} hari).", "warna": "text-red-500"}
    if penyakit_berat:
        return {"status": "DITOLAK PERMANEN", "pesan": "Riwayat HIV, Hepatitis, Sifilis, Penyakit Jantung atau Kanker adalah penolakan permanen.", "warna": "text-red-500"}
    if hamil:
        return {"status": "DITOLAK SEMENTARA", "pesan": "Ibu hamil/menyusui ditunda donorkannya untuk menjaga asupan gizinya.", "warna": "text-yellow-500"}
    if haid:
        return {"status": "DITOLAK SEMENTARA", "pesan": "Wanita sedang haid ditunda hingga minimal 7 hari pasca haid untuk mencegah anemia.", "warna": "text-yellow-500"}
    if tato_tindik:
        return {"status": "DITOLAK SEMENTARA", "pesan": "Anda harus menunggu 1 tahun setelah pembuatan tato/tindik/operasi terakhir.", "warna": "text-yellow-500"}
    if vaksin:
        return {"status": "DITOLAK SEMENTARA", "pesan": "Anda harus menunggu masa jeda aman setelah menerima vaksinasi.", "warna": "text-yellow-500"}
    if demam or obat:
        return {"status": "DITOLAK SEMENTARA", "pesan": "Anda sedang dalam pengaruh obat/sakit. Silakan kembali setelah sembuh total.", "warna": "text-yellow-500"}

    return {"status": "LAYAK (LOLOS SKRINING)", "pesan": "Anda lolos skrining medis dasar Sistem Pakar.", "warna": "text-emerald-500"}