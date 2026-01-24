import json
import os
from datetime import datetime
from utils import sanitize_input, is_key_safe

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

def search_vault(query):
    """Searches the JSON vault for a specific key or status."""
    data = load_vault()
   
    results = [item for item in data if query.lower() in item['key'].lower() or query.lower() in item['status'].lower()]
    
    if results:
        print(f"\n🔍 Found {len(results)} matches for '{query}':")
        for r in results:
            print(f"- {r['timestamp']} | {r['key']} | {r['status']}")
    else:
        print(f"\n❌ No matches found for '{query}'.")


def generate_report():
    """Calculates and displays security statistics."""
    data = load_vault()
    if not data:
        return
    
    total = len(data)
   
    passed = sum(1 for item in data if not item['flagged'])
    failed = total - passed
    
    print("\n---  SECURITY ANALYTICS REPORT ---")
    print(f"Total Scans: {total}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    print(f"Flagged Threats: {failed}")
    print("------------------------------------\n")

def main():
    while True:
        print("\n---  ADVANCED JSON VAULT ---")
        print("1. Log New Key")
        print("2. Search Records") 
        print("3. View Analytics")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
         raw_key = input("Enter Key: ")
         clean_key = sanitize_input(raw_key) 
    
         is_valid, message = is_key_safe(clean_key) 
    
         if is_valid:
          save_entry(clean_key, "✅ Access Granted")
         else:
             print(f"⚠️ {message}")
            
            
        elif choice == "2": 
            q = input("Enter search term (key or status): ")
            search_vault(q) 
        elif choice == "3":
            generate_report()
            
        elif choice == "4":
            print("Goodbye!")
            break
    else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()