# D4 — Sequence Diagrams Menferse

## 1. Tujuan

Sequence Diagram menggambarkan urutan interaksi antara aktor, antarmuka pengguna (*user interface*), dan komponen sistem Menferse. Dokumen ini mencakup tiga skenario utama: pengiriman menfess, moderasi menfess, dan pemesanan bunga.

## 2. Sequence Diagram 1: Mengirim Menfess

### Deskripsi Skenario

Skenario ini menggambarkan proses mahasiswa mengirim menfess melalui Menferse. Skenario ini penting karena pengiriman menfess merupakan fungsi utama aplikasi dan menjadi awal dari proses moderasi konten.

### Alur Proses

1. Mahasiswa membuka halaman pengiriman menfess.
2. Mahasiswa mengisi pesan dan memilih identitas pengirim.
3. UI mengirim data ke modul pengelolaan menfess.
4. Sistem memeriksa autentikasi dan memvalidasi data.
5. Jika data valid, sistem menyimpan menfess dengan status menunggu moderasi.
6. UI menampilkan konfirmasi pengiriman.
7. Jika validasi gagal atau mahasiswa belum login, sistem menampilkan pesan yang sesuai.

### Gambar Sequence Diagram

![Sequence Diagram 1: Mengirim Menfess](img/D4_SEQUENCE_1.png)

**Lokasi file PNG:** `docs/img/D4_SEQUENCE_1.png`

**Lokasi source PlantUML:** `diagrams/D4_SEQUENCE_1.puml`

### Hasil yang Diharapkan

Menfess yang valid tersimpan dengan status menunggu moderasi dan tidak langsung muncul di halaman publik.

---

## 3. Sequence Diagram 2: Moderasi Menfess

### Deskripsi Skenario

Skenario ini menggambarkan proses administrator memeriksa dan menentukan kelayakan menfess sebelum dipublikasikan. Skenario ini penting untuk memastikan konten melewati proses moderasi.

### Alur Proses

1. Administrator membuka halaman moderasi menfess.
2. UI meminta daftar menfess yang menunggu pemeriksaan.
3. Sistem memeriksa hak akses administrator dan mengambil data menfess.
4. Administrator memilih menfess untuk diperiksa.
5. Sistem menampilkan detail menfess.
6. Administrator memilih untuk menyetujui atau menolak menfess.
7. Modul moderasi menyimpan keputusan.
8. Jika disetujui, menfess dapat ditampilkan di halaman publik.
9. Jika ditolak, menfess tidak dipublikasikan.
10. UI menampilkan hasil moderasi kepada administrator.

### Gambar Sequence Diagram

![Sequence Diagram 2: Moderasi Menfess](img/D4_SEQUENCE_2.png)

**Lokasi file PNG:** `docs/img/D4_SEQUENCE_2.png`

**Lokasi source PlantUML:** `diagrams/D4_SEQUENCE_2.puml`

### Hasil yang Diharapkan

Sistem menyimpan keputusan administrator dengan benar. Menfess yang disetujui dapat ditampilkan kepada publik, sedangkan menfess yang ditolak tidak dipublikasikan.

---

## 4. Sequence Diagram 3: Memesan Bunga

### Deskripsi Skenario

Skenario ini menggambarkan proses mahasiswa memilih bunga dan membuat pesanan untuk penerima di lingkungan kampus. Skenario ini penting karena melibatkan validasi informasi penerima dan ketersediaan produk.

### Alur Proses

1. Mahasiswa membuka katalog bunga.
2. UI meminta daftar bunga yang tersedia.
3. Mahasiswa memilih bunga.
4. Sistem memeriksa autentikasi mahasiswa.
5. Mahasiswa mengisi nama penerima, program studi, angkatan, dan gedung kampus.
6. Sistem memvalidasi data penerima dan memeriksa ketersediaan bunga.
7. Jika data valid dan bunga tersedia, sistem menyimpan pesanan.
8. UI menampilkan konfirmasi dan status pesanan.
9. Jika data tidak lengkap atau bunga tidak tersedia, sistem menampilkan pesan kesalahan.

### Gambar Sequence Diagram

![Sequence Diagram 3: Memesan Bunga](img/D4_SEQUENCE_3.png)

**Lokasi file PNG:** `docs/img/D4_SEQUENCE_3.png`

**Lokasi source PlantUML:** `diagrams/D4_SEQUENCE_3.puml`

### Hasil yang Diharapkan

Pesanan berhasil dicatat apabila mahasiswa telah login, data penerima valid, dan bunga tersedia. Jika salah satu persyaratan tidak terpenuhi, sistem menampilkan informasi yang sesuai.

---

## 5. Kesimpulan

Ketiga Sequence Diagram menggambarkan proses utama Menferse, yaitu pengiriman menfess, moderasi menfess, dan pemesanan bunga. Diagram menunjukkan interaksi aktor dengan UI dan komponen sistem, termasuk alur alternatif ketika validasi gagal, akses ditolak, atau bunga tidak tersedia.
