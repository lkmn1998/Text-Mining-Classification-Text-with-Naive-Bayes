
# coding: utf-8

# In[2]:

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import numpy as np

factory = StemmerFactory()
stemmer = factory.create_stemmer()

#0
D1 = 'nama1 sudah selesai belum machine learningnya ?'
D2 = 'nama1 nomor kamu yang ini kan? bentar ayu sms kalau sudah depan kosan iya' 
D3 = 'nama1 saya ke kosan iya, mau nanya2 juga soal laporan.. boleh tidak?'
D4 = 'nama1, minta controller dan view nya aja.'
D5 = 'nama1, minta database kamu sama view dan controller yang ada js buat dropdown kotanya.'
D6 = 'nama1 bisa pakai flash buat animasi tidak?? Atau pakai movie maker??'
D7 = 'nama1 ke point inti?' 
D8 = 'nama1 di kosan tidak? Mau numpang dong'
#1
D9 = 'Uangnya di Transfer di BNI ini aja atas nama RASTINA Nomor .Rekening.0253 7915 37. Kalau sudah di Transfer Sms saja di nomor ini 085293355598 Terima kasih.'
D10 = 'Uangnya dikirim saja ke Rekening ini, Bank BNI atas nama SAFITRI Â Nomor Rekening 0282566132'
D11 = 'Uangnya dikirim saja ke Rekening. BANK BNI atas nama : Saudara ABDUL RAHMAN Nomor Rek. : 024-8721- 191 SMS saja kalau sudah dikirim. terima kasih'
D12 = 'WASSALAMU ALAIKUM WR WB UANGNYA DIKIRIM SAJA KE NOMOR REKENING INI BRI ATAS NAMA NOVA ARYAxxx 0544 0100 8633 xxx KALAU SUDAH TRANSFER SMS SAJA DI NOMOR INI TERIMA KASIHâ€ Nomor. HP Pengirim SMS: 0821-5104-2542'
D13 = 'Ya Allah, semoga yang mempunyai hp ini & keluarganya selalu dalam Kasih SayangMu, diberkahi rejekinya & dijauhkan dari mara bahaya", jawab Amin jika Anda berkenan'
D14 = 'Yang Terhormat kepada bapak/ibu saya Eka Novitasari karyawan 3care sudah Menghubungi anda tidak tersambung dengan hormat hal ini kami sampaikan melalui sms singkat dari layanan kami bahwa selamat nomor anda Mendapatkan hadiah 1 unit mobil Toyota Avanza dengan PIN:47V27 dari undian rejeki 3care periode utama 2014.untuk info lebih lanjut kunjungi www.rejekiundian3care.jimdo.com'
D15 = 'sayang, isikan dulu pulsa di nomor as ini 085323048677 nanti gw gantiin.Penting banget nih karena barusan bos gw menelepon gw tungguin iya¦'
D16 = 'Yang Terhormat Bapak/Ibu. BNI menyatakan Rekening anda terpilih sebagai pemenang hadiah Rp. 35jt. kode cek anda 03299757 info klik www.bankbni2016.blogspot.com'
#2
D17 = '[PROMO] Beli paket Flash mulai 1GB di MY TELKOMSEL APP dapat EXTRA kuota 2GB 4G LTE dan EXTRA nelpon hingga 100menit/1hari. Buruan, cek  di tsel.me/mytsel1'
D18 = '2.5 GB/30 hari hanya Rp 35 Ribu Spesial buat Anda yang terpilih. Aktifkan sekarang juga di *550*905#. Promo sampai dengan 30 Nov 2015.Buruan aktifkan sekarang'
D19 = '4.5GB/30 hari hanya Rp 55 Ribu Spesial buat anda yang terpilih. Aktifkan sekarang juga di *550*907# Buruan..!'
D20 = '5 HARI LAGI ! EKSTRA Pulsa 50rb dengan beli paket internet bulanan di MyTelkomsel untuk pembelian pertama sejak 25Aug- 25Sept. Cek detail promo di tsel.me/mytsel1'
D21 = 'Ada iRing dengan tarif Rp. 0,1/7hari (perpanjangan Rp. 3190/7hari) dari hits Armada - Pencuri Hati. Tekan *808*3*1*4*1# lalu OK/Call. Info: 100&111'
D22 = 'Akhir bulan harus tetap eksis loh! Internetan pake volume ultima 900MB/30hari. Harga mulai Rp 35rb di *100*471#. Tarif&lokasi cek di tsel.me/fl' 
D23 = 'Aktifkan iRing Coboy Jr - Terhebat. Tekan *808*7#. Info: 100&111 Ada hits terbaru dari NOAH - Jika Engkau. Aktifkan iRing di HP kamu. Ketik MG NOAH02 kirim ke 808 Info: 100&111 Berkah iRing Rp 1000 dari Yuni'
D24 = 'Anda akan berhenti berlangganan Paket Flash. Ketik FLASH<spasi>YA jika setuju. Tunggu SMS konfirmasi penonaktifan Paket Anda'

list_biasa = [D1, D2, D3, D4, D5, D6, D7, D8]
i=0
stem_biasa = []
for stem_bias in list_biasa:
    
    stem_bias = stemmer.stem(list_biasa[i]) 
    stem_bias = ''.join([c for c in stem_bias if not c.isdigit()])
    stem_bias = re.sub(r'[^\w\s]','',stem_bias)
    stem_biasa.append(stem_bias)
    i+=1
#split_biasa
split_biasa=[]
i=0
for split_bias in stem_biasa:
    split_bias = (stem_biasa[i]).split()
    split_biasa.append(split_bias)
    i+=1
print  (split_biasa)

list_fraud = [D9, D10, D11, D12, D13, D14, D15, D16]
i=0
stem_fraud = []
for stem_fra in list_fraud:
    
    stem_fra = stemmer.stem(list_fraud[i]) 
    stem_fra = ''.join([c for c in stem_fra if not c.isdigit()])
    stem_fra = re.sub(r'[^\w\s]','',stem_fra)
    stem_fraud.append(stem_fra)
    i+=1

print ('')
# print  (stem_fraud)
split_fraud=[]
i=0
for split_fra in stem_fraud:
    split_fra = (stem_fraud[i]).split()
    split_fraud.append(split_fra)
    i+=1
print  (split_fraud)

list_promo = [D17, D18, D19, D20, D21, D22, D23, D24]
i=0
stem_promo = []
for stem_pro in list_promo:
    
#     list_promo[i] = ''.join([c for c in list_promo[i] if not c.isdigit()])
    stem_pro = stemmer.stem(list_promo[i])
    stem_pro = ''.join([c for c in stem_pro if not c.isdigit()])
    stem_pro = re.sub(r'[^\w\s]','',stem_pro)
    stem_promo.append(stem_pro)
    i+=1
print ('')

split_promo=[]
i=0
for split_pro in stem_promo:
    split_pro = (stem_promo[i]).split()
    split_promo.append(split_pro)
    i+=1
print  (split_promo)

stopword = ['ada', 'adalah', 'adanya', 'adapun', 'agak', 'agaknya', 'agar', 'akan', 'akankah', 'akhir', 'akhiri', 'akhirnya', 'aku', 'akulah', 'amat', 'amatlah', 'anda', 'andalah', 'antar', 'antara', 'antaranya', 'apa', 'apaan', 'apabila', 'apakah', 'apalagi', 'apatah', 'artinya', 'asal', 'asalkan', 'atas', 'atau', 'ataukah', 'ataupun', 'awal', 'awalnya', 'bagai', 'bagaikan', 'bagaimana', 'bagaimanakah', 'bagaimanapun', 'bagi', 'bagian', 'bahkan', 'bahwa', 'bahwasanya', 'baik', 'bakal', 'bakalan', 'balik', 'banyak', 'bapak', 'baru', 'bawah', 'beberapa', 'begini', 'beginian', 'beginikah', 'beginilah', 'begitu', 'begitukah', 'begitulah', 'begitupun', 'bekerja', 'belakang', 'belakangan', 'belum', 'belumlah', 'benar', 'benarkah', 'benarlah', 'berada', 'berakhir', 'berakhirlah', 'berakhirnya', 'berapa', 'berapakah', 'berapalah', 'berapapun', 'berarti', 'berawal', 'berbagai', 'berdatangan', 'beri', 'berikan', 'berikut', 'berikutnya', 'berjumlah', 'berkali-kali', 'berkata', 'berkehendak', 'berkeinginan', 'berkenaan', 'berlainan', 'berlalu', 'berlangsung', 'berlebihan', 'bermacam', 'bermacam-macam', 'bermaksud', 'bermula', 'bersama', 'bersama-sama', 'bersiap', 'bersiap-siap', 'bertanya', 'bertanya-tanya', 'berturut', 'berturut-turut', 'bertutur', 'berujar', 'berupa', 'besar', 'betul', 'betulkah', 'biasa', 'biasanya', 'bila', 'bilakah', 'bisa', 'bisakah', 'boleh', 'bolehkah', 'bolehlah', 'buat', 'bukan', 'bukankah', 'bukanlah', 'bukannya', 'bulan', 'bung', 'cara', 'caranya', 'cukup', 'cukupkah', 'cukuplah', 'cuma', 'dahulu', 'dalam', 'dan', 'dapat', 'dari', 'daripada', 'datang', 'dekat', 'demi', 'demikian', 'demikianlah', 'dengan', 'depan', 'di', 'dia', 'diakhiri', 'diakhirinya', 'dialah', 'diantara', 'diantaranya', 'diberi', 'diberikan', 'diberikannya', 'dibuat', 'dibuatnya', 'didapat', 'didatangkan', 'digunakan', 'diibaratkan', 'diibaratkannya', 'diingat', 'diingatkan', 'diinginkan', 'dijawab', 'dijelaskan', 'dijelaskannya', 'dikarenakan', 'dikatakan', 'dikatakannya', 'dikerjakan', 'diketahui', 'diketahuinya', 'dikira', 'dilakukan', 'dilalui', 'dilihat', 'dimaksud', 'dimaksudkan', 'dimaksudkannya', 'dimaksudnya', 'diminta', 'dimintai', 'dimisalkan', 'dimulai', 'dimulailah', 'dimulainya', 'dimungkinkan', 'dini', 'dipastikan', 'diperbuat', 'diperbuatnya', 'dipergunakan', 'diperkirakan', 'diperlihatkan', 'diperlukan', 'diperlukannya', 'dipersoalkan', 'dipertanyakan', 'dipunyai', 'diri', 'dirinya', 'disampaikan', 'disebut', 'disebutkan', 'disebutkannya', 'disini', 'disinilah', 'ditambahkan', 'ditandaskan', 'ditanya', 'ditanyai', 'ditanyakan', 'ditegaskan', 'ditujukan', 'ditunjuk', 'ditunjuki', 'ditunjukkan', 'ditunjukkannya', 'ditunjuknya', 'dituturkan', 'dituturkannya', 'diucapkan', 'diucapkannya', 'diungkapkan', 'dong', 'dua', 'dulu', 'empat', 'enggak', 'enggaknya', 'entah', 'entahlah', 'guna', 'gunakan', 'hal', 'hampir', 'hanya', 'hanyalah', 'hari', 'harus', 'haruslah', 'harusnya', 'hendak', 'hendaklah', 'hendaknya', 'hingga', 'ia', 'ialah', 'ibarat', 'ibaratkan', 'ibaratnya', 'ibu', 'ikut', 'ingat', 'ingat-ingat', 'ingin', 'inginkah', 'inginkan', 'ini', 'inikah', 'inilah', 'itu', 'itukah', 'itulah', 'jadi', 'jadilah', 'jadinya', 'jangan', 'jangankan', 'janganlah', 'jauh', 'jawab', 'jawaban', 'jawabnya', 'jelas', 'jelaskan', 'jelaslah', 'jelasnya', 'jika', 'jikalau', 'juga', 'jumlah', 'jumlahnya', 'justru', 'kala', 'kalau', 'kalauah', 'kalaupun', 'kalian', 'kami', 'kamilah', 'kamu', 'kamulah', 'kan', 'kapan', 'kapankah', 'kapanpun', 'karena', 'karenanya', 'kasus', 'kata', 'katakan', 'katakanlah', 'katanya', 'ke', 'keadaan', 'kebetulan', 'kecil', 'kedua', 'keduanya', 'keinginan', 'kelamaan', 'kelihatan', 'kelihatannya', 'kelima', 'keluar', 'kembali', 'kemudian', 'kemungkinan', 'kemungkinannya', 'kenapa', 'kepada', 'kepadanya', 'kesampaian', 'keseluruhan', 'keseluruhannya', 'keterlaluan', 'ketika', 'khususnya', 'kini', 'kinilah', 'kira', 'kira-kira', 'kiranya', 'kita', 'kitalah', 'kok', 'kurang', 'lagi', 'lagian', 'lah', 'lain', 'lainnya', 'lalu', 'lama', 'lamanya', 'lanjut', 'lanjutnya', 'lebih', 'lewat', 'lima', 'luar', 'macam', 'maka', 'makanya', 'makin', 'malah', 'malahan', 'mampu', 'mampukah', 'mana', 'manakala', 'manalagi', 'masa', 'masalah', 'masalahnya', 'masih', 'masihkah', 'masing', 'masing-masing', 'mau', 'maupun', 'melainkan', 'melakukan', 'melalui', 'melihat', 'melihatnya', 'memang', 'memastikan', 'memberi', 'memberikan', 'membuat', 'memerlukan', 'memihak', 'meminta', 'memintakan', 'memisalkan', 'memperbuat', 'mempergunakan', 'memperkirakan', 'memperlihatkan', 'mempersiapkan', 'mempersoalkan', 'mempertanyakan', 'mempunyai', 'memulai', 'memungkinkan', 'menaiki', 'menambahkan', 'menandaskan', 'menanti', 'menanti-nanti', 'menantikan', 'menanya', 'menanyai', 'menanyakan', 'mendapat', 'mendapatkan', 'mendatang', 'mendatangi', 'mendatangkan', 'menegaskan', 'mengakhiri', 'mengapa', 'mengatakan', 'mengatakannya', 'mengenai', 'mengerjakan', 'mengetahui', 'menggunakan', 'menghendaki', 'mengibaratkan', 'mengibaratkannya', 'mengingat', 'mengingatkan', 'menginginkan', 'mengira', 'mengucapkan', 'mengucapkannya', 'mengungkapkan', 'menjadi', 'menjawab', 'menjelaskan', 'menuju', 'menunjuk', 'menunjuki', 'menunjukkan', 'menunjuknya', 'menurut', 'menuturkan', 'menyampaikan', 'menyangkut', 'menyatakan', 'menyebutkan', 'menyeluruh', 'menyiapkan', 'merasa', 'mereka', 'merekalah', 'merupakan', 'meski', 'meskipun', 'meyakini', 'meyakinkan', 'minta', 'mirip', 'misal', 'misalkan', 'misalnya', 'mula', 'mulai', 'mulailah', 'mulanya', 'mungkin', 'mungkinkah', 'nah', 'naik', 'namun', 'nanti', 'nantinya', 'nyaris', 'nyatanya', 'oleh', 'olehnya', 'pada', 'padahal', 'padanya', 'pak', 'paling', 'panjang', 'pantas', 'para', 'pasti', 'pastilah', 'penting', 'pentingnya', 'per', 'percuma', 'perlu', 'perlukah', 'perlunya', 'pernah', 'persoalan', 'pertama', 'pertama-tama', 'pertanyaan', 'pertanyakan', 'pihak', 'pihaknya', 'pukul', 'pula', 'pun', 'punya', 'rasa', 'rasanya', 'rata', 'rupanya', 'saat', 'saatnya', 'saja', 'sajalah', 'saling', 'sama', 'sama-sama', 'sambil', 'sampai', 'sampai-sampai', 'sampaikan', 'sana', 'sangat', 'sangatlah', 'satu', 'saya', 'sayalah', 'se', 'sebab', 'sebabnya', 'sebagai', 'sebagaimana', 'sebagainya', 'sebagian', 'sebaik', 'sebaik-baiknya', 'sebaiknya', 'sebaliknya', 'sebanyak', 'sebegini', 'sebegitu', 'sebelum', 'sebelumnya', 'sebenarnya', 'seberapa', 'sebesar', 'sebetulnya', 'sebisanya', 'sebuah', 'sebut', 'sebutlah', 'sebutnya', 'secara', 'secukupnya', 'sedang', 'sedangkan', 'sedemikian', 'sedikit', 'sedikitnya', 'seenaknya', 'segala', 'segalanya', 'segera', 'seharusnya', 'sehingga', 'seingat', 'sejak', 'sejauh', 'sejenak', 'sejumlah', 'sekadar', 'sekadarnya', 'sekali', 'sekali-kali', 'sekalian', 'sekaligus', 'sekalipun', 'sekarang', 'sekarang', 'sekecil', 'seketika', 'sekiranya', 'sekitar', 'sekitarnya', 'sekurang-kurangnya', 'sekurangnya', 'sela', 'selain', 'selaku', 'selalu', 'selama', 'selama-lamanya', 'selamanya', 'selanjutnya', 'seluruh', 'seluruhnya', 'semacam', 'semakin', 'semampu', 'semampunya', 'semasa', 'semasih', 'semata', 'semata-mata', 'semaunya', 'sementara', 'semisal', 'semisalnya', 'sempat', 'semua', 'semuanya', 'semula', 'sendiri', 'sendirian', 'sendirinya', 'seolah', 'seolah-olah', 'seorang', 'sepanjang', 'sepantasnya', 'sepantasnyalah', 'seperlunya', 'seperti', 'sepertinya', 'sepihak', 'sering', 'seringnya', 'serta', 'serupa', 'sesaat', 'sesama', 'sesampai', 'sesegera', 'sesekali', 'seseorang', 'sesuatu', 'sesuatunya', 'sesudah', 'sesudahnya', 'setelah', 'setempat', 'setengah', 'seterusnya', 'setiap', 'setiba', 'setibanya', 'setidak-tidaknya', 'setidaknya', 'setinggi', 'seusai', 'sewaktu', 'siap', 'siapa', 'siapakah', 'siapapun', 'sini', 'sinilah', 'soal', 'soalnya', 'suatu', 'sudah', 'sudahkah', 'sudahlah', 'supaya', 'tadi', 'tadinya', 'tahu', 'tahun', 'tak', 'tambah', 'tambahnya', 'tampak', 'tampaknya', 'tandas', 'tandasnya', 'tanpa', 'tanya', 'tanyakan', 'tanyanya', 'tapi', 'tegas', 'tegasnya', 'telah', 'tempat', 'tengah', 'tentang', 'tentu', 'tentulah', 'tentunya', 'tepat', 'terakhir', 'terasa', 'terbanyak', 'terdahulu', 'terdapat', 'terdiri', 'terhadap', 'terhadapnya', 'teringat', 'teringat-ingat', 'terjadi', 'terjadilah', 'terjadinya', 'terkira', 'terlalu', 'terlebih', 'terlihat', 'termasuk', 'ternyata', 'tersampaikan', 'tersebut', 'tersebutlah', 'tertentu', 'tertuju', 'terus', 'terutama', 'tetap', 'tetapi', 'tiap', 'tiba', 'tiba-tiba', 'tidak', 'tidakkah', 'tidaklah', 'tiga', 'tinggi', 'toh', 'tunjuk', 'turut', 'tutur', 'tuturnya', 'ucap', 'ucapnya', 'ujar', 'ujarnya', 'umum', 'umumnya', 'ungkap', 'ungkapnya', 'untuk', 'usah', 'usai', 'waduh', 'wah', 'wahai', 'waktu', 'waktunya', 'walau', 'walaupun', 'wong', 'yaitu', 'yakin', 'yakni', 'yang']


# In[3]:

stop_biasa=[]
for i in range(len(split_biasa)):
            temp = []
            for j in range(len(split_biasa[i])):
                if split_biasa[i][j] not in stopword:
                    temp.append(split_biasa[i][j])
            stop_biasa.append(temp)

                                                       
print (stop_biasa)
print ('')

stop_fraud=[]
for i in range(len(split_fraud)):
            temp = []
            for j in range(len(split_fraud[i])):
                if split_fraud[i][j] not in stopword:
                    temp.append(split_fraud[i][j])
            stop_fraud.append(temp)
                            
                            
print (stop_fraud)
print ('')

stop_promo=[]
for i in range(len(split_promo)):
            temp = []
            for j in range(len(split_promo[i])):
                if split_promo[i][j] not in stopword:
                    temp.append(split_promo[i][j])
            stop_promo.append(temp)

                            
                            
print (stop_promo)                 


# In[4]:

count_biasa= {}
for sublist in stop_biasa:
    for item in sublist:
        if item not in count_biasa:
            count_biasa[item] = 1
        else:
            count_biasa[item] += 1
        
print(count_biasa)
print('')

count_fraud= {}
for sublist in stop_fraud:
    for item in sublist:
        if item not in count_fraud:
            count_fraud[item] = 1
        else:
            count_fraud[item] += 1
        
print(count_fraud)
print('')


count_promo= {}
for sublist in stop_promo:
    for item in sublist:
        if item not in count_promo:
            count_promo[item] = 1
        else:
            count_promo[item] += 1
        
print(count_promo)
# print('')


# In[5]:

count_all_value_biasa = 0
for i in count_biasa:
    count_all_value_biasa+=count_biasa[i]

print (count_all_value_biasa)

count_all_value_fraud = 0
for i in count_fraud:
    count_all_value_fraud+=count_fraud[i]

print (count_all_value_fraud)

count_all_value_promo = 0
for i in count_promo:
    count_all_value_promo+=count_promo[i]

print (count_all_value_promo)


# In[6]:

a=stop_biasa+stop_fraud+stop_promo
term_all= np.concatenate(a)
term_all= (list(set(term_all)))
count_term = len(term_all)
print(term_all)
print (count_term)


# In[7]:

array_biasa=[]
array_biasa= np.concatenate(stop_biasa)
nilai_term_biasa= {}
for sublist in term_all:
#     for item in sublist:
 
    if sublist in array_biasa:
        nilai_term_biasa[sublist] = (count_biasa[sublist])+1/count_all_value_biasa+count_term
#         nilai_term_biasa[sublist] = 0+1/count_all_value_biasa+count_term
    else:
        nilai_term_biasa[sublist] = 0+1/count_all_value_biasa+count_term
#         nilai_term_biasa[sublist] = (count_biasa[sublist])+1/count_all_value_biasa+count_term
            
        
print(nilai_term_biasa)
# nilai_term_biasa

array_fraud= np.concatenate(stop_fraud)
nilai_term_fraud= {}
for sublist in term_all:
    if sublist in array_fraud:
        nilai_term_fraud[sublist] = (count_fraud[sublist])+1/count_all_value_fraud+count_term
    else:
        nilai_term_fraud[sublist] = 0+1/count_all_value_fraud+count_term
            
print ('')        
print(nilai_term_fraud)

array_promo= np.concatenate(stop_promo)
nilai_term_promo= {}
for sublist in term_all:
    if sublist in array_promo:
        nilai_term_promo[sublist] = (count_promo[sublist])+1/count_all_value_promo+count_term
    else:
        nilai_term_promo[sublist] = 0+1/count_all_value_promo+count_term
            
print ('')        
print(nilai_term_promo)


# In[14]:

D_uji = 'nama1 dimana ? boleh minta tolong ss dong bisnis proses nya,,,,,'
kata_uji = stemmer.stem(D_uji)
kata_uji = ''.join([c for c in kata_uji if not c.isdigit()])
split_uji = kata_uji.split();
stop_uji= []
for i in split_uji:
    if i not in stopword:     
        stop_uji.append(i)                
# print(stop_uji)
nilai_uji_promo= 1/3
for sublist in stop_uji:
    if sublist in nilai_term_promo:
        nilai_uji_promo= nilai_uji_promo*(nilai_term_promo[sublist])
#     else:
#         nilai_uji_promo[sublist] = 0+1/count_all_value_promo+count_term

print (nilai_uji_promo)


# In[ ]:



