import json
import os
from datetime import datetime
from cloud_sync import fetch_blacklisted_keys

# Import our custom modules
from config import VAULT_FILE, ADMIN_SECRET
from utils import sanitize_input, is_key_safe

def load_vault():
    """Safely loads the JSON database using path from config."""
    if not os.path.exists(VAULT_FILE):
        return []
    try:
        with open(VAULT_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_entry(key, status):
    """Adds a new record to the JSON database."""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "key": key,
        "status": status,
        "flagged": "❌" in status or "Fail" in status
    }

    current_data = load_vault()
    current_data.append(entry)
    
    with open(VAULT_FILE, "w") as f:
        json.dump(current_data, f, indent=4)

def search_vault(query):
    """Searches records for a specific key or status."""
    data = load_vault()
    results = [item for item in data if query.lower() in item['key'].lower()]
    
    if results:
        print(f"\n🔍 Matches found: {len(results)}")
        for r in results:
            print(f"- {r['timestamp']} | {r['key']} | {r['status']}")
    else:
        print("\n❌ No records match that search.")

def main():
    print(f"--- 🔐 GATEKEEPER SYSTEM (Admin: {ADMIN_SECRET[0:4]}***) ---")
    
    while True:
        print("\n1. Log New Key")
        print("2. Search Vault")
        print("3. Exit")
        
        choice = input("\nSelect Option: ")
        
        if choice == "1":
            raw_key = input("Enter Key: ")
            clean_key = sanitize_input(raw_key)
            is_valid, msg = is_key_safe(clean_key)
            
            # --- NEW CLOUD CHECK ---
            blacklisted, cloud_msg = fetch_blacklisted_keys()
            if blacklisted and clean_key in blacklisted:
                is_valid = False
                msg = "🚨 SECURITY ALERT: Key found in Cloud Blacklist!"
            # -----------------------

            if is_valid:
                save_entry(clean_key, "✅ Access Granted")
            else:
                print(f"⚠️ {msg}")

        elif choice == "2":
            q = input("Search for key: ")
            search_vault(q)

        elif choice == "3":
            print("Shutting down...")
            break

if __name__ == "__main__":
    main()