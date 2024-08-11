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

![1_Bookshelf(1)](https://github.com/user-attachments/assets/4852c521-9c2e-49a7-b52b-0a30344c0f86)


2. Halaman Detail Buku

![2_Book Detail(1)](https://github.com/user-attachments/assets/05fe3084-77ad-446f-9f04-474b77d388cc)


3. Halaman Login

![3_Login (small screen)(1)](https://github.com/user-attachments/assets/6fc28478-047d-4e96-80f9-0a804710007e)


4. Halaman Registrasi

![4_Registrasi (small screen)(1)](https://github.com/user-attachments/assets/075c092d-9f40-41df-9eb3-aa8ca34f7f4f)


5. Halaman Tambah Buku

![5_Add Book(1)](https://github.com/user-attachments/assets/ecd8890f-4ddf-4a3a-9e10-3440f57fb8af)
