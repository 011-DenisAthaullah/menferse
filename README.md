# Menferse 💌🌷
### Platform Menfess dan Pengiriman Bunga Kampus

Menferse adalah aplikasi web berbasis kampus yang memungkinkan mahasiswa menyampaikan pesan, perasaan, dan apresiasi kepada sesama mahasiswa melalui menfess dan pengiriman bunga. Mahasiswa dapat mengirim pesan secara anonim atau menampilkan nama mereka. Setiap pesan akan diperiksa oleh admin sebelum ditampilkan di halaman utama. Menferse juga menyediakan katalog bunga dan fitur pemesanan bunga untuk pengiriman di lingkungan kampus.

## 👥 Anggota Kelompok

| No. | Nama | NIM | Nama Pengguna GitHub |
|---|---|---|---|
| 1 | Denis Athaullah      | 26110300002 | 011-DenisAthaulah |
| 2 | Dude Dzaky Fadilla   | 26110300024 | rausyan27         |
| 3 | Rausyan Fikri Ananda | 26110300023 | dudedzfadilla02   |

## 📌 Latar Belakang Masalah

Mahasiswa terkadang merasa kesulitan atau canggung untuk menyampaikan perasaan, apresiasi, maupun pesan secara langsung kepada mahasiswa lain. Media informal seperti media sosial dan grup percakapan dapat membuat pesan tersebar di berbagai tempat serta memberikan keterbatasan dalam pengaturan identitas pengirim dan pemeriksaan isi pesan.

Selain itu, pengiriman bunga kepada seseorang di lingkungan kampus memerlukan koordinasi antara pengirim, penerima, dan pihak pengantar. Tanpa proses pemesanan yang terstruktur, informasi penerima dan pesanan dapat menjadi sulit dikelola.

Menferse dirancang untuk menyediakan satu platform yang membantu mahasiswa mengirim menfess, mengatur publikasi pesan melalui pemeriksaan admin, serta melakukan pemesanan bunga untuk penerima di lingkungan kampus.

## ✨ Fitur Utama

- **Kirim Menfess:** Mahasiswa dapat mengirim pesan kepada mahasiswa lain.
- **Mode Anonim:** Pengirim dapat memilih untuk menyembunyikan atau menampilkan namanya.
- **Moderasi Pesan:** Admin memeriksa pesan sebelum dipublikasikan.
- **Halaman Utama:** Pengunjung dapat melihat menfess yang telah disetujui.
- **Katalog Bunga:** Mahasiswa dapat melihat bunga yang tersedia.
- **Pemesanan Bunga:** Mahasiswa dapat memesan bunga dengan mengisi informasi penerima.
- **Pengiriman di Kampus:** Pesanan bunga ditujukan untuk pengiriman di lingkungan kampus.
- **Status Pesanan:** Sistem menyediakan pengelolaan informasi dan status pesanan bunga.

## 🎯 Pengguna Sistem

### 1. Mahasiswa

Mahasiswa dapat membuat akun, mengirim menfess, memilih mode anonim, melihat pesan yang telah disetujui, melihat katalog bunga, dan memesan bunga.

### 2. Admin

Admin bertugas memeriksa menfess, menyetujui atau menolak pesan, mengelola konten yang dipublikasikan, serta mengelola informasi pesanan bunga.

## 📦 Ruang Lingkup Proyek

### Termasuk dalam Proyek

- Registrasi dan login mahasiswa.
- Pengiriman menfess dan pengaturan anonimitas.
- Pemeriksaan dan publikasi menfess.
- Halaman utama untuk menampilkan menfess yang disetujui.
- Katalog bunga dan pengajuan pesanan.
- Informasi penerima berupa nama, program studi, angkatan, dan gedung kampus.
- Pengelolaan status pesanan bunga.

### Tidak Termasuk dalam Proyek

- Integrasi login menggunakan akun Google atau sistem akun universitas.
- Integrasi pembayaran digital secara langsung.
- Pelacakan pengiriman menggunakan GPS.
- Fitur percakapan pribadi antarpengguna.
- Moderasi konten otomatis menggunakan AI.
- Pengiriman bunga ke luar lingkungan kampus.

## 🧩 Modul Sistem

| Modul | Tanggung Jawab |
|---|---|
| Autentikasi | Mengelola registrasi, login, dan hak akses pengguna. |
| Pengelolaan Menfess | Mengelola pengiriman pesan dan pengaturan anonimitas. |
| Moderasi | Memungkinkan admin menyetujui atau menolak menfess. |
| Katalog Bunga dan Pesanan | Mengelola katalog bunga dan pengajuan pesanan. |
| Halaman Utama dan Status Pesanan | Menampilkan menfess yang disetujui dan informasi status pesanan. |

## 📚 Dokumen Proyek

Dokumen dan kode sumber proyek akan disimpan dalam struktur berikut.

| Bagian | Lokasi Berkas |
|---|---|
| D1: Topik dan Rumusan Masalah | `docs/D1_PROBLEM_STATEMENT.md` |
| D2: Pembagian Modul | `docs/D2_MODULE_BREAKDOWN.md` |
| D3: Diagram Use Case | `docs/D3_USE_CASE_DIAGRAM.md` |
| D4: Diagram Sequence | `docs/D4_SEQUENCE_DIAGRAMS.md` |
| D5: Catatan Aktivitas Tim | `ACTIVITY_LOG.md` |
| D6: Rancangan Kasus Uji | `docs/D6_TEST_CASES.md` |
| D7: Kode dan Pengujian Unit | `src/validation.py` dan `tests/test_validation.py` |
| Berkas Diagram | `diagrams/` |

*Tautan ke setiap dokumen akan dilengkapi setelah berkas terkait dibuat dan disimpan di GitHub.*

## 🛠️ Teknologi yang Digunakan

- **Bahasa pemrograman:** Python
- **Pengelolaan versi kode:** Git dan GitHub
- **Kerangka pengujian:** pytest
- **Dokumentasi:** Markdown
- **Pembuatan diagram:** Mermaid atau draw.io

## 🧪 Cara Menjalankan Pengujian

Pastikan Python sudah terpasang di komputer.

### 1. Unduh repository

```bash
git clone <URL_REPOSITORY>
cd <NAMA_FOLDER_REPOSITORY>
```

Ganti URL dan nama folder sesuai repository milik kelompokmu.

### 2. Pasang pytest

```bash
python -m pip install pytest
```

### 3. Jalankan pengujian

```bash
python -m pytest -v
```

Pengujian diharapkan berhasil setelah kode sumber dan seluruh kasus uji selesai dibuat.

## 🤖 Penggunaan AI

ChatGPT dapat digunakan untuk membantu menyusun draf dokumentasi, merencanakan modul dan diagram, memberikan ide kasus uji, serta membantu memahami dan meninjau kode program.

Seluruh hasil yang dibantu AI harus diperiksa, dipahami, dan diuji oleh anggota kelompok. Setiap anggota bertanggung jawab untuk memahami bagian yang dikerjakannya dan memastikan bahwa hasil yang dikumpulkan sesuai dengan implementasi sebenarnya.

## 📋 Informasi Proyek

- **Nama proyek:** Menferse
- **Mata kuliah:** Software Development Fundamentals
- **Jenis proyek:** Tugas Ujian Akhir Semester
- **Repository GitHub:** https://github.com/011-DenisAthaullah/menferse

---

*Menferse: Ruang untuk berbagi pesan, perasaan, dan perhatian di lingkungan kampus.*
