tautan menuju aplikasi PWS yang sudah di-deploy: http://rizki-hidayatul-icecreamy.pbp.cs.ui.ac.id/

TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Hal pertama yang saya lakukan adalah membuat sebuah direktori utama lokal yang diberi nama ice_creamy. 
   - Kemudian, saya membuat dan mengaktifkan virtual environment.
   - Setelah itu, saya membuat file requirements.txt yang diisi dengan beberapa dependencies dan melakukan instalasi terhadap dependencies tersebut.
   - Kemudian saya meng-Setup Proyek Django. Melakukan instalasi django dan membuat project ice_creamy dengan perintah 'django-admin startproject ice_creamy'. 
   - Menambahkan Berkas .gitignore yang digunakan sebagai konfigurasi pada repositori git untuk memilah berkas apa saja yang perlu diabaikan ketika nanti dipush
   - Setting Github dengan nama seperti direktori sebelumnya yaitu ice_creamy. Kemudian saya menginisiasi direktori lokal ice_creamy sebagai repositori git. Setelah itu melakukan add, commit, dan push dari direktori lokal
   - Langkah selanjutnya yaitu membuat Aplikasi Django dengan nama 'main' dan mendaftarkan aplikasi di 'settings.py' agar Django dapat mengenali aplikasi tersebut.
   - Setelah membuat aplikasi django, saya membuat berkas template html, lalu mengisinya dengan berkas main.html
   - Membuat Model. Mengubah berkas 'models.py' sesuai dengan ketentuan soal. 
   - Setelah itu, melakukan migrasi model agar perubahan model yang terjadi dapat diketahui oleh server.
   - Kemudian, membuat views. Melakukan integrasi model, views, dan template pada berkas 'views.py'. Fungsinya untuk mengatur http agar dapat mengembalikan tampilan yang sesuai. Lalu melakukan modifikasi pada template agar dapat menampilkan data.
   - Melakukan routing URL. Menambahkan 'urls.py' pada direktori main agar dapat mengambil modul main views sebagai tampilan ketika mengakses url. 
   - Terakhir, saya mengecek website saya melalui local host dengan menjalankan server django. Kebetulan tidak terjadi error, sehingga saya tidak perlu melakukan trouble shooting. ><

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src="bagan_no2.jpg" width="1802" height="330">
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

5. Mengapa model pada Django disebut sebagai ORM?##
Model pada Django disebut sebagai ORM (Object-Relational Mapper) karena Django menggunakan ORM untuk mempermudah interaksi antara kode Python dan basis data. Dalam ORM Django, data dari basis data diubah menjadi objek Python, yang lebih mudah dimanipulasi. Ini berarti bahwa tabel dan kolom dalam database dipetakan menjadi kelas dan atribut Python, sehingga kita dapat melakukan operasi database seperti menyimpan, mengambil, memperbarui, atau menghapus data hanya dengan menggunakan sintaks Python, tanpa perlu menulis SQL secara eksplisit.
sources: https://sohaibanser.medium.com/django-orm-pros-and-cons-8ab069598c1b 


TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam implementasi sebuah platform karena memungkinkan pertukaran informasi/data antara server dengan pengguna (seperti aplikasi web atau mobile). Pada umumnya, platform terdiri dari beberapa begian yang saling terhubung dan berkomunikasi. Data Delivery digunakan agar setiap bagian ini dapat saling berkomunikasi.
Misalnya, ketika user mengirimkan informasi/data (misalnya mengisi form), server akan menerima, memproses, lalu mengirimkan respons kepada pengguna. Tanpa adanya data delivery, setiap bagian pada platform tidak dapat bekerja dengan optimal karena tidak dapat berbagi informasi.
Selain itu, data delivery mempunyai peran penting dalam implementasi sebuah platform, diantaranya yaitu:
- Real-time data delivery, dimana memungkinkan pengguna dapat selalui melihat pembaruan data terbaru secara real time.
- User experience yang responsif dan akurat, karena dengan data delivery, user dapat mengakses informasi secara real-time dan akurat.
- Integrasi Data. Data delivery yang efektif memastikan bahwa komunikasi antara platform dengan sistem lain berjalan dengan lancar.
- Keamanan data: Data delivery yang baik mencakup enkripsi dan perlindungan data saat dalam proses pengirimannya.
  
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dari pada XML. Alasan mengapa JSON lebih populer menurut saya yaitu:
- Syntax yang lebih simple.  JSON memiliki struktur yang lebih ringkas daripada XML.  JSON menggunakan kurung kurawal {} untuk objek dan tanda kurung siku []untuk array, yang membuatnya ringkas dan jelas. Sebaliknya, XML menggunakan tag pembuka dan penutup seperti <tag></tag>, yang membuatnya lebih panjang dan tidak seefisien JSON.
- Ukuran JSON lebih kecil. Karena sytax yang lebih sederhana dan simple, file JSON biasanya lebih kecil ukurannya dari pada xml. Sehingga, pengiriman data lebih cepat dan hemat bandwidth. Dalam pengembangan aplikasi web dan mobile, sering kali bekerja dengan data dalam jumlah besar, sehingga hal ini menjadi perlu diperhatikan.
- Kemudahan dalam Parsing. Parsing dalam JSON dapat dilakukan parsing menggunakan fungsi JavaScript standar. Sedangkan parsing XML harus dengan parser XML, dimana dapat memperlambat dan mempersulit prosesnya. Hal ini juga mempengaruhi waktu dalam memproses data, dimana JSON akan lebih cepat dari pada XML.
- Selain itu, JSON juga lebih kompatibel dengan banyak bahasa pemrograman sehingga bagus untuk digunakan dalam banyak platform
source: https://www.directual.com/blog/json-and-xml-which-one-is-better-for-no-coders

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Kita memerlukan method is_valid() pada form Django untuk memvalidasi/memeriksa apakah data yang dikirimkan melalui form sudah benar sesuai aturan yang ditentukan. Jika datanya valid, is_valid() akan mengembalikan True dan menyediakan data yang bersih (cleaned data) untuk diproses lebih lanjut. Hal ini diperlukan agar aplikasi hanya menerima data yang benar (yang sudah diproses oleh method is_valid) sebelum di proses, seperti disimpan ke database. Hal ini dapat mencegah kesalahan atau masalah keamanan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token dibutuhkan saat membuat form di Django karena csrf_token penting untuk menlindungi dari serangan CSRF (Cross-Site Request Forgery). csrf_token bekerja dengan memastikan setiap permintaan yang adamodifikasi data berasal dari sumber yang benar. Tanpa validasi csrf_token, aplikasi Django tidak bisa membedakan antara permintaan dari pengguna dan permintaan berbahaya dari pihak ketiga. Dengan hal ini, aplikasi menjadi lebih aman dari serangan yang memanfaatkan user session yang sah tanpa sepengatahuan user.
source: https://www.geeksforgeeks.org/csrf-token-in-django/ 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pada tugas ini, saya diminta untuk membuat input form dan menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID, serta membuat routing URL di masing-masing views.
Berikut langkah-langkah yang saya kerjakan:

a. Membuat forms.py di direktori main untuk membuat form input data Product menggunakan field ['name', 'price', 'description', 'quantity', 'stock', 'rating'].

b. Implementasi fungsi create_product pada views.py untuk menampilkannya di template HTML.
Saya melakukan import forms yang baru dibuat dengan menambahkan import redirect. Saya lalu membuat fungsi baru yaitu create_product untuk melakukan validasi input form dan menambahkan data yang ditambah user pada form. Selanjutnya, pada fungsi show_main, saya menambahkan kode Product.object.all() untuk mengambil semua objek dari model Product yang ada pada database. Nilai ini kemudian disimpan pada variable products dan dimasukkan ke context, lalu dikirimkan ke HTML agar dapat ditampilkan pada website.

c. Melaukan routing URL
Hal ini dilakukan dengan mengimport fungsi create_product pada urls.py dan menambahkan path untuk mengakses fungsi create_product.

d. Membuat tampilan pada template HTML.
Ini dilakukan dengan membuat file html baru, yaitu create_product.html pada direktori main/templates. <form method = "POST"> ditambahkan untuk menandakan block untuk form yang menggunakan metode POST. Selain itu, ditambah juga {% csrf_token %} yang fungsinya dijelaskan pada no 4 di atas.

e. Membuat 4 fungsi untuk mengembalikan data dalam bentuk XML dan JSON, yaitu show_xml, show_json, show_xml_by_id, dan show_json_by_id di file views.py.

f. Melakukan routing URL di masing-masing views. Hal ini dilakukan dengan Menambahkan path untuk menampilkan page yang dapat melihat database.

g. Add, commit, dan push ke github untuk menyimpan perubahan.

##Dokumentasi Postman##
![postman_xml](https://github.com/user-attachments/assets/93cb2d56-5663-452a-a309-7056d2d38e86)
![postman_xml_id](https://github.com/user-attachments/assets/ccd43db2-1cd4-406d-979a-fedcb73bf232)
![postman_json](https://github.com/user-attachments/assets/0cd6017f-853c-4267-8aab-070cdff4645b)
![postman_json_id](https://github.com/user-attachments/assets/fb0f0a7c-f59d-4d6c-9f19-402d7a9622ba)

