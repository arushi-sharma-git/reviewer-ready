import json
import os

VAULT_PATH = "projects/security_system/vault.json"

def run_audit():
    if not os.path.exists(VAULT_PATH):
        print("❌ No vault found to audit.")
        return

    with open(VAULT_PATH, "r") as f:
        data = json.load(f)

    
    threats = [item for item in data if item.get("flagged") == True]

    print("--- 🛡️ QUICK SECURITY AUDIT ---")
    print(f"Total Records Scanned: {len(data)}")
    print(f"Threats Detected: {len(threats)}")
    
    if threats:
        print("\nListing Critical Threats:")
        for t in threats:
            print(f"⚠️  {t['timestamp']} | Key: {t['key']}")
    else:
        print("\n✅ System Clean: No flagged threats found.")

if __name__ == "__main__":
    run_audit()