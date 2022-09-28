# Link Heroku Tugas 2
https://webtugaspbp.herokuapp.com/katalog

# Bagan _request client_ ke _web_

![Bagan VMT](https://user-images.githubusercontent.com/112608674/190245314-0d41aa65-a33c-49e5-b707-84d7bc96e984.png)

Setiap _request_ dari _client_ akan diproses pertama kali oleh 'urls.py', karena di sini berisi definisi alamat URL (_route_) dan fungsi yang dieksekusi di setiap rute.

Berikutnya, fungsi yang ada di 'views.py' akan melakukan pemrosesan seperti:
- Tulis data atau ambil data dari model
- Mengatur tampilan data dengan HTML
- Kirim _HTTP_ Response ke _Client_

# _Virtual Environment_
Saat menginstal modul/library menggunakan pip, modulnya akan terinstal secara global di /usr/lib/python2.7/site-packages. Dimana, semua aplikasi bisa mengakses dan menggunakannya.

Pembuatan aplikasi berbasis django bisa saja dilakukan tanpa _virtual environment_. Namun, hal ini memiliki masalah dimana, jika kita membuat proyek dengan menggunakan django 1.1. Pada awalnya, aplikasi dapat berjalan sempurna. Namun, dikemudian hari ketika django merilis versi terbaru seperti versi 4.0. Kita akan melakukan _upgrade_ modul. Maka, aplikasi kita tadi sudah tidak relevan lagi karena ada perubahan fungsi dan lain-lain. Oleh karena itu, penggunaan _virtual environment_ dibutuhkan agar masing-masing aplikasi memiliki modulnya sendiri

# Pengimplementasian Tugas 2
1. Buka views.py yang ada pada folder katalog dan buatlah sebuah fungsi yang menerima _parameter request_ dan mengembalikan render(request, "katalog.html")
2. Berkas di dalam folder aplikasi katalog yang bernama urls.py berfungsi untuk melakukan _routing_ terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat _browser_. Daftarkan juga aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode path pada variabel urlpatterns.
3. Pada fungsi views yang telah dibuat, import models yang sudah dibuat sebelumnya ke dalam file views.py. Tambahkan Potongan kode yang berfungsi untuk memanggil fungsi _query_ ke _model database_ dan menyimpan hasil _query_ tersebut ke dalam sebuah variabel. Langkah terakhir, tambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat sebelumnya. Data yang ada pada variabel context tersebut akan ikut di-render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
4. Untuk _deployment_, buat aplikasi baru di Heroku, salin API Key dari akun Heroku. Lalu, simpanlah API Key beserta informasi tentang aplikasi Heroku di repository secret dalam variabel HEROKU_API_KEY dan HEROKU_APP_NAME. Terakhir, jalankan kembali workflow yang gagal sebelumnya.
