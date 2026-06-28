import os
import pandas as pd
import matplotlib.pyplot as plt
import csv

if __name__ == "__main__":
    class main:
        def __init__(self):
            pass

        def BARCHART(self,option_file):
            os.system("cls" if os.name == "nt" else "clear")
            print("="*100)
            print(f"{"========================= VISUALISASI DENGAN BARCHART =========================":^100}")
            print("="*100)
            try:
                if option_file == 1:
                    namafile = input("Masukkan Nama File (e.g nilaisiswa.xlsx) : ")
                    df = pd.read_excel(namafile)
                    comparisonoptions = input("APAKAH KAMU INGIN MEMBUAT PERBANDINGAN DATA (YES/NO) : ").lower()
                    if comparisonoptions == "yes" or comparisonoptions == "y":
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ykolom2 = input("Masukkan kolom variabel y 2 bawah (e.g namakolom)            : ")
                        Ykolom2 = df[Ykolom2]
                        Ycolor  = input("Masukkan warna kolom variabel y bawah (e.g green)            : ")
                        Ycolor2 = input("Masukkan warna kolom variabel y 2 bawah (e.g orange)         : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.bar(Xkolom,Ykolom, 
                                    color=Ycolor)
                        plt.bar(Xkolom,Ykolom2,
                                    color=Ycolor2)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()
                    
                    else:
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ycolor  = input("Masukkan warna kolom variabel y bawah (e.g green)            : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.bar(Xkolom,Ykolom, 
                                    color=Ycolor)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()

                elif option_file == 2:
                    namafile = input("Masukkan Nama File (e.g nilaisiswa.xlsx) : ")
                    df = pd.read_csv(namafile)
                    comparisonoptions = input("APAKAH KAMU INGIN MEMBUAT PERBANDINGAN DATA (YES/NO) : ").lower()
                    if comparisonoptions == "yes" or comparisonoptions == "y":
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ykolom2 = input("Masukkan kolom variabel y 2 bawah (e.g namakolom)            : ")
                        Ykolom2 = df[Ykolom2]
                        Ycolor  = input("Masukkan warna untuk barchart (e.g green)                    : ")
                        Ycolor2 = input("Masukkan warna untuk barchart 2 (e.g green)                  : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.bar(Xkolom,Ykolom, 
                                    color=Ycolor)
                        plt.bar(Xkolom,Ykolom2,
                                    color=Ycolor2)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()
                    
                    else:
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ycolor  = input("Masukkan warna untuk barchart (e.g green)                    : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.bar(Xkolom,Ykolom, 
                                    color=Ycolor)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()

                else:
                    print("PILIHAN HANYA 1-2 ...")

            except ValueError:
                print("PILIHAN HANYA BERUPA ANGKA ...")

            except FileNotFoundError:
                print(f"FILE BERNAMA {namafile} TIDAK DITEMUKAN")
                    
            except Exception as e:
                print(e)

        def PLOTCHART(self,option_file):
            os.system("cls" if os.name == "nt" else "clear")
            print("="*100)
            print(f"{"========================= VISUALISASI DENGAN PLOTCHART =========================":^100}")
            print("="*100)
            try:
                if option_file == 1:
                    namafile = input("Masukkan Nama File (e.g nilaisiswa.xlsx) : ")
                    df = pd.read_excel(namafile)
                    comparisonoptions = input("APAKAH KAMU INGIN MEMBUAT PERBANDINGAN DATA (YES/NO) : ").lower()
                    if comparisonoptions == "yes" or comparisonoptions == "y":
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ykolom2 = input("Masukkan kolom variabel y 2 bawah (e.g namakolom)            : ")
                        Ykolom2 = df[Ykolom2]
                        Ycolor  = input("Masukkan warna untuk plotchart (e.g green)                   : ")
                        Ycolor2  = input("Masukkan warna untuk plotchart 2 (e.g green)                : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.plot(Xkolom,Ykolom,
                                marker=".",
                                markersize=20,
                                linestyle="solid",
                                color=Ycolor,
                                linewidth=3)
                        plt.plot(Xkolom,Ykolom2,
                                marker=".",
                                markersize=20,
                                linestyle="solid",
                                color=Ycolor2,
                                linewidth=3)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()
                    
                    else:
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ycolor  = input("Masukkan warna untuk plotchart (e.g green)                   : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.plot(Xkolom,Ykolom,
                                marker=".",
                                markersize=20,
                                linestyle="solid",
                                color=Ycolor,
                                linewidth=3)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()

                elif option_file == 2:
                    namafile = input("Masukkan Nama File (e.g nilaisiswa.xlsx) : ")
                    df = pd.read_csv(namafile)
                    comparisonoptions = input("APAKAH KAMU INGIN MEMBUAT PERBANDINGAN DATA (YES/NO) : ").lower()
                    if comparisonoptions == "yes" or comparisonoptions == "y":
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ykolom2 = input("Masukkan kolom variabel y 2 bawah (e.g namakolom)            : ")
                        Ykolom2 = df[Ykolom2]
                        Ycolor  = input("Masukkan warna untuk plotchart (e.g green)                   : ")
                        Ycolor2  = input("Masukkan warna untuk plotchart 2 (e.g green)                : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.plot(Xkolom,Ykolom,
                                marker=".",
                                markersize=20,
                                linestyle="solid",
                                color=Ycolor,
                                linewidth=3)
                        plt.plot(Xkolom,Ykolom2,
                                marker=".",
                                markersize=20,
                                linestyle="solid",
                                color=Ycolor2,
                                linewidth=3)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()
                    
                    else:
                        Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                        Xname   = input("Masukkan nama variabel x bawah (e.g namakolom)               : ")
                        Yname   = input("Masukkan nama variabel y samping (e.g namakolom)             : ")
                        Xkolom  = input("Masukkan kolom variabel x bawah (e.g namakolom)              : ")
                        Xkolom  = df[Xkolom]
                        Ykolom  = input("Masukkan kolom variabel y bawah (e.g namakolom)              : ")
                        Ykolom  = df[Ykolom]
                        Ycolor  = input("Masukkan warna untuk plotchart (e.g green)                   : ")

                        plt.grid(linestyle="dashed")
                        plt.title(Title, fontsize=20)
                        plt.plot(Xkolom,Ykolom,
                                marker=".",
                                markersize=20,
                                linestyle="solid",
                                color=Ycolor,
                                linewidth=3)
                        plt.xlabel(Xname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.ylabel(Yname, fontsize=15,
                                    family="Arial",
                                    fontweight="bold",
                                    color="Gray")
                        plt.show()

                else:
                    print("PILIHAN HANYA 1-2 ...")

            except ValueError:
                print("PILIHAN HANYA BERUPA ANGKA ...")

            except FileNotFoundError:
                print(f"FILE BERNAMA {namafile} TIDAK DITEMUKAN")
                    
            except Exception as e:
                print(e)

        def PIECHART(self):
            os.system("cls" if os.name == "nt" else "clear")
            print("="*100)
            print(f"{"========================= VISUALISASI DENGAN PIECHART =========================":^100}")
            print("="*100)
            try:
                if option_file == 1:
                    namafile = input("Masukkan Nama File (e.g nilaisiswa.xslx) : ")
                    df = pd.read_excel(namafile)
                    Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                    Xkolom = input("Kolom label : ")
                    Ykolom = input("Kolom nilai : ")
                    Xkolom = df[Xkolom]
                    Ykolom = df[Ykolom]
                    Ycolor = []
                    for nama in Xkolom:
                        color = input(f"Masukkan warna untuk {nama} : ")
                        Ycolor.append(color)

                    plt.title(Title, fontsize=20)
                    plt.pie(Ykolom,labels=Xkolom,
                        autopct="%1.1f%%",
                        colors=Ycolor,
                        explode = [0.1] * len(Ykolom),
                        shadow=True)
                    plt.show()

                elif option_file == 2:
                    namafile = input("Masukkan Nama File (e.g nilaisiswa.csv) : ")
                    df = pd.read_csv(namafile)
                    Title   = input("Masukkan nama title barchart bawah (e.g pendapatan mingguan) : ")
                    Xkolom = input("Kolom label : ")
                    Ykolom = input("Kolom nilai : ")
                    Xkolom = df[Xkolom]
                    Ykolom = df[Ykolom]
                    Ycolor = []
                    for nama in Xkolom:
                        color = input(f"Masukkan warna untuk {nama} : ")
                        Ycolor.append(color)

                    plt.title(Title, fontsize=20)
                    plt.pie(Ykolom,labels=Xkolom,
                        autopct="%1.1f%%",
                        colors=Ycolor,
                        explode = [0.1] * len(Ykolom),
                        shadow=True)
                    plt.show()

                else:
                    print("PILIHAN HANYA 1-2 ...")

            except ValueError:
                print("PILIHAN HANYA BERUPA ANGKA ...")

            except FileNotFoundError:
                print(f"FILE BERNAMA {namafile} TIDAK DITEMUKAN")
                    
            except Exception as e:
                print(e)

        def TUTORIAL(self):
            os.system("cls" if os.name == "nt" else "clear")
            print("="*100)
            print(f"{"========================= TUTORIAL PENGGUNAAN =========================":^100}")
            print(f"{"="*100}\n")
            print(f"{'''PASTIKAN KAMU MEMAHAMI BENTUK DARI SELURUH DIAGRAM DARI KETIGA INI
    1. BARCHART : 
                  
    Fungsi Utama: Membandingkan nilai atau jumlah dari beberapa kategori atau kelompok yang berbeda.
    Kapan Digunakan: Mengetahui produk terlaris, membandingkan penjualan antar cabang, 
    atau melihat tren perubahan satu variabel dalam kurun waktu tertentu.
    
    2. PLOTCHART : 
    
    Fungsi Utama: Menampilkan komposisi atau persentase dari suatu total data keseluruhan (proporsi part-to-whole).
    Kapan Digunakan: Menunjukkan persentase pangsa pasar (market share) perusahaan, 
    alokasi anggaran, atau komposisi demografi.
                  
    3. PIECHART
    
    Fungsi Utama: Menemukan pola, tren, korelasi (hubungan), atau distribusi antara dua variabel.
    Kapan Digunakan: Menganalisis data statistik, 
    misalnya melihat hubungan antara biaya promosi dengan jumlah penjualan, 
    atau mengidentifikasi apakah ada data yang menyimpang (outlier).
                  
    4. FORMAT PROGRAM
    |- MAIN FOLDER (FOLDER UTAMA)
    |___ MAIN PROGRAM (RUNNING DISINI)
    |___ FILE TIPE CSV/EXCEL (RUNNING DISINI)
                  
    5. CONTOH FORMAT UNTUK PIE CHART
    FORMAT HANYA DUA KOLOM YAITU SEBAGAI LABEL DAN NILAI, CARA KERJANYA UNTUK KOLOM NILAI MIRIP DENGAN PERSENTASE
    Hari  | Minggu1
    Hari1 | 10
    Hari2 | 15
    Hari3 | 15
    Hari4 | 20
    Hari5 | 40
                  
    6. CONTOH FORMAT UNTUK BARCHART DAN PLOTCHART
    FORMAT NORMAL SATU KOLOM SEBAGAI X LABEL DAN SATU LAGI SEBAGAI Y LABEL, Y LABEL BISA 2
    Hari   | minggu1 | minggu2
    Senin  | 10      | 20
    Selasa | 13      | 13
    rabu   | 11      | 10
    Kamis  | 13      | 12
    Jumat  | 40      | 30
    Sabtu  | 50      | 55
    Minggu | 100     | 86''':^100}")
    

    mainclass = main()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("="*100)
        print(f"{"========================= COBA VISUALISASI DATA KAMU DISINI =========================":^100}")
        print("="*100)

        try:

            option1 = int(input('''PILIH AKSI DIBAWAH
    1. TUTORIAL PROGRAM (WAJIB UNTUK PERTAMA KALI)
    2. VISUALISASI DATA DENGAN BARCHART
    3. VISUALISASI DATA DENGAN PLOTCHART
    4. VISUALISASI DATA DENGAN PIECHART
PILIH NOMOR AKSI : '''))
            
            
            if option1 == 1:
                mainclass.TUTORIAL()

            elif option1 == 2:
                option_file = int(input('''PILIH JENIS FILE
    1. TIPE EXCEL
    2. TIPE CSV
PILIH 1-2 : '''))
                mainclass.BARCHART(option_file)

            elif option1 == 3:
                option_file = int(input('''PILIH JENIS FILE
    1. TIPE EXCEL
    2. TIPE CSV
PILIH 1-2 : '''))
                mainclass.PLOTCHART(option_file)

            elif option1 == 4:
                option_file = int(input('''PILIH JENIS FILE
    1. TIPE EXCEL
    2. TIPE CSV
PILIH 1-2 : '''))
                mainclass.PIECHART()

            else:
                print("PILIHAN HANYA 1-4 ...")
        
        except ValueError:
            print("PILIHAN HANYA BERUPA ANGKA ...")

        option2 = input("APAKAH KAMU INGIN MELANJUTKAN (YES/NO) : ").lower()
        if option2 != "yes" and option2 != "y":
            print(f"\n{"========================= GOOD BYE =========================":^100}")
            break