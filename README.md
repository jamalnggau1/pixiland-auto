# 🤖 Pixiland Automation Bot

Bot otomatis untuk menjalankan tugas-tugas harian di game https://play.pixiland.app, seperti:

- 🔧 Upgrade bangunan  
- ✅ Selesaikan quest  
- 🎁 Klaim hadiah quest  
- 🏗️ Klaim hasil produksi dari bangunan  
- 🔄 Berjalan otomatis setiap 1 jam  

---

## 🧠 Cara Kerja

Script ini akan berjalan terus-menerus dalam loop. Setiap 1 jam, bot akan:

1. Meng-upgrade bangunan ke level tertentu.
2. Menyelesaikan beberapa quest.
3. Mengklaim reward dari quest yang telah diselesaikan.
4. Mengklaim hasil produksi dari bangunan tertentu.

---

## 🛠️ Instalasi

1. Pastikan Python 3.x sudah terpasang di perangkatmu.
2. Install dependency yang diperlukan:
   pip install requests

3. Buat file bernama config.py di direktori yang sama dengan script utama, lalu isi seperti ini:

   # config.py  
   AUTHORIZATION = "Bearer TOKEN_KAMU"  
   DELAY = 2  # Jeda antar request dalam detik

4. Jalankan script:
   python main.py

---

## ⚙️ Konfigurasi

Nilai-nilai berikut diatur melalui file config.py:

- AUTHORIZATION  
  Token otentikasi milikmu dari Pixiland. Diperlukan agar semua permintaan API valid.

- DELAY  
  Delay antar request (dalam detik) untuk mencegah spam dan menghindari pemblokiran IP atau akun.

Sedangkan di dalam script utama (main.py), kamu bisa mengatur:

- UPGRADE_BUILDINGS  
  List ID bangunan yang ingin di-upgrade dan level targetnya.

- QUEST_COMPLETE_IDS  
  Daftar ID quest yang ingin diselesaikan.

- QUEST_CLAIM_IDS  
  Daftar ID quest yang ingin diklaim hadiahnya.

- CLAIM_BUILDING_IDS  
  Daftar ID bangunan yang hasil produksinya ingin diklaim setiap jam.

---

## 📝 Catatan

- Gunakan script ini secara bijak dan jangan disalahgunakan agar tidak terkena banned.
- Token Authorization bisa berubah jika logout/login, jadi pastikan selalu diperbarui jika script berhenti bekerja.
- Semua ID (building_id, quest_id, dll.) bisa didapat dari inspeksi jaringan (HAR) saat kamu bermain manual di browser.

---

## 📄 Lisensi

Proyek ini dibuat hanya untuk keperluan edukasi dan otomatisasi pribadi.  
Tidak berafiliasi dengan pihak resmi Pixiland dalam bentuk apapun.
