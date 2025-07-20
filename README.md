# 🤖 Pixiland Automation Bot

Bot otomatis untuk menjalankan tugas-tugas harian di game [Pixiland](https://play.pixiland.app), seperti:

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

1. Pastikan Python 3.x sudah terpasang.
2. Install dependency:

```bash
pip install requests

## ⚙️ Konfigurasi

## ⚙️ Konfigurasi

Nilai konfigurasi diatur melalui file `config.py`. Buat file ini di direktori yang sama dengan script utama, lalu isi seperti berikut:

```python
# config.py
AUTHORIZATION = "Bearer TOKEN_KAMU"
DELAY = 2  # Jeda antar request dalam detik

---

## 📝 Catatan

- Gunakan script ini secara bijak dan **jangan disalahgunakan** agar tidak terkena banned.
- Token `Authorization` bisa berubah jika kamu logout/login. Pastikan selalu diperbarui jika script berhenti bekerja.
- Semua ID (`building_id`, `quest_id`, dll.) bisa didapat dari inspeksi jaringan (HAR file) saat kamu bermain manual di browser.

---

## 📄 Lisensi

Proyek ini dibuat **hanya untuk keperluan edukasi dan otomatisasi pribadi**.  
Tidak berafiliasi dengan pihak resmi **Pixiland** dalam bentuk apapun.
