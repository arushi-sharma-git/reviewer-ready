import requests

def get_network_info():
    """Fetches the user's public IP using a real API."""
    try:
        # We use a 3-second timeout so the program doesn't hang if internet is slow
        response = requests.get("https://api.ipify.org?format=json", timeout=3)
        if response.status_code == 200:
            return response.json().get("ip"), "Success"
        return "Unknown", "API Error"
    except requests.RequestException:
        return "Offline", "Connection Failed"