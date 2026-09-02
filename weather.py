from pathlib import Path
import requests
from flask import Flask, render_template, jsonify, request
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATE_DIR = BASE_DIR / "templates"

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)

# Weather code to emoji mapping (WMO Weather Codes)
WEATHER_EMOJI_MAP = {
    0: ("☀️", "Clear sky"),
    1: ("🌤️", "Mainly clear"),
    2: ("🌤️", "Partly cloudy"),
    3: ("☁️", "Overcast"),
    45: ("🌫️", "Foggy"),
    48: ("🌫️", "Depositing rime fog"),
    51: ("🌧️", "Light drizzle"),
    53: ("🌧️", "Moderate drizzle"),
    55: ("🌧️", "Dense drizzle"),
    61: ("🌧️", "Slight rain"),
    63: ("🌧️", "Moderate rain"),
    65: ("🌧️", "Heavy rain"),
    71: ("❄️", "Slight snow"),
    73: ("❄️", "Moderate snow"),
    75: ("❄️", "Heavy snow"),
    77: ("❄️", "Snow grains"),
    80: ("🌧️", "Slight rain showers"),
    81: ("🌧️", "Moderate rain showers"),
    82: ("🌧️", "Violent rain showers"),
    85: ("❄️", "Slight snow showers"),
    86: ("❄️", "Heavy snow showers"),
    95: ("⛈️", "Thunderstorm"),
    96: ("⛈️", "Thunderstorm with slight hail"),
    99: ("⛈️", "Thunderstorm with heavy hail"),
}


@app.route("/")
def index():
    """Serve the main weather app page."""
    return render_template("weather.html")


@app.route("/api/weather", methods=["POST"])
def get_weather():
    """
    Fetch weather data for a given city.
    
    Request JSON: {"city": "New York"}
    Response JSON: {
        "city": "New York",
        "temperature": 72,
        "condition": "Clear sky",
        "icon": "☀️",
        "timestamp": "2026-09-02T14:30:00"
    }
    Error Response: {"error": "City not found"}
    """
    try:
        data = request.get_json()
        city = data.get("city", "").strip()
        
        if not city:
            return jsonify({"error": "Please enter a city name"}), 400
        
        # Step 1: Geocode the city name to get latitude and longitude
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        geocoding_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }
        
        geocoding_response = requests.get(geocoding_url, params=geocoding_params, timeout=5)
        geocoding_response.raise_for_status()
        geocoding_data = geocoding_response.json()
        
        if not geocoding_data.get("results"):
            return jsonify({"error": f"City '{city}' not found"}), 400
        
        location = geocoding_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location.get("name", city)
        country = location.get("country", "")
        display_name = f"{city_name}, {country}" if country else city_name
        
        # Step 2: Fetch weather data using the coordinates
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,weather_code",
            "temperature_unit": "celsius"
        }
        
        weather_response = requests.get(weather_url, params=weather_params, timeout=5)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        current = weather_data.get("current", {})
        temperature = current.get("temperature_2m")
        weather_code = current.get("weather_code")
        
        if temperature is None or weather_code is None:
            return jsonify({"error": "Unable to fetch weather data"}), 500
        
        # Step 3: Map weather code to emoji and description
        emoji, condition = WEATHER_EMOJI_MAP.get(weather_code, ("❓", "Unknown"))
        
        # Step 4: Return formatted response
        return jsonify({
            "city": display_name,
            "temperature": round(temperature, 1),
            "condition": condition,
            "icon": emoji,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out. Please try again."}), 503
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch weather data. Please try again."}), 503
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
