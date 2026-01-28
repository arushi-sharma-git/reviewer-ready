import re

def sanitize_input(user_input):
    return user_input.strip().upper()

def is_key_safe(key):
   
    pattern = r"^[A-Z][A-Z0-9]{7}$"
    
    if re.match(pattern, key):
        return True, "Safe"
    else:
        
        return False, "Pattern Mismatch: Invalid format or length"