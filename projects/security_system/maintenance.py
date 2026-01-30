import os
from config import VAULT_FILE

def reset_vault():
    confirm = input("⚠️ Are you sure you want to delete all logs? (y/n): ")
    if confirm.lower() == 'y':
        if os.path.exists(VAULT_FILE):
            os.remove(VAULT_FILE)
            print("✅ Vault cleared successfully.")
        else:
            print("ℹ️ Vault file does not exist.")
    else:
        print("❌ Action cancelled.")

if __name__ == "__main__":
    reset_vault()