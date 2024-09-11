tautan menuju aplikasi PWS yang sudah di-deploy: http://rizki-hidayatul-icecreamy.pbp.cs.ui.ac.id/

Jawab:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Hal pertama yang saya lakukan adalah membuat sebuah direktori utama lokal yang diberi nama ice_creamy. 
2. Kemudian, saya membuat dan mengaktifkan virtual environment.
3. Setelah itu, saya membuat file requirements.txt yang diisi dengan beberapa dependencies dan melakukan instalasi terhadap dependencies tersebut.
4. Kemudian saya meng-Setup Proyek Django. Melakukan instalasi django dan membuat project ice_creamy dengan perintah 'django-admin startproject ice_creamy'. 
5. Menambahkan Berkas .gitignore yang digunakan sebagai konfigurasi pada repositori git untuk memilah berkas apa saja yang perlu diabaikan ketika nanti dipush
6. Setting Github dengan nama seperti direktori sebelumnya yaitu ice_creamy. Kemudian saya menginisiasi direktori lokal ice_creamy sebagai repositori git. Setelah itu melakukan add, commit, dan push dari direktori lokal
7. Langkah selanjutnya yaitu membuat Aplikasi Django dengan nama 'main' dan mendaftarkan aplikasi di 'settings.py' agar Django dapat mengenali aplikasi tersebut.
8. Setelah membuat aplikasi django, saya membuat berkas template html, lalu mengisinya dengan berkas main.html
9. Membuat Model. Mengubah berkas 'models.py' sesuai dengan ketentuan soal. 
10. Setelah itu, melakukan migrasi model agar perubahan model yang terjadi dapat diketahui oleh server.
11. Kemudian, membuat views. Melakukan integrasi model, views, dan template pada berkas 'views.py'. Fungsinya untuk mengatur http agar dapat mengembalikan tampilan yang sesuai. Lalu melakukan modifikasi pada template agar dapat menampilkan data.
12. Melakukan routing URL. Menambahkan 'urls.py' pada direktori main agar dapat mengambil modul main views sebagai tampilan ketika mengakses url. 
13. Terakhir, saya mengecek website saya melalui local host dengan menjalankan server django. Kebetulan tidak terjadi error, sehingga saya tidak perlu melakukan trouble shooting. ><

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src="bagan_no2.jpg" width="1802" height="619">
Bagan di atas merupakan konsep dan arsitektur MVT pada django. User mengirim request ke internet dan internet meneruskan request tersebut kepada file django untuk komponen2 MVT ini.
M: Model:  mengatur dan mengelola seluruh data pada aplikasi. Model mewakili struktur data dan logika aplikasi di belakang tampilan web.
V: View: view mengontrol bagaimana data yang dikelola oleh model dapat ditampilkan kepada user. Ini merupakan komponen yang menangani logika presentasi dalam konsep MVT
T: Template: mengatur tampilan interface pengguna dengan memisahkan kode HTML dari loika aplikasi. 

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Menurur dcloud.co.id, git merupakan software debelopment yang berfungsi sebagai sistem kontrol versi (version control system) untuk menyimpan, mengelola, dan berbagi kode sumber secara efisien dan kolaboratif. Menurut pengalaman saya, penggunaan git berfungsi agar dapat melacak perubahan kode proyek yang dibuat programmer. Selain itu, penggunaan git memungkinkan developer bekerja secara kolaboratif dalam tim. 
sources:https://dcloud.co.id/blog/apa-itu-git.html#:~:text=Git%20adalah%20alat%20software%20development,code)%20secara%20efisien%20dan%20kolaboratif. 

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut sumber belajar pbp di scele, ada beberapa alasan django dijadikan permulaan pembelajaran pengembangan software, yaitu:
- Open sources: siapapun dapat mengakses, memodifikasi, dan mendistribusikan kode secara gratis. Ini membuat django mudah diakses bagi para pelajar yang ingin mulai belajar tanpa memerlukan biaya lisensi
- Ridiculously Fast: Django dirancang untuk membantu pengembang membangun aplikasi web dengan cepat. Sehingga menjadikan django ramah bagi pemula.
- Fully loaded: django memiliki banyak fitur bawaan seperti sistem autentikasi, manajemen konten admin, ORM (Object-Relational Mapping) untuk database, dan lainnya.
- Reassuringly secure: Framework django dilengkapi dengan perlindungan terhadap serangan umum seperti  SQL injection, cross-site scripting (XSS), dan cross-site request forgery (CSRF)
- Exceedingly Scalable: aplikasi yang dibangun dengan Django dapat dengan mudah menangani peningkatan trafik pengguna atau kompleksitas fitur seiring dengan pertumbuhan aplikasi. Hal ini menjadikan django ideal untuk belajar sekaligus memungkinkan ekspansi aplikasi tanpa harus mengganti framework.
- Incredibly Versatile: Django sangat serbaguna dan dapat digunakan untuk berbagai jenis aplikasi web. Fleksibilitas ini memungkinkan untuk bereksperimen dengan berbagai tipe aplikasi web tanpa harus mempelajari framework baru.
sources: https://revou.co/kosakata/django , https://www-netguru-com.translate.goog/blog/django-apps-examples?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc (+dibantu chatgpt)

5. Mengapa model pada Django disebut sebagai ORM? 
Model pada Django disebut sebagai ORM (Object-Relational Mapper) karena Django menggunakan ORM untuk mempermudah interaksi antara kode Python dan basis data. Dalam ORM Django, data dari basis data diubah menjadi objek Python, yang lebih mudah dimanipulasi. Ini berarti bahwa tabel dan kolom dalam database dipetakan menjadi kelas dan atribut Python, sehingga kita dapat melakukan operasi database seperti menyimpan, mengambil, memperbarui, atau menghapus data hanya dengan menggunakan sintaks Python, tanpa perlu menulis SQL secara eksplisit.
sources: https://sohaibanser.medium.com/django-orm-pros-and-cons-8ab069598c1b 