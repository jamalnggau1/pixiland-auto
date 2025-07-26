import requests
import time
from config import AUTHORIZATION, DELAY

# === DATA ===

UPGRADE_BUILDINGS = [
    {"id": "01K0C8V3PDHX6YADAX0J775HX3", "target": 4},
    {"id": "01K0CA1FMEC56B1E3TVJRP191X", "target": 2}
]

QUEST_COMPLETE_IDS = [
    "01JCDZR6TTT94MYBGC7TPAQZK6",
    "01JCDZR6TVYY61NH4TY8NVPJNK",
    "01JCDZR6TVREVNXJFA71AAW0DJ",
    "01J9E1Z0ZDK9AHZ5Q7X3FJWYQT",
    "01J9E1Z0ZDYVS3XV2FMFX4J7B7",
    "01JN5CXM890ZX5TH7P5DMRVMN4",
    "01JPKSY05RQEZ759XJHH65T08G",
    "01JVM13RD2FZB17C9BG8K3JZVZ",
    "01K12PHTSZ8YCH3Y1EHXWY42EN",
    "01JKSZV8VV9Q2BN7QCX495TMT3",
    "01JN0EMTCTER2KSSDCZZBSYXVS",
    "01K106M4FF5S1WJSXFBXVZDBDT",
    "01JZZPHDCMYYHR19Y8BRYXKEEE",
    "01JZM3QMY9GKNXXNHXH5CFQ852",
    "01JNQZG472JS455KNGFSGC0DP9",
    "01JTMG9HDDXQM1J5361QW1A4K7",
    "01JTMGB0KVRVZQDV7NV2N6WS8K",
    "01JV9W1K1GZJ0HTCV8344AB6JG",
    "01JVS1NAS2FHXGHRCCAT9C2FM9",
    "01JVS1Q6H1DFYAZFTWJRPBGDJX",
    "01JWWJ5S3SS2CDWZKXEAXFW5WV",
    "01JWZEA92YRS4JJBHWR5ZTKVRP",
    "01JX1V14376TNVW3EPS2AX7Z5A",
    "01JX4ZFF77Z28GJC5K7ZAHY3NY",
    "01JXBZK5BKP9M9Z6YGD3SCKDE2",
    "01JXHM68894VZBPDXZEGCJG4W7",
    "01JXHM7JCXZF6M3NWWV0RE2AZB",
    "01JYFY4MZEHGHQKN65H1AH505D",
    "01JYGKRZWJJF29ZJBAQPWE4VR7",
    "01JYK61Q8CCFJQ7DWHDGV2DWWR"
    
]

QUEST_CLAIM_IDS = [
    "01J9E1Z0ZD34H1ES4XWYQ2FN6M",
    "01JCDZR6TTT94MYBGC7TPAQZK6",
    "01JCDZR6TVREVNXJFA71AAW0DJ",
    "01JCDZR6TVYY61NH4TY8NVPJNK",
    "01J9E1Z0ZDK9AHZ5Q7X3FJWYQT",
    "01J9E1Z0ZDYVS3XV2FMFX4J7B7",
    "01JN5CXM890ZX5TH7P5DMRVMN4",
    "01JPKSY05RQEZ759XJHH65T08G",
    "01JVM13RD2FZB17C9BG8K3JZVZ",
    "01K12PHTSZ8YCH3Y1EHXWY42EN",
    "01JKSZV8VV9Q2BN7QCX495TMT3",
    "01JN0EMTCTER2KSSDCZZBSYXVS",
    "01K106M4FF5S1WJSXFBXVZDBDT",
    "01JZZPHDCMYYHR19Y8BRYXKEEE",
    "01JZM3QMY9GKNXXNHXH5CFQ852",
    "01JNQZG472JS455KNGFSGC0DP9",
    "01JTMG9HDDXQM1J5361QW1A4K7",
    "01JTMGB0KVRVZQDV7NV2N6WS8K",
    "01JV9W1K1GZJ0HTCV8344AB6JG",
    "01JVS1NAS2FHXGHRCCAT9C2FM9",
    "01JVS1Q6H1DFYAZFTWJRPBGDJX",
    "01JWWJ5S3SS2CDWZKXEAXFW5WV",
    "01JWZEA92YRS4JJBHWR5ZTKVRP",
    "01JX1V14376TNVW3EPS2AX7Z5A",
    "01JX4ZFF77Z28GJC5K7ZAHY3NY",
    "01JXBZK5BKP9M9Z6YGD3SCKDE2",
    "01JXHM68894VZBPDXZEGCJG4W7",
    "01JXHM7JCXZF6M3NWWV0RE2AZB",
    "01JYFY4MZEHGHQKN65H1AH505D",
    "01JYGKRZWJJF29ZJBAQPWE4VR7",
    "01JYK61Q8CCFJQ7DWHDGV2DWWR"
    
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
    response = requests.put(url, headers=HEADERS, json=payload)
    print(f"🔧 Upgrade {building_id} -> Lv{target_level} | Status: {response.status_code}")

def complete_quest(quest_id):
    url = "https://play.pixiland.app/api/v1/quests/complete"
    payload = {"quest_id": quest_id}
    response = requests.post(url, headers=HEADERS, json=payload)
    print(f"✅ Complete Quest {quest_id} | Status: {response.status_code}")

def claim_quest(quest_id):
    url = "https://play.pixiland.app/api/v1/quests/rewards/claim"
    payload = {"quest_id": quest_id}
    response = requests.post(url, headers=HEADERS, json=payload)
    print(f"🎁 Claim Reward {quest_id} | Status: {response.status_code}")

def claim_building(building_id):
    url = "https://play.pixiland.app/api/v1/building/claim"
    payload = {"id": building_id}
    response = requests.put(url, headers=HEADERS, json=payload)
    print(f"🏗️ Klaim hasil bangunan {building_id} | Status: {response.status_code}")

# === LOOP UTAMA ===

if __name__ == "__main__":
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

        print("\n✅ Eksekusi selesai! Menunggu 1 jam...\n")
        time.sleep(3600)
