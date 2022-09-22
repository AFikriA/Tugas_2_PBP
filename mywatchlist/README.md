# Jelaskan perbedaan antara JSON, XML, dan HTML!
-  JSON hanyalah format data sedangkan XML dan HTML adalah bahasa markup
-  XML dan JSON berfokus pada transfer data sedangkan HTML difokuskan pada penyajian data.
-  JSON mengirimkan data dengan cara menguraikan data terlebih dahulu, kemudian dikirimkan melalui internet. Sedangkan XML memiliki data yang jauh lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.
-  JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.
-   Nama file JSON diakhiri ekstensi .json, file XML dikahir ekstensi .xml, file HTML diakhiri dengan ekstensi .html

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena nantinya dalam proses pengimplementasian sebuah platform, akan butuh mengirimkan data dari satu stack ke stack lainnya. Data tersebut bisa berbentuk macam-macam seperti HTML,XML atau JSON.

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

# Screenshoot dari postman
![Screenshot (407)](https://user-images.githubusercontent.com/112608674/191567896-5bbd2f9c-0855-4b1a-8e5d-37c7f53fd34d.png)
![Screenshot (408)](https://user-images.githubusercontent.com/112608674/191567910-d4760f9b-3f16-42a7-93dc-dac4ffeb736b.png)
![Screenshot (409)](https://user-images.githubusercontent.com/112608674/191567927-7796f22f-b94d-4679-9f50-4a9d475e9e89.png)
