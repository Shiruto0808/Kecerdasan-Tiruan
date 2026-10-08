# Tugas Kelompok: Rute Optimal A ke E

Program `dijkstra_a_ke_e.py` mencari jalur paling optimal dari simpul **A** ke **E** menggunakan algoritma **Dijkstra**. Program juga menampilkan tabel setiap iterasi dan menyimpan tabel tersebut sebagai `tabel_iterasi_dijkstra.csv`, sehingga dapat dibuka di Excel.

## Data graf dari gambar

| Dari | Ke | Bobot |
|---|---|---:|
| A | B | 4 |
| A | C | 6 |
| B | C | 7 |
| B | D | 9 |
| B | F | 2 |
| C | D | 8 |
| D | E | 9 |

Graf dianggap **berarah** mengikuti arah panah pada gambar. Jika dosen menyatakan jalan dua arah, tambahkan arah balik pada bagian `GRAF` dalam program.

## Cara menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Buka terminal pada folder tugas ini.
3. Jalankan:

```powershell
python dijkstra_a_ke_e.py
```

## Hasil

Rute optimal yang diperoleh adalah **A → B → D → E** dengan total bobot **22**.

Kolom `jarak_X` pada tabel adalah jarak sementara dari A ke simpul X setelah simpul pada kolom `simpul_dipilih` diproses. `INF` artinya belum ada rute yang ditemukan.
