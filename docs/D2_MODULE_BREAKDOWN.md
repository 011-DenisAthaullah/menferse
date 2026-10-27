# D2: Perincian Modul

## 1. Pendahuluan

Menferse adalah situs web kampus yang menyediakan fitur penyampaian pesan menfess dan pemesanan bunga bagi mahasiswa. Untuk mempermudah proses pengembangan, sistem dibagi menjadi lima modul utama. Setiap modul memiliki tanggung jawab dan fitur masing-masing serta saling berhubungan untuk mendukung fungsi aplikasi secara keseluruhan.

## 2. Daftar Modul

### 2.1 Modul Autentikasi

**Tanggung Jawab**

Mengelola proses masuk dan keluar akun serta membatasi akses pengguna ke fitur tertentu berdasarkan peran.

**Fitur**
- Registrasi akun mahasiswa.
- Masuk dan keluar dari akun.
- Memeriksa status login pengguna.
- Mengidentifikasi peran pengguna sebagai mahasiswa atau administrator.

**Ketergantungan**
- Menyediakan informasi identitas dan peran pengguna bagi modul lain.

### 2.2 Modul Pengelolaan Menfess

**Tanggung Jawab**

Mengelola proses pengiriman pesan menfess oleh mahasiswa sebelum pesan diperiksa oleh administrator.

**Fitur**
- Mengisi dan mengirim pesan menfess.
- Memasukkan nama penerima.
- Memilih opsi anonim atau menampilkan nama pengirim.
- Memeriksa kelengkapan pesan.
- Menyimpan pesan dengan status menunggu pemeriksaan.

**Ketergantungan**
- Modul Autentikasi untuk memastikan mahasiswa telah masuk ke akun.
- Modul Moderasi Menfess untuk proses pemeriksaan pesan.

### 2.3 Modul Moderasi Menfess

**Tanggung Jawab**

Mengelola proses pemeriksaan pesan menfess oleh administrator sebelum pesan ditampilkan kepada pengguna.

**Fitur**
- Menampilkan daftar pesan yang menunggu pemeriksaan.
- Menyetujui pesan menfess.
- Menolak pesan menfess.
- Memperbarui status pesan berdasarkan keputusan administrator.

**Ketergantungan**
- Modul Autentikasi untuk memeriksa hak akses administrator.
- Modul Pengelolaan Menfess untuk memperoleh pesan yang perlu diperiksa.
- Modul Halaman Utama dan Status Pesanan untuk memastikan hanya pesan yang disetujui ditampilkan.

### 2.4 Modul Katalog dan Pemesanan Bunga

**Tanggung Jawab**

Mengelola katalog bunga dan proses pemesanan bunga oleh mahasiswa untuk penerima di lingkungan kampus.

**Fitur**
- Menampilkan katalog bunga.
- Menampilkan informasi dan harga bunga.
- Memilih bunga yang ingin dipesan.
- Mengisi nama penerima, program studi, angkatan, dan gedung kampus.
- Memeriksa kelengkapan informasi pesanan.
- Menyimpan pesanan dan status awalnya.

**Ketergantungan**
- Modul Autentikasi untuk memastikan mahasiswa telah masuk ke akun.
- Modul Halaman Utama dan Status Pesanan untuk menampilkan informasi pesanan.

### 2.5 Modul Halaman Utama dan Status Pesanan

**Tanggung Jawab**

Menyediakan halaman utama yang menampilkan pesan menfess yang telah disetujui serta informasi status pesanan bunga.

**Fitur**
- Menampilkan pesan menfess yang telah disetujui administrator.
- Menampilkan nama pengirim jika pengirim memilih untuk menampilkan namanya.
- Menyembunyikan identitas pengirim jika memilih opsi anonim.
- Menampilkan status pesanan bunga kepada mahasiswa yang melakukan pemesanan.
- Memperbarui informasi berdasarkan status terbaru.

**Ketergantungan**
- Modul Moderasi Menfess untuk memperoleh pesan yang telah disetujui.
- Modul Katalog dan Pemesanan Bunga untuk memperoleh informasi pesanan.

## 3. Ringkasan Ketergantungan Antar-Modul

| Modul | Modul yang Berkaitan | Tujuan Ketergantungan |
|---|---|---|
| Autentikasi | Tidak ada modul utama lain | Menyediakan identitas dan peran pengguna |
| Pengelolaan Menfess | Autentikasi, Moderasi Menfess | Memastikan pengirim terautentikasi dan pesan dapat diperiksa |
| Moderasi Menfess | Autentikasi, Pengelolaan Menfess, Halaman Utama dan Status Pesanan | Memastikan pesan diperiksa oleh administrator dan hasil persetujuan diteruskan |
| Katalog dan Pemesanan Bunga | Autentikasi, Halaman Utama dan Status Pesanan | Memastikan pengguna terautentikasi dan informasi pesanan dapat ditampilkan |
| Halaman Utama dan Status Pesanan | Moderasi Menfess, Katalog dan Pemesanan Bunga | Menampilkan pesan yang disetujui dan status pesanan |

## 4. Kesimpulan

Menferse dibagi menjadi lima modul utama, yaitu Modul Autentikasi, Modul Pengelolaan Menfess, Modul Moderasi Menfess, Modul Katalog dan Pemesanan Bunga, serta Modul Halaman Utama dan Status Pesanan. Pembagian ini membantu pengembangan sistem menjadi lebih terstruktur, memperjelas tanggung jawab setiap modul, dan memudahkan pembagian pekerjaan antaranggota kelompok.
