# Tugas PBP 5

Link Heroku : http://webtugaspbp.herokuapp.com/todolist

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Inline CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. 
Kelebihan dan kekurangan:
- Berguna untuk memperbaiki kode dengan cepat.
- Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
- Sangat membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen. Kekurangan:
- Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.
- 
### Internal CSS
Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. 
Kelebihan dan kekurangan:
- Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
- Class dan ID bisa digunakan oleh internal stylesheet. Kekurangan:
- Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
- Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website.
  
### Eksternal CSS
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. 
Kelebihan dan kekurangan:
- Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
- Loading website menjadi lebih cepat
- File CSS dapat digunakan di beberapa halaman website sekaligus.
- Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML.
  
##  Jelaskan tag HTML5 yang kamu ketahui.
  
1. `<button>`  : Creates a clickable button.
2. `<div>`     : Specifies a division or a section in a document.
3. `<form>`    : Defines an HTML form for user input.
4. `<span>`    : Defines an inline styleless section in a document.
5. `<nav>`     : Defines a section of navigation links.
6. `<header>`  : Represents the header of a document or a section.
7. `<footer>`  : Represents the footer of a document or a section.
8. `<title>`   : Defines a title for the document.
9. `<tr>`      : Defines a row of cells in a table.
10. `<td>`     : Defines a cell in a table.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. Type Selector, memilih semua elemen yang memiliki nama simpul yang diberikan.
2. ID Selector, memilih elemen berdasarkan nilai atribut id-nya. Seharusnya hanya ada satu elemen dengan ID yang diberikan dalam dokumen. Diimplementasikan dengan tanda pagar(#)
3. Class Selector, memilih semua elemen yang memiliki atribut kelas tertentu. Diimplementasikan dengan tanda titik (.)
4. Universal Selector, universal selector hanya ada 1 di dalam CSS, yaitu tanda bintang “*”. Selector ini bertujuan untuk ‘mencari’ semua tag yang ada.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  
1. Mendefinisikan link src bootstrap ke dalam tag `<head>`
2. Membuat struktur HTML dengan menggunakan class dan menyesuaikan bootstrap sesuai kebutuhan
3. Mengubah style dari tampilan bootstrap dengan menambahkan Internal CSS ke dalam tag `<style>`
4. Deploy ke aplikasi Heroku
