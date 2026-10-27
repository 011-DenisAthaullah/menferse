# D3 — Use Case Diagram Menferse

## 1. Tujuan

Use Case Diagram Menferse menggambarkan interaksi antara mahasiswa, administrator, dan sistem Menferse. Sistem ini menyediakan fitur untuk melihat menfess publik, mengirim menfess, melakukan moderasi menfess, melihat katalog bunga, memesan bunga, serta memeriksa status pesanan.

## 2. Identifikasi Aktor

| Aktor | Deskripsi |
|---|---|
| Mahasiswa | Pengguna yang dapat melihat menfess publik, masuk ke akun, mengirim menfess, melihat katalog bunga, memesan bunga, dan memeriksa status pesanan. |
| Administrator | Pengelola sistem yang memeriksa menfess serta menyetujui atau menolaknya sebelum dipublikasikan. |

## 3. Daftar Use Case

| ID | Nama Use Case | Aktor | Deskripsi |
|---|---|---|---|
| UC-01 | Melihat Menfess Publik | Mahasiswa | Melihat menfess yang telah disetujui dan dipublikasikan. |
| UC-02 | Masuk ke Akun | Mahasiswa | Melakukan autentikasi untuk mengakses fitur yang memerlukan akun. |
| UC-03 | Mengirim Menfess | Mahasiswa | Mengirim pesan menfess untuk ditinjau administrator. |
| UC-04 | Memilih Identitas Pengirim | Mahasiswa | Memilih apakah nama ditampilkan atau pengiriman dilakukan secara anonim. |
| UC-05 | Memoderasi Menfess | Administrator | Memeriksa menfess yang menunggu peninjauan. |
| UC-06 | Menyetujui Menfess | Administrator | Menyetujui menfess agar dapat ditampilkan secara publik. |
| UC-07 | Menolak Menfess | Administrator | Menolak menfess yang tidak layak dipublikasikan. |
| UC-08 | Melihat Katalog Bunga | Mahasiswa | Melihat pilihan bunga yang tersedia. |
| UC-09 | Memesan Bunga | Mahasiswa | Memilih bunga dan membuat pesanan untuk penerima di lingkungan kampus. |
| UC-10 | Mengisi Data Penerima | Mahasiswa | Mengisi nama penerima, program studi, angkatan, dan gedung kampus untuk keperluan pengantaran. |
| UC-11 | Melihat Status Pesanan | Mahasiswa | Memeriksa perkembangan status pesanan bunga. |

## 4. Relasi Antar-Use Case

- `<<include>>` Mengirim Menfess — Memilih Identitas Pengirim: mahasiswa menentukan apakah identitasnya ditampilkan atau disembunyikan saat mengirim menfess.
- `<<include>>` Memesan Bunga — Mengisi Data Penerima: data penerima diperlukan untuk memproses pengantaran bunga.
- `<<extend>>` Menyetujui Menfess — Memoderasi Menfess: persetujuan merupakan salah satu kemungkinan hasil moderasi.
- `<<extend>>` Menolak Menfess — Memoderasi Menfess: penolakan merupakan kemungkinan hasil lainnya.

Persetujuan dan penolakan merupakan dua kemungkinan hasil yang berbeda, bukan tindakan yang harus dilakukan sekaligus.

## 5. Gambar Use Case Diagram

Diagram Use Case Menferse dapat dilihat pada gambar berikut.

![Use Case Diagram Menferse](img/D3_USE_CASE_DIAGRAM.png)

**Lokasi gambar:** `diagrams/img/D3_USE_CASE_DIAGRAM.png`

**Lokasi source PlantUML:** `diagrams/D3_USE_CASE_DIAGRAM.puml`

## 6. Kesimpulan

Use Case Diagram Menferse memuat dua aktor dan sebelas use case yang menggambarkan fitur utama sistem. Diagram ini menjadi gambaran interaksi pengguna dengan sistem sebelum proses pengembangan dilakukan.
