def menu_chatbot():
    while True:
        print("====================================")
        print("= Selamat Datang di fitur Chatbot  =")
        print("====================================")
        # user memilih pilihan sesuai keadaan user
        print("\nPilih opsi:")
        print("1. Burnout")
        print("2. Depresi")
        print("3. Stres")
        print("4. Kecemasan")
        print("5. Keluar")
        pilih = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilih == "1":
            burnout()
        elif pilih == "2":
            depresi()
        elif pilih == "3":
            stres()
        elif pilih == "4":
            kecemasan()
        elif pilih == "5":
            print("Terima kasih sudah berkunjung ke menu fitur chatbot, selamat tinggal.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4 atau 5.")        

def burnout():
    print("Kamu mengunjungi halaman ini karena merasa mengalami gejala-gejala burnout berikut ?")
    print("- Hilangnya semangat berkerja")
    print("- Performa kerja menurun")
    print("- Mudah sakit")
    print("- Mudah marah")
    print("- Menarik diri dari lingkungan")

    print("\nKami menyediakan beberapa artikel")
    print("\nPilih opsi artikel :")
    print("1. 5 Cara Efektif Mencegah Parental Burnout")
    print("2. Mengenal Lebih Jauh Tentang Burnout")
    print("3. Keluar")
    pilih = input("Masukkan pilihan (1/2/3): ")

    if pilih == "1":
        print("\n5 Cara Efektif Mencegah Parental Burnout")
        print("\nMenurut penelitian dalam Clinical Psychological Science (2019),parental burnout adalah kelelahan yang intens pada orang tua yang mengakibatkan perasaan berjarak secara emosional dari anak-anaknya disertai keraguan akan kemampuan mereka sebagai orang tua. Ketika mengalami burnout, orangtua merasa sangat lelah dan suasana hati menjadi mudah berubah seperti mudah marah. Parental burnout berisiko memengaruhi kualitas hubungan orang tua dan anak, seperti contohnya orangtua yang mengalami burnout dapat memiliki pemikiran untuk pergi dari anak-anak, dapat mengabaikan anak-anak mereka, atau bahkan melakukan kekerasan terhadap anak baik secara fisik dan emosional.  Orangtua yang mengalami burnout juga seringkali merasa terjebak dalam peran mereka sebagai orangtua, ketika burnout ini sudah sangat parah, mereka dapat merasakan keinginan bunuh diri dan melarikan diri. ")
        print("\nBerikut merupakan 5 cara efektif untuk mencegah terjadinya parental burnout:")
        print("\n1. Ambil jeda sejenak")
        print("\nmengambil jeda sejenak dari peran sebagai orangtua dan menyisihkan waktu untuk diri sendiri merupakan hal yang krusial. Jeda yang dimaksud tidak selalu harus dalam waktu yang lama, contohnya kita bisa mengunci diri di dalam kamar mandi selama 10 menit untuk mengambil nafas panjang, atau duduk di mobil sambil mengatur nafas dan beristirahat sejenak. Jika memungkinkan, lakukan hal yang menyenangkan untuk diri sendiri dalam jeda yang ada. ")
        print("\n2. Berolahraga")
        print("\nKetika berolahraga, otak akan melepaskan endorfin, zat kimia saraf yang memicu perasaan senang dan bahagia. Selain itu, dengan berolahraga maka kita dapat merasa lebih bertenaga.")
        print("\n3. Mendengarkan Musik")
        print("\nMusik adalah salah satu hal yang dapat mengubah suasana hati dan perspektif kita. Manfaat mendengarkan musik sangat banyak, seperti meningkatkan kualitas tidur, meningkatkan pembelajaran dan memori, mengurangi depresi, meningkatkan produktivitas, dan meningkatkan kesenangan. Ketika mendengarkan musik yang disukai, otak akan melepaskan dopamin, zat kimia saraf yang memicu perasaan senang dan bahagia. Penelitian juga menunjukkan bahwa mendengarkan musik yang menenangkan dapat mengurangi stres dan kecemasan dengan cara menurunkan detak jantung dan tekanan darah.")
        print("\n4. Bersosialisasi")
        print("\nMengasuh anak dapat membuat kita merasa kesepian. Jangan biarkan peran sebagai orangtua memudarkan hubungan pertemanan, teman merupakan salah satu support system penting bagi kita para orangtua. Penelitian telah berulang kali menunjukkan bahwa memiliki support system yang sehat dapat mengurangi stres, mencegah penyakit, dan meningkatkan kualitas hidup secara keseluruhan. Ketika hidup sebagai orangtua terasa melelahkan, luangkan waktu berkualitas dengan teman atau keluarga sehingga kita dapat mengisi energi kita kembali sebagai individu.")
        print("\n5. Delegasikan Tugas")
        print("\nMenjadi orangtua bukan berarti kita menjadi manusia super, tidak harus semua tugas kita kerjakan seorang diri. Jika ada tugas-tugas yang dapat didelegasikan, seperti mencuci pakaian atau membersihkan, tentunya boleh kita delegasikan pada orang lain atau support system yang dapat membantu kita. Contohnya, sesekali ketika sangat lelah kita dapat menggunakan jasa laundry atau jasa pembersih rumah untuk membantu kita menyelesaikan pekerjaan rumah.")

        #Jika tidak memasukkan angka 1 maka akan akan keluar dari artikel dan akan di arahkan ke menu burnout
        print("\nPilih opsi:")
        print("1. Keluar")
        pilih = input("Masukkan (1) Jika ingin Keluar dari Artikel : ")
        if pilih == "1":
            burnout()
        else:
            print("Pilihan tidak valid. Anda langsung dikembalikan ke menu awal Chatbot")

    elif pilih == "2":
        print("\nMengenal Lebih Jauh Tentang Burnout")
        print("\nBurnout pertama kali diteliti oleh Freudenberger, seorang psikiater, pada tahun 1975. Ia mengobservasi pekerja di klinik tempatnya bekerja. Kemudian penelitian tentang burnout juga banyak dilakukan oleh Maslach dan Leiter, dimulai dari tahun 1976, dimana Maslach banyak mewawancarai pekerja sosial (Maslach, Schaufeli, & Leiter, 2001).")
        print("\nTerdapat tiga dimensi dari burnout, antara lain: ")
        print("\n1. Merasakan kelelahan yang amat sangat, atau disebut exhaustion. Kelelahan yang amat sangat ini menjadi gejala utama yang paling terlihat pada kondisi burnout (Leiter, Maslach, & Frame, 2015). Kelelahan yang dirasakan tidak seperti kelelahan biasa, tetapi lebih jauh lagi, individu akan merasakan kehabisan energi, seperti terkuras habis. ")
        print("\n2. Depersonalisasi atau merasa berjarak dengan pekerjaan. Beberapa teori menyebut kondisi ini sebagai sinisme, dimana individu menjadi bersikap sinis terhadap pekerjaannya, dengan tujuan menjauhkan diri dari pekerjaannya. Sikap yang muncul misalnya menunjukkan sikap yang tidak pantas terhadap klien, mudah tersinggung, kehilangan idealisme diri, dan menghindar dari pekerjaan yang seharusnya dilakukan. ")
        print("\n3. Perasaan inefficacy atau merasa mengalami penurunan pencapaian personal. Misalnya terjadi penurunan produktivitas kerja, moral kerja yang menurun, dan merasa tidak sanggup untuk menghadapi beban kerja.")
        print("\nBurnout memang tidak diklasifikasikan dalam gangguan kondisi mental, tetapi tetap perlu perhatian yang serius. Penanganan yang tepat diperlukan karena dampak burnout bisa menyebar ke berbagai aspek kehidupan yang lain, termasuk menurunnya kondisi kesehatan fisik dan memicu masalah mental lainnya.")
        print("\nOleh karena itu, cobalah sadari kondisi diri jika sudah mulai merasa kelelahan ketika bekerja, karena ini bisa jadi tanda awal kita mengalami tekanan, yang jika tidak tertangani, bisa menjadi burnout. Jangan abaikan kelelahan yang dirasakan itu, segera lakukan self-care, termasuk istirahat yang cukup, perhatikan pola makan dan tidur, dan sebisa mungkin atur kegiatanmu agar work-life balance tetap terjaga.")

         #Jika tidak memasukkan angka 1 maka akan akan keluar dari artikel dan akan di arahkan ke menu burnout
        print("\nPilih opsi:")
        print("1. Keluar")
        pilih = input("Masukkan (1) Jika ingin Keluar dari Artikel : ")
        if pilih == "1":
            burnout()
        else:
            print("Pilihan tidak valid. Anda langsung dikembalikan ke menu awal Chatbot")
    
    elif pilih == "3":
        print("Anda kembali ke menu awal Chatbot")
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

def depresi():
    print("Kamu mengunjungi halaman ini karena merasa mengalami gejala-gejala depresi berikut ?")
    print("- Selalu dibebani rasa bersalah")
    print("- Merasa putus asa")
    print("- Merasa tidak berharga")
    print("- Selalu merasa cemas")
    print("- Sedih yang berkelanjutan")
    print("Apabila kamu mengalami gejala di atas dan sedang mencari solusi untuk mengatasinya, tenaga profesional kami siap membantumu")

    print("\nKami menyediakan beberapa artikel")
    print("\nPilih opsi artikel:")
    print("1. Menjadi teman yang baik: 3 langkah sederhana untuk mendukung Ibu yang mungkin mengalami depresi.")
    print("2. Apa itu depresi?")
    print("3. Keluar")
    pilih = input("Masukkan pilihan (1/2/3): ")

    if pilih == "1":
        print("\nMenjadi teman yang baik: 3 langkah sederhana untuk mendukung Ibu yang mungkin mengalami depresi.")
        print("\nMenjadi seorang Ibu bukan sebuah tugas yang mudah. Mengasuh anak dinobatkan sebagai salah satu pekerjaan penuh tekanan yang setara dengan dokter bedah saraf dan pilot. Ibu tidak hanya mengasuh anak dengan menyediakan kebutuhan materil seperti makanan dan pakaian, tapi juga bertanggung jawab untuk menciptakan dan menjaga bonding emosional dengan anak.")
        print("\nMeskipun semua Ibu mengalami tekanan dan hari-hari yang berat dalam perjalanan mereka membesarkan sang kecil, namun ketika Ibu mengalami depresi tentu tekanan yang dirasakan lebih besar. Ibu bisa merasa putus asa dan tidak terhubung secara emosional dengan sang anak. Ibu juga mungkin kesulitan menemukan energi untuk melakukan sesuatu dengan anak, yang dapat menyebabkan rasa bersalah dan rendah diri. Kemudian, perasaan itu membuat Ibu semakin sulit untuk merasa termotivasi dalam mengasuh anak mereka. Hal ini tentunya berdampak pada sang anak.")
        print("\nBerikut merupakan tiga langkah yang dapat kalian lakukan sebagai seorang teman dari Ibu yang mungkin mengalami depresi :")
        
        print("\n1. Tanyakan keadaan dan perasaan Ibu")
        print("\nLangkah pertama menjadi teman yang baik bagi Ibu yang mengalami depresi adalah dengan mengajak mereka berbicara, hal ini dapat dilakukan dengan bertanya mengenai keadaan mereka serta perasaan mereka. Berikut merupakan beberapa contoh pertanyaan sederhana")
        print("\n- Bagaimana keadaanmu?")
        print("\n- Bagaimana perasaanmu saat ini menjalani tugas seorang Ibu yang tidak mudah?")

        print("\n2. Dorong Ibu untuk melakukan hal-hal yang dapat membuatnya merasa lebih baik")
        print("\nSeorang ibu mungkin mengaku merasa sedih, stres, atau kewalahan. Berikut adalah beberapa hal yang dapat kamu lakukan sebagai teman untuk membantu Ibu meningkatkan suasana hatinya:")
        print("\n- Jadilah pendengar yang baik, buat temanmu merasa aman dan diterima saat membicarakan perasaannya")
        print("\n- Dorong dia untuk menjaga rutinitasnya")
        print("\n- Dukung dan bantu temanmu untuk tetap menjaga hubungan dengan orang-orang penting")
        
        print("\n3. Bantu dan Dukung Temanmu Mencari Bantuan Profesional")
        print("\nJika temanmu menunjukkan gejala depresi yang cukup serius, mungkin ia tidak dapat berfungsi dengan baik di pekerjaannya, tugasnya sebagai ibu, atau aspek kehidupan lainnya. Pada fase ini, kamu bisa membantu temanmu mendapatkan bantuan profesional.")

        #Jika tidak memasukkan angka 1 maka akan akan keluar dari artikel dan akan di arahkan ke menu depresi
        print("\nPilih opsi:")
        print("1. Keluar")
        pilih = input("Masukkan (1) Jika ingin Keluar dari Artikel : ")
        if pilih == "1":
            depresi()
        else:
            print("Pilihan tidak valid. Anda langsung dikembalikan ke menu awal Chatbot")

    elif pilih == "2":
        print("\nApa itu depresi?")

        print("\nDepresi adalah salah satu bentuk kondisi kesehatan mental yang dialami banyak orang dan sering kali muncul berbarengan dengan kecemasan. Depresi bisa ringan dan sementara, atau berat dan berkepanjangan. Ada orang-orang yang mengalami depresi hanya sekali dalam hidupnya; ada pula yang mengalaminya berkali-kali. Depresi bisa berujung pada tindak bunuh diri, tetapi hal ini bisa dicegah dengan dukungan yang tepat. Penting untuk mengetahui bahwa ada banyak hal yang bisa dilakukan untuk membantu anak-anak muda yang memiliki dorongan untuk melakukan tindakan ini.")
        
        print("\nApa penyebab depresi?")
        print("\nDepresi bisa terjadi sebagai reaksi terhadap suatu peristiwa, misalnya penganiayaan, kekerasan di sekolah, kematian orang terdekat, atau masalah keluarga seperti kekerasan di dalam rumah tangga ataupun perpisahan orang tua. Seseorang bisa mengalami depresi setelah merasa stres untuk waktu yang lama. Depresi juga bisa diturunkan di dalam keluarga. Selain itu, ada kalanya kita tidak tahu mengapa depresi timbul")
        
        print("\nTanda dan gejala depresi")
        
        print("\nGejala fisik:")
        print("- Lelah atau tidak ada energi, meskipun sudah beristirahat")
        print("- Gelisah atau sulit berkonsentrasi")
        print("- Kesulitan melakukan kegiatan sehari-hari")
        print("- Perubahan selera makan atau pola tidur")
        print("- Rasa nyeri atau sakit yang muncul tanpa sebab tertentu")

        print("\nGejala emosional dan mental:")
        print("- Rasa sedih, cemas, atau mudah marah yang terus-menerus")
        print("- Hilang minat untuk bergaul dan melakukan kegiatan yang biasanya disukai")
        print("- Menarik diri dari orang lain dan merasa kesepian")
        print("- Merasa tidak berharga, tidak punya harapan, atau merasa bersalah")
        print("- Mengambil tindakan-tindakan berisiko yang tidak biasanya dilakukan")

        #Jika tidak memasukkan angka 1 maka akan akan keluar dari artikel dan akan di arahkan ke menu depresi
        print("\nPilih opsi:")
        print("1. Keluar")
        pilih = input("Masukkan (1) Jika ingin Keluar dari Artikel : ")
        if pilih == "1":
            depresi()
        else:
            print("Pilihan tidak valid. Anda langsung dikembalikan ke menu awal Chatbot")

    elif pilih == "3":
        print("Anda kembali ke menu awal Chatbot")
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

def stres():
    print("Kamu mengunjungi halaman ini karena merasa mengalami gejala-gejala stres berikut ?")
    print("- Suasana hati berubah-ubah")
    print("- Sering gelisah dan murung")
    print("- Sulit fokus dan konsentrasi")
    print("- Merasa tidak percaya diri")
    print("- Badan terasa pegal dan nyeri")
    print("Apabila kamu mengalami gejala di atas dan sedang mencari solusi untuk mengatasinya, tenaga profesional kami siap membantumu")

    print("\nKami menyediakan beberapa artikel")
    print("\nPilih opsi artikel :")
    print("1. Apa itu Stres?")
    print("2. Keluar")
    pilih = input("Masukkan pilihan (1/2): ")

    if pilih == "1":
        print("\nApa itu Stres?")
        print("\nStres mengacu pada gangguan ritme alami tubuh. Hal ini biasanya terjadi sebagai respons terhadap perubahan lingkungan positif maupun negatif yang dirasakan seseorang di luar kendali mereka. Setiap orang akan mengalami stres sepanjang hidup mereka, namun pada tingkat tertentu stres dapat menjadi berbahaya jika tidak ditangani dengan tepat.")
        print("\nBagaimana cara kerja stres?")
        print("\nPerubahan fisiologis terjadi ketika seseorang dihadapkan dengan stressor yaitu merasakan tantangan atau situasi berbahaya. Secara khusus, 'insting melarikan diri atau melawan' kita diaktifkan, mempersiapkan kita untuk menghadapi ancaman itu. Perubahan ini dapat mencakup:")
        print("- Perubahan aliran darah")
        print("- Peningkatan denyut jantung")
        print("- Bernafas lebih cepat")
        print("- Otot mengencang")
        print("- Peningkatan tekanan darah")
        print("\nMeskipun dalam stres jangka pendek perubahan ini dapat membantu kita mengatasi stres, namun stres jangka panjang dapat mempengaruhi tubuh dan pikiran secara negatif.")
        print("\nJenis-jenis stres")
        print("\n- Stres akut")
        print("\nIni adalah bentuk stres yang paling umum. Stres ini muncul dari tekanan yang dirasakan atau baru saja dialami. Stres ini biasanya relatif singkat dan memiliki efek jangka panjang yang  terbatas pada kesehatan mental dan fisik. Contoh umumnya antara lain disebabkan oleh terlambat bekerja, mengalami kecelakaan mobil, atau berbicara di depan umum.")
        print("\n- Stres akut episodik")
        print("\nStres akut episodik terjadi ketika seseorang sering mengalami stres akut. Individu yang rentan terhadap jenis stres ini dapat dikategorikan ke dalam dua kelompok, yaitu:")
        print("\n1. Individu dengan gaya hidup yang penuh tekanan")
        print("\n2. Individu yang sedang mengalami kecemasan")
        print("\nStres kronis")
        print("\nStres kronis disebabkan oleh situasi stres yang terjadi terus-menerus atau dari anggapan bahwa  lingkungan tertentu sebagai ancaman. Stres kronis dapat diinternalisasi, yang berarti seseorang dapat belajar bagaimana hidup di dalamnya dan perlahan mungkin lupa bahwa tekanan ini ada.")
        print("\nAkibat dari stres")
        print("\n1. Peningkatan gejala depresi, gangguan depresi mayor, penyalahgunaan obat-obatan, dan ketergantungan alkohol.")
        print("2. Masalah kesehatan seperti:")
        print("\n- Sakit kepala")
        print("- Penyakit jantung")
        print("- Tekanan darah tinggi")
        print("- Nyeri otot")
        print("- Sakit perut")
        print("- Masalah pencernaan")
        print("- Tidur terganggu")
        print("Ingatlah bahwa stres dalam jangka pendek terkadang bisa bermanfaat dan berguna sampai batas tertentu. Namun, akan menjadi berbahaya bagi kesehatan jika tidak dikelola dengan baik.")
        print("\nCara Mengelola Stres")
        print("\n1. Teknik relaksasi")
        print("2. Identifikasi penyebab stres dalam hidupmu")
        print("3. Perubahan gaya hidup:")
        print("\n- Tidur yang cukup")
        print("- Olahraga")
        print("- Hindari atau kurangi konsumsi kafein, gula, alkohol, obat-obatan, dan nikotin")

         #Jika tidak memasukkan angka 1 maka akan akan keluar dari artikel dan akan di arahkan ke menu stres
        print("\nPilih opsi:")
        print("1. Keluar")
        pilih = input("Masukkan (1) Jika ingin Keluar dari Artikel : ")
        if pilih == "1":
            stres()
        else:
            print("Pilihan tidak valid. Anda langsung dikembalikan ke menu awal Chatbot")

    elif pilih == "2":
        print("Anda kembali ke menu awal Chatbot")
    else:
        print("Pilihan tidak valid. Silakan pilih 1, atau 2.")

def kecemasan():
    print("Kamu mengunjungi halaman ini karena merasa mengalami gejala-gejala kecemasan (anxiety) berikut ?")
    print("- Gugup, gelisah dan tegang")
    print("- Detak jantung cepat")
    print("- Sulit atau tidak bisa tidur")
    print("- Sulit berkonsentrasi")
    print("- Selalu dibebani rasa bersalah")
    print("Apabila kamu mengalami gejala di atas dan sedang mencari solusi untuk mengatasinya, tenaga profesional kami siap membantumu")

    print("\nKami menyediakan beberapa artikel")
    print("\nPilih opsi artikel :")
    print("1. Satu cara untuk mengurangi kecemasan akibat overthinking")
    print("2. Keluar")
    pilih = input("Masukkan pilihan (1/2): ")

    if pilih == "1":
        print("\nSatu cara untuk mengurangi kecemasan akibat overthinking")
        print("\nSebagai manusia, kita memiliki kecenderungan untuk mengantisipasi masa depan. Kemampuan manusia untuk berpikir ke depan merupakan komponen penting dari fungsi otak manusia. Sayangnya, seringkali manusia terjebak dalam sebuah pola pikir negatif yang dilakukan secara berlebihan dan akhirnya menyebabkan kecemasan. Salah satu bentuknya adalah ketika seseorang cenderung memprediksi masa depan dengan kemungkinan-kemungkinan terburuk, seperti “Bagaimana kalau saya gagal dalam wawancara pekerjaan ini?” atau “Bagaimana kalau saya tidak bisa membiayai perkuliahan anak saya?”.")
        print("\nSebenarnya, dibalik pertanyaan “bagaimana kalau” tersebut, seringkali terdapat ketakutan yang mendasari. Contohnya, ketakutan akan kegagalan, penolakan, kehilangan, dan rasa tidak aman. Sayangnya, cara berpikir ini justru memperkuat rasa takut kita dan menambah kecemasan.")
        print("\nSolusi yang dapat dilakukan untuk merubah pola pikir ini adalah dengan menjawab pikiran-pikiran tersebut dengan jawaban “kalau, maka”. Sekarang, mari kita coba dengan dua contoh di atas.")
        print("\n“Kalau saya gagal dalam wawancara pekerjaan ini, maka saya akan mencari kesempatan wawancara di perusahaan lain.”")
        print("\nDengan menerapkan pola pikir ini, kita dapat menyadari bahwa kemungkinan-kemungkinan yang kita takuti belum terjadi dan mungkin tidak akan pernah terjadi. Pola pikir “kalau, maka” ini juga mengingatkan kalaupun hal buruk yang kita pikirkan terjadi, sebenarnya kita memiliki pilihan, keberdayaan, dan kemampuan untuk menangani hal tersebut.")
        print("\nAgar kita dapat menerapkan pola berpikir “kalau, maka” ini membutuhkan latihan. Awalnya, mungkin tidak terasa alami. Namun, ada baiknya mencoba pendekatan ini karena pada akhirnya akan membantu kita mengurangi kecemasan akibat overthinking khususnya akan skenario-skenario masa depan yang belum tentu terjadi.")
        
         #Jika tidak memasukkan angka 1 maka akan akan keluar dari artikel dan akan di arahkan ke menu kecemasan
        print("\nPilih opsi:")
        print("1. Keluar")
        pilih = input("Masukkan (1) Jika ingin Keluar dari Artikel : ")
        if pilih == "1":
            kecemasan()
        else:
            print("Pilihan tidak valid. Anda langsung dikembalikan ke menu awal Chatbot")
    elif pilih == "2":
        print("Anda kembali ke menu awal Chatbot")
    else:
        print("Pilihan tidak valid. Silakan pilih 1, atau 2.")