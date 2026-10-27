# D7: Unit-Tested Code

## 1. Tujuan

Pengujian unit dilakukan untuk memastikan fungsi validasi pesan menfess pada aplikasi Menferse berjalan sesuai dengan aturan yang ditentukan. Pengujian mencakup kondisi input normal dan kondisi khusus.

## 2. Fungsi yang Diuji

Fungsi yang diuji adalah `validate_menfess(message)` yang terdapat pada file `src/menfess_validator.py`.

Fungsi ini memeriksa apakah input berupa string dan apakah pesan memiliki panjang 1 sampai 500 karakter setelah spasi di awal dan akhir diabaikan.

## 3. Tools yang Digunakan

- Bahasa pemrograman: Python
- Framework pengujian: pytest
- Otomatisasi: GitHub Actions

Lokasi file:
- Source code: `src/menfess_validator.py`
- Unit test: `tests/test_menfess_validator.py`
- Workflow: `.github/workflows/python-tests.yml`

## 4. Test Cases

Terdapat 10 test cases untuk menguji fungsi validasi menfess.

| ID | Skenario Pengujian | Hasil yang Diharapkan |
|---|---|---|
| TC-01 | Pesan normal | Valid |
| TC-02 | Pesan anonim | Valid |
| TC-03 | Pesan dengan spasi di awal dan akhir | Valid |
| TC-04 | Pesan sepanjang 200 karakter | Valid |
| TC-05 | Pesan kosong | Tidak valid |
| TC-06 | Pesan hanya berisi spasi | Tidak valid |
| TC-07 | Pesan dengan satu karakter | Valid |
| TC-08 | Pesan sepanjang 500 karakter | Valid |
| TC-09 | Pesan sepanjang 501 karakter | Tidak valid |
| TC-10 | Input berupa angka | Tidak valid |

## 5. Cara Menjalankan Pengujian

Jalankan perintah berikut dari direktori utama repository:

```bash
python -m pip install pytest
python -m pytest -v
```

Pengujian juga dijalankan secara otomatis menggunakan GitHub Actions ketika terdapat push atau pull request.

## 6. Hasil Pengujian

Berdasarkan log GitHub Actions, seluruh 10 test cases berhasil dijalankan.

**Hasil: 10 passed in 0.02s.**

### Bukti Hasil Pengujian

Klik tautan berikut untuk melihat screenshot hasil pengujian:

![Bukti Unit Test Menferse](https://github.com/011-DenisAtaullah/menferse/blob/main/screenshots/D7_UNIT_TESTS.png?raw=true)

## 7. Kesimpulan

Berdasarkan hasil pengujian, fungsi `validate_menfess(message)` berhasil melewati seluruh 10 test cases. Pengujian mencakup input valid, pesan kosong, spasi, batas panjang pesan, dan input dengan tipe data yang tidak sesuai.

GitHub Actions membantu menjalankan pengujian secara otomatis sehingga hasil pengujian dapat diperiksa setiap kali perubahan dikirim ke repository.
