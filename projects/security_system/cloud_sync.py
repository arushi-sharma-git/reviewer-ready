import random

def fetch_blacklisted_keys():
    """
    Simulates fetching a list of compromised keys from a remote server.
    In a real app, you'd use the 'requests' library here.
    """
    # Simulated remote database of leaked keys
    leaked_keys = ["Z1234567", "X9999999", "B1111111"]
    
    # Simulate a network "glitch" (10% chance)
    if random.random() < 0.1:
        return None, "Connection Timeout"
    
    return leaked_keys, "Success"