import os
import shutil                                                          
import time
from pathlib import Path
import subprocess


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    teks = """
  ________  ___________   _____    __  _____   _____
 /_  __/ / / / ____/   | / ___/   / / / /   | / ___/
  / / / / / / / _/ /| | \_ \   / / / / /| | \__ \
 / / / // / // / ___ |/ /  / // / ___ |_/ /
//  \/\//  |//   \//  |/_/
    """.strip("\n").split("\n")

    terminal_width = os.get_terminal_size().columns
    for line in teks:
        print(line.center(terminal_width))

    # Tabel nama kelompok
    table = [
        "|                   KELOMPOK                  |",
        "+=============================================+",                 
        "+=======================+=====================+",
        "| Nama                  | NIM                 |",
        "+-----------------------+---------------------+",
        "| Lalu Bagus A.K. Wijaya| 24241138            |",
        "| Hasan Wirayuda        | 24241133            |",
        "+=======================+=====================+"
    ]

    for row in table:
        print(row.center(terminal_width))

    print("=" * terminal_width)

def tugas1():
    clear()
    print("\n===== TUGAS 1: Logika Boolean =====\n")
    print("==========NOT==========")
    x = False
    z = not x
    print("nilai z =", z)

    # AND
    print("==========AND==========")
    x = False
    y = False
    nilai = x and y
    print(x, "and", y, "=", nilai)

    x = False
    y = True
    nilai = x and y
    print(x, "and", y, "=", nilai)

    x = True
    y = False
    nilai = x and y
    print(x, "and", y, "=", nilai)

    x = True
    y = True
    nilai = x and y
    print(x, "and", y, "=", nilai)

    # OR
    print("==========OR==========")
    x = False
    y = False
    nilai = x or y
    print(x, "or", y, "=", nilai)

    x = False
    y = True
    nilai = x or y
    print(x, "or", y, "=", nilai)

    x = True
    y = False
    nilai = x or y
    print(x, "or", y, "=", nilai)

    x = True
    y = True
    nilai = x or y
    print(x, "or", y, "=", nilai)

    # XOR
    print("==========XOR==========")
    x = False
    y = False
    nilai = x ^ y
    print(x, "xor", y, "=", nilai)

    x = False
    y = True
    nilai = x ^ y
    print(x, "xor", y, "=", nilai)

    x = True
    y = False
    nilai = x ^ y
    print(x, "xor", y, "=", nilai)

    x = True
    y = True
    nilai = x ^ y
    print(x, "xor", y, "=", nilai)

def tugas2():
    clear()
    print("\n===== TUGAS 2: Logika Input Angka =====\n")
    print("Nama: Hasan Wirayuda Nim: 24241133")
    while True:
        try:
            inputUser = int(input("Masukkan angka yang bernilai kurang dari 24 atau lebih dari 38: "))
            break
        except ValueError:
            print("Harap masukkan angka yang valid!")

    iskurangdari = (inputUser < 24)
    islebihdari = (inputUser > 33)
    final = iskurangdari or islebihdari
    print("\n┌──────────────────────┬───────────┐")
    print(  "│     Kondisi          │   Hasil   │")
    print(  "├──────────────────────┼───────────┤")
    print( f"│ Angka < 24           │{str(iskurangdari):<5}    │")
    print( f"│ Angka > 38           │{str(islebihdari):<5}    │")
    print( f"│ Valid (OR kondisi)   │{str(final):<5}    │")
    print(  "└──────────────────────┴───────────┘")

def tugas3():
    clear()
    print("\n===== TUGAS 3: Nilai Kuliah =====\n")
    while True:
        try:
            nilai = float(input("Masukkan nilai Anda (0–100): "))
            if 0 <= nilai <= 100:
                break
            print("Nilai harus antara 0-100!")
        except ValueError:
            print("Harap masukkan angka yang valid!")

    print(  "\n┌──────────────────────┬───────────┐")
    print(    "│     Rentang Nilai    │   Grade   │")
    print(    "├──────────────────────┼───────────┤")

    if nilai > 100 or nilai < 0:
        print("│ Nilai tidak valid    │           │")
    elif nilai >= 85:
        print("│ >= 85                │     A     │")
    elif nilai >= 80:
        print("│ 80 - 84              │     A-    │")
    elif nilai >= 75:
        print("│ 75 - 79              │     B+    │")
    elif nilai >= 70:
        print("│ 70 - 74              │     B     │")
    elif nilai >= 65:
        print("│ 65 - 69              │     B-    │")
    elif nilai >= 60:
        print("│ 60 - 64              │     C+    │")
    elif nilai >= 55:
        print("│ 55 - 59              │     C     │")
    elif nilai >= 50:
        print("│ 50 - 54              │     C-    │")
    elif nilai >= 40:
        print("│ 40 - 49              │     D     │")
    else:
        print("│ < 40                 │     E     │")

    print(    "└────────────────────  ┴───────────┘")

def tugas4():
    clear()
    print("\n===== TUGAS 4: Cek Umur =====\n")
    while True:
        try:
            umur = int(input("Masukkan umur: "))
            break
        except ValueError:
            print("Harap masukkan angka yang valid!")

    print("\n┌──────────────────────┬───────────────┐")
    print("│     Umur            │   Kategori   │")
    print("├──────────────────────┼───────────────┤")
    if umur < 18:
        print(f"│ {umur:<20} │ Anak-anak     │")
    else:
        print(f"│ {umur:<20} │ Dewasa        │")
    print("└──────────────────────┴───────────────┘")

def tugas5():
    clear()
    print("\n===== TUGAS 5: Cek Password =====\n")
    password = input("Masukkan password: ")
    panjang = len(password)

    print("\n┌──────────────────────┬───────────────────┐")
    print("│     Kriteria        │     Hasil        │")
    print("├──────────────────────┼───────────────────┤")
    print(f"│ Panjang Password    │ {panjang:<17} │")
    print("├──────────────────────┼───────────────────┤")
    if panjang < 8:
        print("│ Validasi            │ Tidak Lolos      │")
    else:
        print("│ Validasi            │ Lolos            │")
    print("└──────────────────────┴───────────────────┘")

def tugas6():
    clear()
    print("\n===== TUGAS 6: String Angka =====\n")
    number = "1234567890"

    print("\n┌──────────────────────┬───────────────────┐")
    print("│     Operasi         │     Hasil        │")
    print("├──────────────────────┼───────────────────┤")
    print(f"│ Data terakhir       │ {number[-1]:<17} │")
    print(f"│ Data pertama        │ {number[0]:<17} │")
    print(f"│ Data ke-3 sampai 6  │ {number[2:6]:<17} │")
    print("└──────────────────────┴───────────────────┘")

def tugas7():
    clear()
    print("\n===== TUGAS 7: Pemisah Domain =====\n")
    domain = input("Masukkan domain (contoh: bagus.com): ")
    bagian = domain.partition(".")

    print("\n┌──────────────────────┬───────────────────┐")
    print("│     Komponen        │     Nilai        │")
    print("├──────────────────────┼───────────────────┤")
    print(f"│ Domain lengkap      │ {domain:<17} │")
    print(f"│ Nama domain         │ {bagian[0]:<17} │")
    print(f"│ Ekstensi domain     │ {bagian[2]:<17} │")
    print("└──────────────────────┴───────────────────┘")

def tugas8():
    clear()
    print("\n===== TUGAS 8: Pembulatan Harga =====\n")
    harga_normal = 15.5935
    harga_diskon = 16.45987
    harga_retail = 14.96884

    print("┌──────────────────────┬───────────────┬───────────────┐")
    print("│     Jenis Harga      │ 1 Desimal     │ 2 Desimal     │")
    print("├──────────────────────┼───────────────┼───────────────┤")
    print(f"│ Harga Normal        │ {round(harga_normal, 1):<13}  {round(harga_normal, 2):<13} │")
    print(f"│ Harga Diskon        │ {round(harga_diskon, 1):<13}  {round(harga_diskon, 2):<13} │")
    print(f"│ Harga Retail        │ {round(harga_retail, 1):<13}  {round(harga_retail, 2):<13} │")
    print("└──────────────────────┴───────────────┴───────────────┘")

def main():
    banner()
    while True:
        print("\n📌 Pilih Program yang Ingin Dijalankan:")
        print("+--------------------------------------------+")
        print("| [1] Logika Matematika (TUGAS 1)            |")
        print("| [2] Logika Angka (TUGAS 2)                 |")
        print("| [3] Nilai Kuliah (TUGAS 3)                 |")
        print("| [4] Cek Umur (TUGAS 4)                     |")
        print("| [5] Validasi Password (TUGAS 5)            |")
        print("| [6] Manipulasi String Angka (TUGAS 6)      |")
        print("| [7] Pemisah Domain (TUGAS 7)               |")
        print("| [8] Pembulatan Harga (TUGAS 8)             |")
        print("| [0] Keluar                                 |")
        print("+--------------------------------------------+")

        pilihan = input(">> Pilih nomor tugas (0-8): ")
        if pilihan == '1':
            tugas1()
        elif pilihan == '2':
            tugas2()
        elif pilihan == '3':
            tugas3()
        elif pilihan == '4':
            tugas4()
        elif pilihan == '5':
            tugas5()
        elif pilihan == '6':
            tugas6()
        elif pilihan == '7':
            tugas7()
        elif pilihan == '8':
            tugas8()
        elif pilihan == '0':
            print("\nTerima kasih! Karena telah menggunakan program kelompok kami.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
        input("\nTekan Enter untuk kembali ke menu utama...")
        banner()
if __name__ == "__main__":
    main()



