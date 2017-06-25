
## Issue #1: s2s ignores model location specified on config file

	$ head valid.bpe.en | ./s2s-93856ed -c model.en2id.npz.s2s.yml 
	npz_load: Error! Unable to open file model.npz!
	Aborted (core dumped)




## Issue #2: s2s needs a warm up? 

Note the first sentence.


	$ head valid.bpe.en | ./s2s-93856ed -m model.en2id.npz.best-cross-entropy.npz -v vocab.en.json vocab.id.json 2>/dev/null | detruecase.py 
	Begbegbegbahnya , begbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbegbeg￭
	Dan kami pergi ke parenting mengharapkan kehidupan kita untuk melihat ini.
	Asal Italia digantikan oleh pelatih asal Portugal di Inter Milan pada tahun 2008.
	Saya memenangkan Kontes World Yoo lagi dalam divisi kinerja artistik.
	Dan di Irak, akhirnya, kekerasan sedang meningkat lagi, dan negara tersebut belum membentuk pemerintah empat bulan setelah pemilihan parlemen terakhir.
	Di dekat masa depan, dealer mobil baru akan dibuka di sini.
	Saya tidak ingin belajar operasi.
	Sejumlah konten, sebuah acara, menyebabkan seseorang untuk berbicara.
	"Seorang wanita iman," "seorang ahli," mungkin "seorang pembeli"?
	Semakin, kita menggunakan perangkat mobile, dan kami berinteraksi di jalan.


Second run, produced correct sentence.


	$ head valid.bpe.en | ./s2s-93856ed -m model.en2id.npz.best-cross-entropy.npz -v vocab.en.json vocab.id.json 2>/dev/null | detruecase.py 
	Dan seperti itu keluar, saya melakukan pekerjaan yang sangat baik.
	Dan kami pergi ke parenting yang mengharapkan kehidupan kita untuk terlihat seperti ini.
	Asal Italia digantikan oleh pelatih asal Portugal di Inter Milan pada tahun 2008.
	Saya memenangkan Kontes World Yoo lagi dalam divisi performa artistik.
	Dan di Irak, akhirnya, kekerasan berada di kenaikan lagi, dan negara tersebut belum membentuk pemerintah empat bulan setelah pemilihan parlemen terakhir.
	Di dekat masa depan, dealer mobil baru akan dibuka di sini.
	Saya tidak ingin mempelajari operasi.
	Sejumlah konten, sebuah acara, menyebabkan seseorang untuk berbicara.
	"Seorang wanita iman," "seorang ahli," mungkin "seorang pembeli"?
	Semakin, kita menggunakan perangkat mobile, dan kami berinteraksi di jalan.
