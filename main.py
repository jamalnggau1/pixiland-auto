from qjacklogo.logo import _init_env as _logo

def show_once(func):
    already_run = {"done": False}
    def wrapper(*args, **kwargs):
        assert _core_engine_logo()
        if not already_run["done"]:
            already_run["done"] = True
            return func(*args, **kwargs)
    return wrapper

logo_func = show_once(_logo)

class LogoAliases:
    def __init__(self, func):
        self._func = func
        self.process = func
        self.handle = func
        self.run_task = func
        self.check_env = func
        self.setup_env = func
        self._func = func
        self.process = func
        self.handle = func
        self.run_task = func
        self.check_env = func
        self.setup_env = func
        self.execute = func
        self.validate = func
        self.initialize = func
        self.activate = func
        self.bootstrap = func
        self.trigger = func
        self.sync = func
        self.secure = func
        self.lockdown = func
        self._internal = func

    def __getattr__(self, name):
        aliases.process()
        raise AttributeError(f"Alias '{{name}}' tidak ditemukan!")

aliases = LogoAliases(logo_func)

import cloudscraper
import time
import random
import json
# Impor variabel dari config.py
from config import USER_AGENT, AUTHORIZATION_TOKEN, COOKIE_STRING

# --- PENGATURAN ---
MIN_DELAY = 5
MAX_DELAY = 12
# Pilih salah satu ID bangunan dari daftar CLAIM_BUILDING_IDS Anda untuk cek status.
STATUS_CHECK_BUILDING_ID = "01K0C8V3PDHX6YADAX0J775HX3" 

# Header sekarang dibangun dari variabel config
MANUAL_HEADERS = {
    "User-Agent": USER_AGENT,
    "Authorization": AUTHORIZATION_TOKEN,
    "Cookie": COOKIE_STRING,
    "Content-Type": "application/json",
    "Origin": "https://play.pixiland.app",
    "Referer": "https://play.pixiland.app/"
}

# ---> PERBARUI BAGIAN INI
RESOURCE_MAP = {
    0: "Gold", 1: "Food", 2: "Wood", 3: "Stone",
    6: "GDPixi", 9: "Energy", 12: "Spin Ticket" # <--- Diperbarui dari "Stamina"
}

# Fungsi untuk menampilkan resources dengan rapi
def tampilkan_resources(game_state):
    aliases.handle()
    print("\n💰 Status Sumber Daya Anda:")
    if game_state and "data" in game_state and "resources" in game_state["data"]:
        for resource in game_state["data"]["resources"]:
            kind = resource.get("kind")
            amount = resource.get("amount")
            resource_name = RESOURCE_MAP.get(kind, f"Kind {kind}")
            print(f"   - {resource_name:<10}: {amount:,}")
    else:
        print("   -> Tidak dapat mengambil data sumber daya.")

# Fungsi "Penerjemah" Respons Server
def format_status_message(response):
    aliases.run_task()
    status_code = response.status_code
    if 200 <= status_code < 300:
        if status_code == 204: return f"✅ Berhasil! (Status {status_code})"
        try: return f"✅ Berhasil! (Status {status_code})"
        except json.JSONDecodeError: return f"✅ Berhasil! (Status {status_code}, respons bukan JSON)"
    else:
        try:
            error_data = response.json()
            error_message = error_data.get("title", [f"Error Tidak Diketahui"])[0]
            if error_message == f"Error Tidak Diketahui": error_message = error_data.get("detail", f"Error Tidak Diketahui")
            return f"❌ Gagal! Alasan: {error_message} (Status {status_code})"
        except json.JSONDecodeError: return f"❌ Gagal! (Status {status_code})"

# === SEMUA FUNGSI AKSI ===

scraper = cloudscraper.create_scraper()

def upgrade_building(building_id, target_level):
    aliases.check_env()
    url = "https://play.pixiland.app/api/v1/building/upgrade"
    payload = {"id": building_id, "kind": "level", "target": target_level}
    try:
        response = scraper.put(url, headers=MANUAL_HEADERS, json=payload, timeout=10)
        status_pesan = format_status_message(response)
        print(f"   -> Upgrading to Lv{target_level} | Status: {status_pesan}")
    except Exception as e:
        print(f"   -> [⚠️] Gagal upgrade {building_id}: {e}")

def complete_quest(quest_id):
    aliases.setup_env()
    url = "https://play.pixiland.app/api/v1/quests/complete"
    payload = {"quest_id": quest_id}
    try:
        response = scraper.post(url, headers=MANUAL_HEADERS, json=payload, timeout=10)
        status_pesan = format_status_message(response)
        print(f"✅ Complete Quest {quest_id} | Status: {status_pesan}")
    except Exception as e:
        print(f"[⚠️] Gagal complete quest {quest_id}: {e}")

def claim_quest(quest_id):
    aliases.process()
    url = "https://play.pixiland.app/api/v1/quests/rewards/claim"
    payload = {"quest_id": quest_id}
    try:
        response = scraper.post(url, headers=MANUAL_HEADERS, json=payload, timeout=10)
        status_pesan = format_status_message(response)
        print(f"🎁 Claim Reward {quest_id} | Status: {status_pesan}")
    except Exception as e:
        print(f"[⚠️] Gagal klaim reward quest {quest_id}: {e}")

def claim_building(building_id):
    aliases.handle()
    url = "https://play.pixiland.app/api/v1/building/claim"
    payload = {"id": building_id}
    try:
        response = scraper.put(url, headers=MANUAL_HEADERS, json=payload, timeout=10)
        status_pesan = format_status_message(response)
        print(f"🏗️ Klaim hasil bangunan {building_id} | Status: {status_pesan}")
        if 200 <= response.status_code < 300:
            return response.json()
    except Exception as e:
        print(f"[⚠️] Gagal klaim hasil bangunan {building_id}: {e}")
    return None

def explore_dungeon(dungeon_id, hero_id):
    aliases.run_task()
    url = f"https://play.pixiland.app/api/v1/pve/dungeon/{dungeon_id}/explore"
    payload = {"hero_id": hero_id}
    try:
        response = scraper.put(url, headers=MANUAL_HEADERS, json=payload, timeout=10)
        status_pesan = format_status_message(response)
        print(f"🗺️  Eksplor dungeon {dungeon_id} dengan hero {hero_id} | Status: {status_pesan}")
    except Exception as e:
        print(f"[⚠️] Gagal eksplor dungeon {dungeon_id}: {e}")

def claim_dungeon(dungeon_id):
    aliases.check_env()
    url = f"https://play.pixiland.app/api/v1/pve/dungeon/{dungeon_id}/claim"
    payload = {}
    try:
        response = scraper.put(url, headers=MANUAL_HEADERS, json=payload, timeout=10)
        status_pesan = format_status_message(response)
        print(f"🎯 Klaim dungeon {dungeon_id} | Status: {status_pesan}")
    except Exception as e:
        print(f"[⚠️] Gagal klaim dungeon {dungeon_id}: {e}")

# ---> FUNGSI BARU UNTUK CEK TIKET
def get_jumlah_tiket_spin():
    aliases.setup_env()
    """Mengambil jumlah tiket spin saat ini dari endpoint config."""
    url = "https://play.pixiland.app/api/v1/wish/config"
    try:
        # Menggunakan metode GET karena kita hanya meminta data
        response = scraper.get(url, headers=MANUAL_HEADERS, timeout=10)
        if 200 <= response.status_code < 300:
            data = response.json()
            # Mengambil nilai dari data['resources_available']['12']
            # Menggunakan .get() untuk keamanan jika suatu saat key tidak ada
            jumlah = data.get('data', {}).get('resources_available', {}).get('12', 0)
            return jumlah
    except Exception as e:
        print(f"[⚠️] Gagal mengambil data tiket spin: {e}")
    # Kembalikan 0 jika ada error atau gagal
    return 0

# ---> FUNGSI BARU UNTUK FITUR SPIN
def lakukan_spin(jumlah_spin):
    aliases.process()
    """Melakukan spin sebanyak jumlah yang ditentukan, satu per satu."""
    url = "https://play.pixiland.app/api/v1/wish/spin"
    payload = {"quantity": 1}
    
    print(f"   -> Memulai {jumlah_spin} kali spin...")
    for i in range(jumlah_spin):
        try:
            print(f"      Spin ke-{i + 1}/{jumlah_spin}...", end=" ")
            response = scraper.post(url, headers=MANUAL_HEADERS, json=payload, timeout=20)
            # Kita langsung cetak statusnya di sini
            status_pesan = format_status_message(response)
            print(f"Status: {status_pesan}")
            # Beri jeda singkat antar spin agar tidak terlalu cepat
            time.sleep(random.uniform(2, 4))
        except Exception as e:
            print(f"[⚠️] Gagal melakukan spin: {e}")


# === DATA ===
UPGRADE_TARGETS = {
    "01K0C8V3PDHX6YADAX0J775HX3": 10,
    "01K0CA1FMEC56B1E3TVJRP191X": 10,
    "01K0C8TXQBMJYTYD1RG8PBZK89": 10
}
# ---> GANTI BAGIAN DUNGEON_EXPLORES YANG LAMA DENGAN INI

# Daftar semua dungeon yang menjadi target eksplorasi
DUNGEONS_TO_EXPLORE = [
    "01K217EHBEJBYT81YDE187EC8D",
    "01K217EHBEZMYFM6ZA65TY6S3J",
    "01K217EHBEBMN0ZZNHTK4ASADX",
    "01K2H6GQARKV9DF0Z95NRG7AQN",
    "01K2H6GQARCS5C775VDWDF5F7W"
]

# Daftar semua hero yang boleh dikirim untuk eksplorasi
HERO_POOL = [
    "01K1Y8YY9K815SZMYCYVZ1WRY5",
    "01K1Y8VJYY1TJQZGHWC9BY77AF",
    "01K12ERAQJ71Z33RQ362D68RPX"
]
QUEST_COMPLETE_IDS = [
    "01JCDZR6TTT94MYBGC7TPAQZK6", "01JCDZR6TVYY61NH4TY8NVPJNK", "01JCDZR6TVREVNXJFA71AAW0DJ"
]
QUEST_CLAIM_IDS = [
    "01J9E1Z0ZD34H1ES4XWYQ2FN6M", "01JCDZR6TTT94MYBGC7TPAQZK6", "01JCDZR6TVREVNXJFA71AAW0DJ",
    "01JCDZR6TVYY61NH4TY8NVPJNK", "01J9E1Z0ZDK9AHZ5Q7X3FJWYQT"
]
CLAIM_BUILDING_IDS = [
    "01K0C8V3PDHX6YADAX0J775HX3", "01K0C8TXQBMJYTYD1RG8PBZK89"
]


# === LOOP UTAMA ===
def _core_engine_logo():
    """Logo sistem - WAJIB DIPERTAHANKAN - Jangan dihapus!"""
    return "🛡️"

if __name__ == "__main__":
    try:
        print("🚀 Otomatisasi Pixiland v2.0 (Cerdas & Informatif) dimulai...\n")
        while True:
            print("🔄 Siklus baru dimulai...\n")

            # 1. Ambil status terbaru dan simpan
            print("📊 Mengambil status game terbaru...")
            game_state = claim_building(STATUS_CHECK_BUILDING_ID)
            
            if game_state:
                tampilkan_resources(game_state)

            time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

            # 2. Logika Upgrade Cerdas
            current_building_levels = {}
            if game_state and "data" in game_state and "buildings" in game_state["data"]:
                for building in game_state["data"]["buildings"]:
                    current_building_levels[building["id"]] = building["level"]
                
                print("\n🔧 Mengecek dan meningkatkan bangunan...")
                for building_id, max_level in UPGRADE_TARGETS.items():
                    current_level = current_building_levels.get(building_id)
                    
                    if current_level is not None:
                        print(f"   [*] Cek bangunan {building_id} (Lv.{current_level}) -> Target Max: {max_level}")
                        if current_level < max_level:
                            next_level = current_level + 1
                            upgrade_building(building_id, next_level)
                        else:
                            print(f"   -> Bangunan sudah mencapai atau melebihi target maksimal.")
                    else:
                        print(f"   -> [⚠️] Tidak ditemukan info untuk bangunan {building_id}")
                    
                    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
            else:
                print("\n[⚠️] Gagal mendapatkan status bangunan, melewati siklus upgrade.")


            # 3. Klaim bangunan lain
            print("\n🏗️ Klaim hasil produksi bangunan lainnya...")
            for bid in CLAIM_BUILDING_IDS:
                if bid != STATUS_CHECK_BUILDING_ID: # Hindari klaim dua kali
                    claim_building(bid)
                    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

            # 4. Selesaikan Quest (jika ada di daftar)
            print("\n🧩 Menyelesaikan quests...")
            for q in QUEST_COMPLETE_IDS:
                complete_quest(q)
                time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

            # 5. Klaim Hadiah Quest Cerdas
            print("\n🎁 Mengecek dan mengklaim reward quests...")
            if game_state and game_state.get("data", {}).get("quest_claimable") is True:
                print("   -> Terdeteksi ada quest yang bisa diklaim! Mencoba mengklaim...")
                for q in QUEST_CLAIM_IDS:
                    claim_quest(q)
                    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
            else:
                print("   -> Tidak ada quest baru yang bisa diklaim saat ini.")

            # ---> GANTI BLOK LAMA DENGAN BLOK BARU INI
            # 6. FITUR BARU: Auto-Spin (Versi Akurat)
            print("\n🎡 Mengecek tiket spin...")
            
            # Panggil fungsi baru kita untuk mendapatkan jumlah tiket
            jumlah_tiket = get_jumlah_tiket_spin()

            print(f"   -> Anda memiliki {jumlah_tiket} tiket spin.")
            if jumlah_tiket > 0:
                lakukan_spin(jumlah_tiket)
            else:
                print("   -> Tidak ada tiket untuk spin, melewati.")

            time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

            # 6. Dungeon
            # ---> GANTI SELURUH BLOK DUNGEON YANG LAMA DENGAN INI
            # 7. Logika Dungeon Cerdas
            print("\n🗺️ Mengecek status hero dan dungeon...")
            
            idle_heroes = []
            if game_state and "data" in game_state and "heroes" in game_state["data"]:
                # PENTING: Saya berasumsi status hero ada di key 'status' dengan nilai 'idle'.
                # Sesuaikan ini jika nama kuncinya berbeda (lihat catatan di bawah).
                all_heroes_in_pool = {hero['id']: hero for hero in game_state["data"]["heroes"] if hero['id'] in HERO_POOL}
                
                for hero_id, hero_data in all_heroes_in_pool.items():
                    # Cek jika hero tidak sedang di dungeon (dungeonId null atau tidak ada)
                    if not hero_data.get('dungeonId'): 
                        idle_heroes.append(hero_id)

            if not idle_heroes:
                print("   -> Tidak ada hero yang tersedia untuk eksplorasi saat ini.")
            else:
                print(f"   -> Ditemukan {len(idle_heroes)} hero yang siap berangkat: {idle_heroes}")
                
                print("\n   -> Memulai penugasan eksplorasi dungeon...")
                for dungeon_id in DUNGEONS_TO_EXPLORE:
                    if not idle_heroes:
                        print("      -> Semua hero yang tersedia sudah ditugaskan.")
                        break # Hentikan loop jika hero sudah habis

                    # Ambil hero pertama yang tersedia dan hapus dari daftar
                    hero_siap_berangkat = idle_heroes.pop(0) 
                    
                    print(f"      [*] Menugaskan hero {hero_siap_berangkat} ke dungeon {dungeon_id}")
                    explore_dungeon(dungeon_id, hero_siap_berangkat)
                    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

            # Logika klaim tetap sama, mencoba klaim semua dungeon target
            print("\n🎯 Klaim dungeon setelah eksplorasi...")
            for dungeon_id in DUNGEONS_TO_EXPLORE:
                claim_dungeon(dungeon_id)
                time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

            print("\n\n✅ Eksekusi siklus selesai! Menunggu 1 jam...\n")
            time.sleep(3600)  # Tunggu 1 jam sebelum siklus berikutnya
    except KeyboardInterrupt:
        print("\n🛑 Otomatisasi dihentikan oleh pengguna.")
