# Tugas Kecerdasan Tiruan: Tic Tac Toe vs Bot

Game ini dimainkan melalui terminal (tanpa GUI), untuk satu pemain melawan bot. Saat permainan dimulai, pemain dapat memilih apakah manusia atau bot yang berjalan terlebih dahulu.

## Algoritma AI

Bot menggunakan **Minimax**. Algoritma ini mencoba semua kemungkinan langkah hingga permainan berakhir, lalu selalu memilih langkah dengan hasil terbaik:

| Nilai | Arti bagi bot |
|---:|---|
| 1 | Bot menang |
| 0 | Seri |
| -1 | Bot kalah |

Karena mengevaluasi seluruh kemungkinan permainan, bot akan menang jika manusia membuat kesalahan dan minimal seri bila manusia bermain optimal. Oleh karena itu, bot tidak mungkin kalah.

## Menjalankan program

1. Pastikan Python 3 terinstal.
2. Buka PowerShell pada folder ini.
3. Jalankan perintah berikut:

```powershell
python tic_tac_toe.py
```

Masukkan nomor kotak 1 sampai 9 sesuai nomor yang tampil pada papan.

## Pengujian bot

Pengujian mengeksplorasi semua kemungkinan langkah manusia dalam dua kondisi: bot jalan duluan dan bot jalan kedua.

```powershell
python test_tic_tac_toe.py
```

Hasil yang diharapkan: tidak ada hasil `O`/manusia menang. Bot hanya menang atau seri.

## Pembagian peran kelompok (contoh)

| Anggota | Tanggung jawab |
|---|---|
| 1 | Membuat papan dan alur permainan |
| 2 | Membuat input serta validasi langkah manusia |
| 3 | Menerapkan algoritma Minimax untuk bot |
| 4 | Pengujian, dokumentasi, dan presentasi |
