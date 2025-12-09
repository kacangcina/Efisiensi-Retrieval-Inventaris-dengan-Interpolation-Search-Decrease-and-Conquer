# Analisis Efisiensi Algoritma Interpolation Search (Decrease and Conquer)

![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-orange?style=for-the-badge)

Repositori ini berisi kode sumber eksperimental (*source code*) untuk penelitian artikel ilmiah berjudul:

> **"Analisis Efisiensi Algoritma Interpolation Search Berbasis Pendekatan Decrease and Conquer untuk Optimasi Retrieval Data Inventaris E-Commerce Berskala Besar"**

## 📋 Tentang Penelitian
Penelitian ini membandingkan kinerja tiga algoritma pencarian dalam konteks manajemen inventaris gudang (*Warehouse Management System*):
1.  **Linear Search** (Brute force)
2.  **Binary Search** (Decrease-by-half)
3.  **Interpolation Search** (Variable-size-decrease)

Tujuan utama dari kode ini adalah untuk mengukur waktu eksekusi (*execution time*) dan jumlah iterasi pada dua jenis distribusi data SKU:
* **Uniform Distribution:** Data SKU yang urut dan rapi.
* **Skewed/Exponential Distribution:** Data dengan jarak antar elemen yang timpang (untuk menguji *worst-case*).

## 🚀 Fitur & Implementasi
Kode ditulis menggunakan **Python 3.9+** dengan pendekatan *Object Oriented Programming* (OOP) sederhana untuk mensimulasikan entitas barang (`InventoryItem`).

Modul utama mencakup:
* Generasi dataset sintetis (10.000 s.d. 1.000.000 entitas).
* Implementasi algoritma Interpolation Search dengan penanganan *edge cases* (pembagian nol).
* Pencatatan waktu presisi nanodetik (`time.time_ns`).

## 🛠️ Prasyarat (Requirements)
Tidak ada dependensi eksternal yang berat. Anda hanya membutuhkan:
* Python 3.x (Disarankan versi 3.8 ke atas)

## 💻 Cara Menjalankan (Usage)

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/username-kamu/judul-repo-kamu.git](https://github.com/username-kamu/judul-repo-kamu.git)
    cd judul-repo-kamu
    ```

2.  **Jalankan skrip eksperimen:**
    ```bash
    python main.py
    ```
    *(Catatan: Sesuaikan `main.py` dengan nama file python kamu)*

## 📊 Contoh Output Eksperimen
Berikut adalah cuplikan hasil simulasi yang akan muncul di terminal:

```text
=== MULAI EKSPERIMEN PENCARIAN INVENTARIS ===

--- Ukuran Dataset: 10000 Items ---
Linear Search        | Waktu:     152300 ns | Iterasi: 4950
Binary Search        | Waktu:       3200 ns | Iterasi: 13
Interpolation Search | Waktu:        800 ns | Iterasi: 1

...

--- Ukuran Dataset: 1000000 Items ---
Linear Search        | Waktu:   15400200 ns | Iterasi: 499900
Binary Search        | Waktu:       4500 ns | Iterasi: 19
Interpolation Search | Waktu:       1200 ns | Iterasi: 2
