# Tugas 4 PBP
Link Heroku : http://webtugaspbp.herokuapp.com/todolist
# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF Token dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna. Tujuan utamanya adalah agar data yang dikirim ke server berasal dari website milik kita. Mencegah orang lain mengirim data ke server tanpa melewati aplikasi.
Jika tidak ada {% csrf_token %}, maka browser akan mereject request / error karena browser tidak bisa memastikan asal data yang dikirim ke server. Error : CSRF token missing
# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
kita dapat membuat elemen <form> secara manual dengan menggunakan tag yang disediakan HTML. Contoh tag pada login.html yang dimana data yang diterima form disimpan dan dapat diakses dalam views.py dengan method get()
# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Browser akan meresponse dengan mengirm POST ke server saat user membuat request dengan cara menekan button login, register, tambah task, dll. Kemudian akan terdapat perubahan pada server dengan adanya event POST. Setelah itu views.py akan merespon dengan mereturn atau mengupdate data dengan melakukan user redirect ke views sebelumnya sehingga tampilan akan mengupdate data baru.
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat aplikasi baru bernama todolist dengan perintah python manage.py startapp todolist
- Mendaftarkan aplikasi ke dalam INSTALLED_APPS di settings.py
- Buat model dalam file models.py pada folder todolist dengan variabel: user, date, title, dan description
- Menjalankan perintah makemigrations dan migrate
- Membuat fungsi-fungsi yang dibutuhkan pada views.py
- Membuat folder template di dalam folder todolist berisi file-file html yang dibutuhkan menampilkan data
- Tambahkan path url dengan membuat file urls.py di dalam folder todolist dan isi dengan path untuk melakukan routing ke fungsi-fungsi yang ada fi views.py
- Daftarkan app todolist ke dalam url pattern pada file urls.py di folder project_django
