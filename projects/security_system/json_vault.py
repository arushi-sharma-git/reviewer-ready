import json
import os
from datetime import datetime

VAULT_PATH = "projects/security_system/vault.json"

def load_vault():
    """Safely loads the JSON database."""
    if not os.path.exists(VAULT_PATH):
        return []
    try:
        with open(VAULT_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
       
        print(" Warning: Vault file corrupted. Starting fresh.")
        return []

def save_entry(key, status):
    """Adds a new record to the JSON database."""
   
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "key": key,
        "status": status,
        "flagged": "❌" in status 
    }

   
    current_data = load_vault()
    
   
    current_data.append(entry)
    
    with open(VAULT_PATH, "w") as f:
        json.dump(current_data, f, indent=4)
    print(f"✅ Record for {key} synced to Vault.")

def main():
    print("--- 🔐 JSON VAULT SYSTEM ---")
    test_key = input("Enter key to log: ")
   
    save_entry(test_key, "✅ Access Granted")
    
    
    data = load_vault()
    print(f"Total records in vault: {len(data)}")

if __name__ == "__main__":
    main()