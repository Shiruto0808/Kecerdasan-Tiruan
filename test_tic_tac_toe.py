"""Pengujian: dari setiap langkah manusia, bot minimax tidak pernah kalah.

Jalankan: python test_tic_tac_toe.py
"""

from tic_tac_toe import langkah_bot, pemenang


def jelajah(papan, giliran, bot, manusia):
    menang = pemenang(papan)
    if menang is not None:
        return {menang}
    if " " not in papan:
        return {"seri"}

    hasil = set()
    if giliran == bot:
        posisi = langkah_bot(papan, bot, manusia)
        papan_baru = list(papan)
        papan_baru[posisi] = bot
        return jelajah(tuple(papan_baru), manusia, bot, manusia)

    for posisi, isi in enumerate(papan):
        if isi == " ":
            papan_baru = list(papan)
            papan_baru[posisi] = manusia
            hasil |= jelajah(tuple(papan_baru), bot, bot, manusia)
    return hasil


for bot_duluan in (True, False):
    bot, manusia = ("X", "O") if bot_duluan else ("O", "X")
    giliran = bot if bot_duluan else manusia
    hasil = jelajah((" ",) * 9, giliran, bot, manusia)
    assert manusia not in hasil, f"Bot kalah saat bot_duluan={bot_duluan}"
    print(f"Bot {'jalan duluan' if bot_duluan else 'jalan kedua'}: {sorted(hasil)}")

print("LULUS: Tidak ada kemungkinan manusia mengalahkan bot.")
