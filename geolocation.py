import requests
from typing import Dict, Optional

def get_ip_based_location(ip_address: str = None) -> Dict[str, Optional[str]]:
    """
    Fetch approximate location based on IP address using ipapi.co.
    Returns: {city, country, latitude, longitude}
    """
    try:
        url = f"https://ipapi.co/{ip_address}/json/" if ip_address else "https://ipapi.co/json/"
        response = requests.get(url, timeout=5).json()
        
        return {
            "city": response.get("city"),
            "country": response.get("country_name"),
            "latitude": response.get("latitude"),
            "longitude": response.get("longitude"),
            "ip": response.get("ip"),
        }
    except Exception as e:
        return {"error": str(e)}