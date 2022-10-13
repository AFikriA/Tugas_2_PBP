# PBP TUGAS 6
Nama  : Aulia Fikri Al Khawariz
NPM   : 2106701160
Kelas : PBP-C
## Link
https://webtugaspbp.herokuapp.com/todolist/ajax/
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. memungkinkan untuk menjalankan banyak proses secara bersamaan tanpa harus menunggu proses lain selesai.
Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous
### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event Driven Programming merupakan paradigma pemrograman di mana objek dapat berkomunikasi secara tidak langsung dengan mengirimkan pesan satu sama lain melalui perantara. Pengiriman pesan tersebut dilakukan melalui event stream. Paradigma ini bergantung pada event dengan memperhatikan operasi apa yang akan diimplementasikan dari adanya event. Penerapan paradigma dalam tugas ini terdapat pada implementasi tombol submit form penambahan task. Apabila tombol ditekan, maka akan terdapat event yang di trigger dan ditangani oleh AJAX sebagai perantara untuk mengirim data yang diisi dari form ke server, Selain itu, AJAX akan memperbarui data pada section Todo list secara asynchronous.
### Jelaskan penerapan asynchronous programming pada AJAX.
Membuat view serta url path baru yang mereturn sebuah response JSON. Implementasi asynchronous programming AJAX dalam tugas ini terdapat pada function get serta post untuk mengambil serta mengirim data JSON ke server, serta mengatur tampilan pada Todo list secara asynchronous sesuai data yang ada pada database.
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat tambahan fungsi untuk yang versi ajax-nya, termasuk tombol change dan delete nya
2. Membuat function baru yang mereturn response berupa JSON
3. Menambahkan attribute onClick pada button create task yang diintegrasikan dengan AJAX serta modals pop up
4. Menambahkan beberapa function javascript untuk melakukan get dan post request ke server
