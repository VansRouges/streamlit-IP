import requests
from typing import Dict, Optional

def get_ip_based_location(ip_address: str = None) -> Dict[str, Optional[str]]:
    """
    Fetch approximate location based on IP address using ipapi.co.
    Returns: {city, country, latitude, longitude}
    """
    try:
        url = f"http://ip-api.com/json/{ip_address}" if ip_address else "http://ip-api.com/json/"
        response = requests.get(url, timeout=5).json()
        
        return {
            "city": response.get("city"),
            "country": response.get("country"),
            "latitude": response.get("lat"),
            "longitude": response.get("lon"),
            "ip": response.get("query"),
        }
    except Exception as e:
        return {"error": str(e)}