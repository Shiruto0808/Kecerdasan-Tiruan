"""Mencari rute terpendek dari A ke E dengan algoritma Dijkstra.

Graf pada soal (arah panah mengikuti gambar papan tulis):
    A -> B (4), A -> C (6), B -> C (7), B -> D (9),
    B -> F (2), C -> D (8), D -> E (9)

Jalankan: python dijkstra_a_ke_e.py
"""

from __future__ import annotations

import csv
import heapq
from math import inf
from pathlib import Path


# Ubah data ini apabila kelompok mendapat bobot/arah graf yang berbeda.
GRAF = {
    "A": {"B": 4, "C": 6},
    "B": {"C": 7, "D": 9, "F": 2},
    "C": {"D": 8},
    "D": {"E": 9},
    "E": {},
    "F": {},
}
SUMBER = "A"
TUJUAN = "E"


def format_jarak(jarak: float) -> str:
    """Menampilkan jarak tak hingga dengan teks yang aman di terminal Windows."""
    return "INF" if jarak == inf else str(int(jarak))


def dijkstra(graf: dict[str, dict[str, int]], sumber: str):
    """Mengembalikan jarak, pendahulu, dan tabel setiap iterasi Dijkstra."""
    simpul = list(graf)
    jarak = {simpul_: inf for simpul_ in simpul}
    pendahulu = {simpul_: None for simpul_ in simpul}
    jarak[sumber] = 0
    antrean = [(0, sumber)]
    sudah_tetap: set[str] = set()
    tabel = []

    while antrean:
        jarak_saat_ini, u = heapq.heappop(antrean)
        if u in sudah_tetap:
            continue

        sudah_tetap.add(u)
        for v, bobot in graf[u].items():
            kandidat = jarak_saat_ini + bobot
            if kandidat < jarak[v]:
                jarak[v] = kandidat
                pendahulu[v] = u
                heapq.heappush(antrean, (kandidat, v))

        tabel.append(
            {
                "iterasi": len(tabel) + 1,
                "simpul_dipilih": u,
                "simpul_tetap": ", ".join(sorted(sudah_tetap)),
                **{f"jarak_{s}": format_jarak(jarak[s]) for s in simpul},
            }
        )

    return jarak, pendahulu, tabel


def buat_rute(pendahulu: dict[str, str | None], tujuan: str) -> list[str]:
    """Menyusun rute mundur dari tujuan menuju sumber."""
    rute = []
    simpul: str | None = tujuan
    while simpul is not None:
        rute.append(simpul)
        simpul = pendahulu[simpul]
    return list(reversed(rute))


def cetak_tabel(tabel: list[dict[str, str | int]]) -> None:
    kolom = list(tabel[0])
    lebar = {k: max(len(k), *(len(str(baris[k])) for baris in tabel)) for k in kolom}
    print(" | ".join(k.ljust(lebar[k]) for k in kolom))
    print("-+-".join("-" * lebar[k] for k in kolom))
    for baris in tabel:
        print(" | ".join(str(baris[k]).ljust(lebar[k]) for k in kolom))


def simpan_csv(tabel: list[dict[str, str | int]], nama_berkas: Path) -> None:
    with nama_berkas.open("w", newline="", encoding="utf-8-sig") as berkas:
        penulis = csv.DictWriter(berkas, fieldnames=tabel[0].keys())
        penulis.writeheader()
        penulis.writerows(tabel)


if __name__ == "__main__":
    jarak, pendahulu, tabel = dijkstra(GRAF, SUMBER)
    rute = buat_rute(pendahulu, TUJUAN)

    print("=== HASIL DIJKSTRA ===")
    print(f"Rute terpendek : {' -> '.join(rute)}")
    print(f"Total bobot    : {format_jarak(jarak[TUJUAN])}")
    print("\n=== TABEL ITERASI ===")
    cetak_tabel(tabel)

    keluaran = Path(__file__).with_name("tabel_iterasi_dijkstra.csv")
    simpan_csv(tabel, keluaran)
    print(f"\nTabel CSV tersimpan di: {keluaran.name}")
