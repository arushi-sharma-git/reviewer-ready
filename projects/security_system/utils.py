import re

def sanitize_input(user_input):
    """Clean the input: remove spaces and make uppercase."""
    return user_input.strip().upper()

def is_key_safe(key):
    """
    Advanced Validation:
    1. Must be exactly 8 chars.
    2. Must be Alphanumeric (no @, !, #).
    """
    if len(key) != 8:
        return False, "Error: Key must be exactly 8 characters."
    
    if not key.isalnum():
        return False, "Error: Key contains prohibited symbols."
        
    return True, "Safe"