def validate_key(key):
    """Checks a single key and returns (is_valid, message)."""
    try:
        if len(key) != 8:
            return False, "Invalid Length"
        
        if not key[0].isalpha() or not key[-1].isdigit():
            return False, "Format Error (Alpha-Digit)"
        
        if "z" in key.lower():
            return False, "Contains 'z'"
        
       
        num1 = int(key[3])
        num2 = int(key[4])
        if (num1 + num2) < 10:
            return False, f"Sum too low ({num1+num2})"
        
        return True, "Success"

    except (ValueError, IndexError):
        return False, "Data Type/Index Error"

def main():
    test_keys = ["A1299BC9", "Z1234567", "A1211BC9", "B9988XY2", "ABC12EF3"]
    authorized = []
    rejected = []

    print("--- 🛡️ Starting Security Scan ---")

    for key in test_keys:
        is_valid, reason = validate_key(key)
        if is_valid:
            authorized.append(key)
            print(f"✅ {key} | Passed")
        else:
            rejected.append(f"{key} ({reason})")
            print(f"❌ {key} | Rejected: {reason}")

    print(f"\nScan Summary: {len(authorized)} Allowed, {len(rejected)} Rejected.")

if __name__ == "__main__":
    main()