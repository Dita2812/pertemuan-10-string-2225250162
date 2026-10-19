# Pertemuan 10 - String dan Pengolahan Teks

Nama: Dita Amalia Veronica
NIM: 2225250162
Kelas: 3F

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python. Program pada Tugas 4 membersihkan data nama mahasiswa dan kode kelas yang formatnya tidak konsisten (spasi berlebih, huruf besar/kecil campur), lalu menampilkan nama bersih, kode kelas yang seragam, jumlah kata pada nama, dan inisial.

## Struktur Folder

```
pertemuan-10-string-NIM/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_dasar_string.py
|   |-- 02_indeks_slicing.py
|   |-- 03_method_string.py
|   |-- 04_bersihkan_teks.py
|   |-- 05_split_join.py
|   `-- 06_pencarian_kata.py
`-- tugas/
    `-- normalisasi_data_mahasiswa.py
```

## Cara Menjalankan

```
python3 tugas/normalisasi_data_mahasiswa.py
```

Program meminta dua input: `Nama` dan `Kode kelas`. Contoh:

```
Nama: aan hendrayana
Kode kelas: pmat a 2026
Nama bersih : Aan Hendrayana
Kode kelas : PMAT-A-2026
Jumlah kata : 2
Inisial : AH
```

## Algoritma

1. Baca nama dan kode kelas sebagai string dengan `input()`.
2. Normalisasi nama: `split()` memecah nama menjadi kata dan otomatis membuang spasi berlebih di awal, akhir, maupun tengah. Kata-kata disambung lagi dengan `" ".join(...)`, lalu diubah ke format huruf kapital di awal tiap kata dengan `title()`.
3. Pecah nama bersih menjadi list kata dengan `split()`. Panjang list (`len`) menjadi jumlah kata.
4. Bangun inisial dengan mengambil karakter pertama (`k[0]`) dari setiap kata, lalu digabung dengan `"".join(...)`.
5. Normalisasi kode kelas: `strip()` menghapus spasi di pinggir, `upper()` mengubah menjadi huruf besar, `split()` memecah per kata, lalu `"-".join(...)` menyambungnya dengan tanda hubung.
6. Tampilkan keempat hasil dengan f-string.

Program dibagi menjadi tiga fungsi dengan tanggung jawab masing-masing: `normalisasi_nama`, `buat_inisial`, dan `normalisasi_kode`.

## Test Case

| No | Input Nama | Input Kode | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|------------|------------|-----------------------|--------------|--------|
| 1 | ` aan hendrayana` | `pmat a 2026` | Aan Hendrayana, PMAT-A-2026, 2 kata, AH | Aan Hendrayana, PMAT-A-2026, 2 kata, AH | Berhasil |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah, KELAS-B, 2 kata, FM | Fathiyyah Muthmainnah, KELAS-B, 2 kata, FM | Berhasil |
| 3 | `BUDI` | `pmtk 01` | Budi, PMTK-01, 1 kata, B | Budi, PMTK-01, 1 kata, B | Berhasil |
| 4 | ` siti nur aisyah` | `kelas c` | Siti Nur Aisyah, KELAS-C, 3 kata, SNA | Siti Nur Aisyah, KELAS-C, 3 kata, SNA | Berhasil |
| 5 | `Dita Amalia Veronica` | `PMAT A 2026` | Dita Amalia Veronica, PMAT-A-2026, 3 kata, DAV | Dita Amalia Veronica, PMAT-A-2026, 3 kata, DAV | Berhasil |

Test case nomor 5 adalah tambahan dengan data nama saya sendiri. Seluruh test case (4 wajib dan 1 tambahan) menghasilkan output yang sesuai, tanpa SyntaxError maupun IndexError.

## Refleksi

Masalah teks yang saya temukan adalah data nama yang formatnya tidak seragam: ada spasi berlebih di awal, huruf besar semua (`BUDI`), dan huruf campur (`fATHIYYAH mUTHMAINNAH`). Jika dibandingkan langsung, data seperti ini dianggap berbeda walaupun maknanya sama. Saya memperbaikinya dengan menormalisasi dulu memakai `strip`, `split`, `join`, dan `title`/`upper`. Saya juga belajar bahwa `strip()` hanya menghapus spasi di pinggir, sedangkan spasi berlebih di tengah dirapikan dengan kombinasi `split()` dan `join()`. Konsep ini akan membantu Pertemuan 11, karena teks yang sudah bersih dan dipecah menjadi kata bisa dihitung frekuensinya memakai dictionary.

## Sumber dan Bantuan

- Bahan Ajar Pertemuan 10 (Algoritma dan Pemrograman, Untirta, 2026/2027 Ganjil).
- Python 3 Documentation: Text Sequence Type (str).
- Bantuan AI (Claude) digunakan untuk membantu menyusun README dan memeriksa hasil test case. Kode dan alasan pemilihan operasi string dapat saya jelaskan.