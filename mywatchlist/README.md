# Jelaskan perbedaan antara JSON, XML, dan HTML!
-  JSON hanyalah format data sedangkan XML dan HTML adalah bahasa markup
-  XML dan JSON berfokus pada transfer data sedangkan HTML difokuskan pada penyajian data.
-  JSON mengirimkan data dengan cara menguraikan data terlebih dahulu, kemudian dikirimkan melalui internet. Sedangkan XML memiliki data yang jauh lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.
-  JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.
-  XML itu Case Sensitive sedangkan HTML Case Insensitive
-  Tag XML dapat dikembangkan sedangkan HTML memiliki tag terbatas
# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat aplikasi baru bernama mywatchlist
- Menambahkan mywatchlist ke settings.py
- Menulis kode untuk models.py yang diisi dengan judul dari tabel
- Melakukan migrate
- Membuat berkas initial_mywatchlist_data.json yang diisi dengan data-data yang sesuai dengan model
- Selanjutnya, loaddata initial_mywatchlist_data.json
- Membuat fungsi di views.py
- Menulis kode untuk diimplementasikan di HTML
- Menambahkan path untuk mywatchlist di urls.py
- Melakukan import HttpResponse dan serializers
- Membuat fungsi show_xml dan show_json
- Lalu tambahkan path nya di urls.py
- Push ke git, lalu deploy ke heroku
