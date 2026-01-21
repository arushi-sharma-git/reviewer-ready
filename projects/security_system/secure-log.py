
STATUS_MESSAGES = {
    "VALID": " Access Granted",
    "ERR_LEN": " Rejected: Wrong Length",
    "ERR_Z": "Rejected: Contains 'z'",
    "ERR_MATH": " Rejected: Math Sum Failed"
}


def check_key(key):
    if len(key) != 8:
        return STATUS_MESSAGES["ERR_LEN"]
    
    if "z" in key.lower():
        return STATUS_MESSAGES["ERR_Z"]
    

    try:
        if int(key[3]) + int(key[4]) < 10:
            return STATUS_MESSAGES["ERR_MATH"]
    except ValueError:
        return " Rejected: Not a Number"

    return STATUS_MESSAGES["VALID"]


def save_to_file(key, result):
  
    with open("projects/security_system/access_logs.txt", "a") as file:
        file.write(f"Key: {key} | Result: {result}\n")


def main():
    keys_to_process = ["A1299BC9", "Z1234567", "B1211BC9"]
    
    print("---  Processing Keys and Logging to File ---")
    
    for k in keys_to_process:
        status = check_key(k)
        print(f"Checking {k}: {status}")
        
        
        save_to_file(k, status)

if __name__ == "__main__":
    main()