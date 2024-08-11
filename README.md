## E-Library with Django and TailwindCSS
Sebuah aplikasi E-Library dengan fitur-fitur sebagai berikut:
- Login, Registrasi, Logout
- Katalog Buku
- Pencarian Buku (berdasarkan judul)
- Detail Buku
- Menambah/Menghapus Buku

### Cara Menjalankan Program
1. Buat virtual environment. Jika menggunakan pipenv, gunakan command berikut:
    ```python
    pip install pipenv
    pip shell
    ```

2. Masuk ke direktori `./project`
    ```python
    cd ./project
    ```

3. Install requirement yang dibutuhkan sesuai daftar pada file `requirements.txt`
    ```python
    pip install -r requirements.txt
    ```

4. Load data dump dan data user (opsional) dengan command berikut:
    ```python
    python manage.py loaddata data_dump.json
    python manage.py loaddata user.json
    ```
    Catatan:
    Jika menggunakan command di atas, username dan password dari superuser adalah `admin`

5. Unduh file tailwindcss.exe dan simpan pada direktori `./project`
    Unduh melalui link berikut (pilih sesuai sistem operasi yang digunakan):
    [Tailwind CSS Github Releases](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.1) > 'Assets'

    Atau menggunakan CURL dengan command berikut (jalankan pada direktori `./project`):
    ```python
    curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/<the_file_name_for_your_os>

    ```

6. Lakukan migrasi database SQLite
    ```python
    python manage.py migrate
    ```

7. Jalankan aplikasi dengan command berikut:
    ```python
    python manage.py runserver
    ```

8. Aplikasi akan berjalan pada localhost port 8000

### Dokumentasi Gambar
1. Halaman Bookshelf (Katalog)
![1_Bookshelf](https://github.com/user-attachments/assets/e99ece5a-b428-48be-a939-be7edd37c256)

2. Halaman Detail Buku
![2_Book Detail](https://github.com/user-attachments/assets/aee98535-3782-4d72-b749-e64afeb306bd)

3. Halaman Login
![3_Login (small screen)](https://github.com/user-attachments/assets/a251f4d6-b023-4643-8887-88abfdb8f69e)

4. Halaman Registrasi
![4_Registrasi (small screen)](https://github.com/user-attachments/assets/e0fe3cd6-7b19-450c-99ac-84904792ab77)

5. Halaman Tambah Buku
![5_Add Book](https://github.com/user-attachments/assets/7d1057f8-458a-4c63-b655-3cd8ee2b8a25)
