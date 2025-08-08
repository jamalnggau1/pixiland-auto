import requests
import time
from config import AUTHORIZATION, DELAY

# === DATA ===

DUNGEON_EXPLORES = [
    {
        "dungeon_id": "01K217EHBEJBYT81YDE187EC8D",  # bisa diganti
        "hero_id": "01K1Y8YY9K815SZMYCYVZ1WRY5"      # bisa diganti
    },
    {
        "dungeon_id": "01K217EHBEZMYFM6ZA65TY6S3J",   # contoh tambahan
        "hero_id": "01K1Y8VJYY1TJQZGHWC9BY77AF"
    }
    # Tambahkan lebih banyak kalau perlu...
]


UPGRADE_BUILDINGS = [
    {"id": "01K0C8V3PDHX6YADAX0J775HX3", "target": 4},
    {"id": "01K0CA1FMEC56B1E3TVJRP191X", "target": 2}
]

QUEST_COMPLETE_IDS = [
    "01JCDZR6TTT94MYBGC7TPAQZK6",
    "01JCDZR6TVYY61NH4TY8NVPJNK",
    "01JCDZR6TVREVNXJFA71AAW0DJ"
    
]

QUEST_CLAIM_IDS = [
    "01J9E1Z0ZD34H1ES4XWYQ2FN6M",
    "01JCDZR6TTT94MYBGC7TPAQZK6",
    "01JCDZR6TVREVNXJFA71AAW0DJ",
    "01JCDZR6TVYY61NH4TY8NVPJNK",
    "01J9E1Z0ZDK9AHZ5Q7X3FJWYQT"
    
]

CLAIM_BUILDING_IDS = [
    "01K0C8V3PDHX6YADAX0J775HX3",
    "01K0C8TXQBMJYTYD1RG8PBZK89"
]

HEADERS = {
    "Authorization": AUTHORIZATION,
    "Content-Type": "application/json",
    "Origin": "https://play.pixiland.app",
    "Referer": "https://play.pixiland.app/"
}

# === FUNGSI ===

def upgrade_building(building_id, target_level):
    url = "https://play.pixiland.app/api/v1/building/upgrade"
    payload = {"id": building_id, "kind": "level", "target": target_level}
    try:
        response = requests.put(url, headers=HEADERS, json=payload, timeout=10)
        print(f"🔧 Upgrade {building_id} -> Lv{target_level} | Status: {response.status_code}")
    except Exception as e:
        print(f"[⚠️] Gagal upgrade {building_id}: {e}")


def complete_quest(quest_id):
    url = "https://play.pixiland.app/api/v1/quests/complete"
    payload = {"quest_id": quest_id}
    try:
        response = requests.post(url, headers=HEADERS, json=payload, timeout=10)
        print(f"✅ Complete Quest {quest_id} | Status: {response.status_code}")
    except Exception as e:
        print(f"[⚠️] Gagal complete quest {quest_id}: {e}")


def claim_quest(quest_id):
    url = "https://play.pixiland.app/api/v1/quests/rewards/claim"
    payload = {"quest_id": quest_id}
    try:
        response = requests.post(url, headers=HEADERS, json=payload, timeout=10)
        print(f"🎁 Claim Reward {quest_id} | Status: {response.status_code}")
    except Exception as e:
        print(f"[⚠️] Gagal klaim reward quest {quest_id}: {e}")


def claim_building(building_id):
    url = "https://play.pixiland.app/api/v1/building/claim"
    payload = {"id": building_id}
    try:
        response = requests.put(url, headers=HEADERS, json=payload, timeout=10)
        print(f"🏗️ Klaim hasil bangunan {building_id} | Status: {response.status_code}")
    except Exception as e:
        print(f"[⚠️] Gagal klaim hasil bangunan {building_id}: {e}")


def explore_dungeon(dungeon_id, hero_id):
    url = f"https://play.pixiland.app/api/v1/pve/dungeon/{dungeon_id}/explore"
    payload = {"hero_id": hero_id}
    try:
        response = requests.put(url, headers=HEADERS, json=payload, timeout=10)
        print(f"🗺️  Eksplor dungeon {dungeon_id} dengan hero {hero_id} | Status: {response.status_code}")
    except Exception as e:
        print(f"[⚠️] Gagal eksplor dungeon {dungeon_id}: {e}")

def claim_dungeon(dungeon_id):
    url = f"https://play.pixiland.app/api/v1/pve/dungeon/{dungeon_id}/claim"
    payload = {}
    try:
        response = requests.put(url, headers=HEADERS, json=payload, timeout=10)
        print(f"🎯 Klaim dungeon {dungeon_id} | Status: {response.status_code}")
    except Exception as e:
        print(f"[⚠️] Gagal klaim dungeon {dungeon_id}: {e}")



# === LOOP UTAMA ===

if __name__ == "__main__":
    try:
        print("🚀 Otomatisasi Pixiland dimulai...\n")

        while True:
            print("🔄 Eksekusi baru...\n")

            # Upgrade bangunan
            for b in UPGRADE_BUILDINGS:
                upgrade_building(b["id"], b["target"])
                time.sleep(DELAY)

            # Selesaikan quest
            print("\n🧩 Menyelesaikan quests...")
            for q in QUEST_COMPLETE_IDS:
                complete_quest(q)
                time.sleep(DELAY)

            # Klaim reward quest
            print("\n🎁 Mengklaim reward quests...")
            for q in QUEST_CLAIM_IDS:
                claim_quest(q)
                time.sleep(DELAY)

            # Klaim hasil bangunan
            print("\n🏗️ Klaim hasil produksi bangunan...")
            for bid in CLAIM_BUILDING_IDS:
                claim_building(bid)
                time.sleep(DELAY)

            print("\n🗺️ Menjalankan eksplorasi dungeon...")
            for entry in DUNGEON_EXPLORES:
                explore_dungeon(entry["dungeon_id"], entry["hero_id"])
                time.sleep(DELAY)  # pakai delay agar tidak terlalu cepat

            print("\n🎯 Klaim dungeon setelah eksplorasi...")
            for entry in DUNGEON_EXPLORES:
                claim_dungeon(entry["dungeon_id"])
                time.sleep(DELAY)


            print("\n✅ Eksekusi selesai! Menunggu 1 jam...\n")
            time.sleep(3600)
    except KeyboardInterrupt:
        print("\n🛑 Otomatisasi dihentikan oleh pengguna.")
