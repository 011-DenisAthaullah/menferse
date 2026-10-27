# D6: Test Case Design Menferse

## 1. Tujuan Pengujian

Pengujian ini bertujuan memastikan fitur pengiriman menfess pada aplikasi Menferse dapat menerima input yang valid, menolak input yang tidak sesuai, serta menangani kondisi khusus dengan benar.

Skenario yang diuji adalah **Mengirim Menfess**, yaitu proses mahasiswa mengisi pesan, memilih identitas pengirim, dan mengirimkan menfess untuk menunggu moderasi administrator.

## 2. Asumsi dan Aturan Validasi

Test case ini menggunakan aturan pengujian berikut sebagai acuan:

- Mahasiswa harus login untuk mengirim menfess.
- Pesan menfess wajib diisi dan tidak boleh hanya berisi spasi.
- Panjang pesan yang diizinkan adalah 1 sampai 500 karakter setelah spasi di awal dan akhir dihapus.
- Mahasiswa dapat memilih identitas ditampilkan atau anonim.
- Menfess yang berhasil dikirim disimpan dengan status `Pending Moderation`.
- Pengiriman yang sama secara tidak sengaja tidak boleh menghasilkan dua menfess yang identik dalam satu proses pengiriman.

Aturan tersebut merupakan asumsi rancangan untuk pengujian dan harus disesuaikan apabila implementasi final Menferse menetapkan aturan yang berbeda.

## 3. Common Test Cases

| ID | Judul | Tipe | Prasyarat | Input / Langkah Pengujian | Hasil yang Diharapkan |
|---|---|---|---|---|---|
| TC-01 | Mengirim menfess dengan pesan valid | Common | Mahasiswa sudah login. | Isi pesan: `Semangat untuk semua mahasiswa hari ini!`, lalu tekan Kirim. | Menfess tersimpan dengan status `Pending Moderation`. |
| TC-02 | Mengirim menfess secara anonim | Common | Mahasiswa sudah login. | Isi pesan valid, pilih opsi anonim, lalu kirim. | Menfess tersimpan dan identitas pengirim tidak ditampilkan kepada publik. |
| TC-03 | Mengirim menfess dengan identitas ditampilkan | Common | Mahasiswa sudah login. | Isi pesan valid, pilih opsi tampilkan identitas, lalu kirim. | Menfess tersimpan dengan preferensi identitas sesuai pilihan mahasiswa. |
| TC-04 | Mengirim pesan dengan spasi di awal dan akhir | Common | Mahasiswa sudah login. | Isi pesan: `  Semangat kuliah!  `, lalu kirim. | Pesan diterima dan spasi di awal serta akhir dihapus sebelum disimpan. |
| TC-05 | Mengirim menfess dengan pesan normal yang cukup panjang | Common | Mahasiswa sudah login. | Isi pesan yang valid dengan panjang 200 karakter, lalu kirim. | Menfess berhasil disimpan dan masuk ke antrean moderasi. |

## 4. Edge Test Cases

| ID | Judul | Tipe | Prasyarat | Input / Langkah Pengujian | Hasil yang Diharapkan |
|---|---|---|---|---|---|
| TC-06 | Mengirim pesan kosong | Edge | Mahasiswa sudah login. | Kosongkan kolom pesan, lalu tekan Kirim. | Sistem menolak pengiriman dan menampilkan pesan bahwa pesan wajib diisi. |
| TC-07 | Mengirim pesan yang hanya berisi spasi | Edge | Mahasiswa sudah login. | Isi pesan dengan beberapa spasi saja, lalu kirim. | Sistem menolak pengiriman karena pesan tidak memiliki konten yang valid. |
| TC-08 | Mengirim pesan dengan panjang minimum | Edge | Mahasiswa sudah login. | Isi pesan dengan satu karakter, misalnya `A`, lalu kirim. | Sistem menerima pesan karena panjangnya memenuhi batas minimum satu karakter. |
| TC-09 | Mengirim pesan melebihi batas maksimum | Edge | Mahasiswa sudah login. | Isi pesan dengan 501 karakter, lalu kirim. | Sistem menolak pesan atau mencegah input melebihi batas 500 karakter. |
| TC-10 | Mengirim menfess tanpa login | Edge | Mahasiswa belum login. | Buka formulir pengiriman dan coba kirim pesan valid. | Sistem menolak pengiriman dan meminta mahasiswa login. |
| TC-11 | Menekan tombol Kirim berulang kali | Edge | Mahasiswa sudah login dan formulir berisi pesan valid. | Tekan tombol Kirim berulang kali dengan cepat untuk satu pengiriman. | Sistem hanya membuat satu menfess dan tidak menghasilkan duplikasi akibat pengiriman berulang tersebut. |
| TC-12 | Database gagal menyimpan menfess | Edge | Mahasiswa sudah login, tetapi penyimpanan database gagal. | Isi pesan valid, lalu kirim ketika database tidak tersedia. | Sistem menampilkan pesan kegagalan dan tidak memberikan konfirmasi bahwa menfess berhasil disimpan. |

## 5. Alasan Pemilihan Edge Cases

Edge cases dipilih untuk menguji batas validasi dan kondisi yang dapat menyebabkan kegagalan pengiriman menfess. Pesan kosong dan pesan yang hanya berisi spasi digunakan untuk memastikan sistem tidak menerima input tanpa konten, sedangkan pengujian panjang minimum dan maksimum memeriksa batas karakter. Pengujian tanpa login memastikan fitur terlindungi dari akses yang tidak sah, sementara pengiriman berulang digunakan untuk memeriksa kemungkinan duplikasi data. Terakhir, kegagalan database menguji apakah sistem dapat memberikan respons yang tepat ketika proses penyimpanan tidak berhasil.

## 6. Kesimpulan

Sebanyak 12 test case dirancang untuk menguji skenario pengiriman menfess pada Menferse, yang terdiri dari 5 common cases dan 7 edge cases. Pengujian mencakup input valid, validasi pesan, batas karakter, autentikasi, duplikasi pengiriman, dan kegagalan penyimpanan. Hasil pengujian nantinya dapat digunakan untuk mengevaluasi apakah fitur pengiriman menfess telah memenuhi perilaku yang diharapkan.
