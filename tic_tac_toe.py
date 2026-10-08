"""Tic Tac Toe terminal: manusia vs bot minimax yang tidak dapat kalah.

Jalankan di PowerShell:
    python tic_tac_toe.py
"""

from __future__ import annotations

from functools import lru_cache

KOMBINASI_MENANG = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # baris
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # kolom
    (0, 4, 8), (2, 4, 6),             # diagonal
)
URUTAN_LANGKAH = (4, 0, 2, 6, 8, 1, 3, 5, 7)  # tengah, sudut, lalu sisi


def pemenang(papan: tuple[str, ...]) -> str | None:
    """Mengembalikan X/O bila ada pemenang, atau None bila belum ada."""
    for a, b, c in KOMBINASI_MENANG:
        if papan[a] != " " and papan[a] == papan[b] == papan[c]:
            return papan[a]
    return None


def selesai(papan: tuple[str, ...]) -> bool:
    return pemenang(papan) is not None or " " not in papan


@lru_cache(maxsize=None)
def nilai_minimax(papan: tuple[str, ...], giliran: str, bot: str, manusia: str) -> int:
    """Nilai posisi dari sudut pandang bot: menang=1, seri=0, kalah=-1."""
    menang = pemenang(papan)
    if menang == bot:
        return 1
    if menang == manusia:
        return -1
    if " " not in papan:
        return 0

    nilai_anak = []
    giliran_selanjutnya = manusia if giliran == bot else bot
    for posisi in URUTAN_LANGKAH:
        if papan[posisi] == " ":
            papan_baru = list(papan)
            papan_baru[posisi] = giliran
            nilai_anak.append(
                nilai_minimax(tuple(papan_baru), giliran_selanjutnya, bot, manusia)
            )
    return max(nilai_anak) if giliran == bot else min(nilai_anak)


def langkah_bot(papan: tuple[str, ...], bot: str, manusia: str) -> int:
    """Memilih langkah bernilai terbaik. Karena minimax, bot tidak mungkin kalah."""
    terbaik = -2
    posisi_terbaik = -1
    for posisi in URUTAN_LANGKAH:
        if papan[posisi] != " ":
            continue
        papan_baru = list(papan)
        papan_baru[posisi] = bot
        nilai = nilai_minimax(tuple(papan_baru), manusia, bot, manusia)
        if nilai > terbaik:
            terbaik = nilai
            posisi_terbaik = posisi
    return posisi_terbaik


def tampilkan_papan(papan: tuple[str, ...]) -> None:
    """Mencetak papan beserta nomor posisi yang dipakai saat memasukkan langkah."""
    print()
    for baris in range(0, 9, 3):
        isi = [papan[i] if papan[i] != " " else str(i + 1) for i in range(baris, baris + 3)]
        print(f" {isi[0]} | {isi[1]} | {isi[2]} ")
        if baris < 6:
            print("---+---+---")
    print()


def pilih_pemain_pertama() -> bool:
    while True:
        pilihan = input("Siapa jalan duluan? [1] Manusia  [2] Bot: ").strip()
        if pilihan == "1":
            return True
        if pilihan == "2":
            return False
        print("Masukkan 1 atau 2.")


def langkah_manusia(papan: tuple[str, ...]) -> int:
    while True:
        masukan = input("Pilih kotak (1-9): ").strip()
        if not masukan.isdigit() or not 1 <= int(masukan) <= 9:
            print("Masukkan angka 1 sampai 9.")
            continue
        posisi = int(masukan) - 1
        if papan[posisi] != " ":
            print("Kotak itu sudah terisi. Pilih kotak lain.")
            continue
        return posisi


def main() -> None:
    print("=" * 39)
    print("       TIC TAC TOE: MANUSIA VS BOT")
    print("=" * 39)
    print("Bot memakai algoritma Minimax, jadi bot tidak dapat kalah.\n")

    while True:
        manusia_duluan = pilih_pemain_pertama()
        manusia, bot = ("X", "O") if manusia_duluan else ("O", "X")
        giliran = manusia if manusia_duluan else bot
        papan: tuple[str, ...] = (" ",) * 9

        while not selesai(papan):
            tampilkan_papan(papan)
            if giliran == manusia:
                posisi = langkah_manusia(papan)
            else:
                posisi = langkah_bot(papan, bot, manusia)
                print(f"Bot memilih kotak {posisi + 1}.")

            papan_baru = list(papan)
            papan_baru[posisi] = giliran
            papan = tuple(papan_baru)
            giliran = bot if giliran == manusia else manusia

        tampilkan_papan(papan)
        menang = pemenang(papan)
        if menang == bot:
            print("Bot menang. Coba lagi!")
        elif menang == manusia:
            # Kondisi ini tidak akan tercapai bila bot menggunakan langkah_bot.
            print("Manusia menang.")
        else:
            print("Permainan seri.")

        lagi = input("Main lagi? [y/n]: ").strip().lower()
        if lagi not in {"y", "ya"}:
            print("Terima kasih sudah bermain.")
            break


if __name__ == "__main__":
    main()
