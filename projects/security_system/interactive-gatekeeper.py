


import os


STATUS_MESSAGES = {
    "VALID": "✅ Access Granted",
    "ERR_LEN": "❌ Rejected: Wrong Length (Must be 8)",
    "ERR_Z": "❌ Rejected: Prohibited Character 'z'",
    "ERR_MATH": "❌ Rejected: Math Sum Rule Failed",
    "ERR_TYPE": "❌ Rejected: Non-numeric at index 3/4"
}

LOG_FILE = "projects/security_system/access_logs.txt"

def check_key(key):
    """Business Logic: Validates the key against all security rules."""
    if len(key) != 8:
        return STATUS_MESSAGES["ERR_LEN"]
    
    if "z" in key.lower():
        return STATUS_MESSAGES["ERR_Z"]
    
    try:
       
        num1 = int(key[3])
        num2 = int(key[4])
        if (num1 + num2) < 10:
            return STATUS_MESSAGES["ERR_MATH"]
    except (ValueError, IndexError):
        return STATUS_MESSAGES["ERR_TYPE"]

    return STATUS_MESSAGES["VALID"]

def save_to_log(key, result):
    """File I/O: Appends the result to the log file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"Key: {key} | Result: {result}\n")

def view_logs():
    """File I/O: Reads and displays the log file."""
    if not os.path.exists(LOG_FILE):
        print("\n⚠️ No logs found yet. Try validating a key first!\n")
        return

    print("\n--- 📜 HISTORICAL ACCESS LOGS ---")
    with open(LOG_FILE, "r") as f:
        print(f.read())
    print("---------------------------------\n")

def main():
    """Main Menu Loop: The 'Engine' of our application."""
    while True:
        print("--- 🛡️ GATEKEEPER INTERACTIVE SYSTEM ---")
        print("1. Validate New Security Key")
        print("2. View All System Logs")
        print("3. Clear Logs")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            user_key = input("Enter key to scan: ")
            status = check_key(user_key)
            print(f"\nScanning... {status}\n")
            save_to_log(user_key, status)

        elif choice == "2":
            view_logs()

        elif choice == "3":
            
            open(LOG_FILE, 'w').close()
            print("\n🧹 Logs cleared successfully!\n")

        elif choice == "4":
            print("Shutting down... Stay secure!")
            break
        else:
            print("\n⚠️ Invalid input. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()