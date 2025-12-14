import requests
import pandas as pd
from datetime import datetime, timedelta

# Keep your OpenWeatherMap API key for future use if needed
API_KEY = "ef590fd9b760fb13698597b3744a1526"

def get_weather_data(city, start_date=None, end_date=None):
    """
    Fetch historical weather data for a city using Open-Meteo API.
    This API provides historical weather data, unlike OpenWeatherMap's forecast API.
    
    Args:
        city: City name (Bengaluru, Mumbai, Delhi, Chennai)
        start_date: Start date for weather data (datetime.date or string YYYY-MM-DD)
        end_date: End date for weather data (datetime.date or string YYYY-MM-DD)
    
    Returns:
        DataFrame with columns: date, temp, rain
    """
    # City coordinates
    city_coords = {
        "Bengaluru": {"lat": 12.9716, "lon": 77.5946},
        "Mumbai": {"lat": 19.0760, "lon": 72.8777},
        "Delhi": {"lat": 28.7041, "lon": 77.1025},
        "Chennai": {"lat": 13.0827, "lon": 80.2707}
    }
    
    if city not in city_coords:
        print(f"Error: City '{city}' not found")
        return None
    
    lat = city_coords[city]["lat"]
    lon = city_coords[city]["lon"]
    
    # Default to last 30 days if no dates provided
    if end_date is None:
        end_date = datetime.now().date()
    if start_date is None:
        start_date = end_date - timedelta(days=30)
    
    # Convert to string format YYYY-MM-DD
    if isinstance(start_date, datetime):
        start_date = start_date.date()
    if isinstance(end_date, datetime):
        end_date = end_date.date()
    
    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")
    
    # Open-Meteo historical weather API
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}&"
        f"start_date={start_str}&end_date={end_str}&"
        f"daily=temperature_2m_mean,precipitation_sum&"
        f"timezone=auto"
    )
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Error: API request failed with status code {response.status_code}")
            print(f"Response: {response.text}")
            return None
        
        data = response.json()
        
        if "daily" not in data:
            print(f"Error: 'daily' key not found in response")
            return None
        
        # Create DataFrame
        df = pd.DataFrame({
            "date": data["daily"]["time"],
            "temp": data["daily"]["temperature_2m_mean"],
            "rain": [1 if p > 0 else 0 for p in data["daily"]["precipitation_sum"]]
        })
        
        return df
    
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed - {e}")
        return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    # Test the function
    from datetime import date
    
    print("Testing weather data fetch...")
    
    # Test with specific date range
    start = date(2025, 1, 1)
    end = date(2025, 1, 31)
    
    city = "Bengaluru"
    print(f"\nFetching weather for {city} from {start} to {end}")
    
    weather_df = get_weather_data(city, start, end)
    
    if weather_df is not None:
        print("\nSuccess! Here's the data:")
        print(weather_df.head(10))
        print(f"\nTotal days: {len(weather_df)}")
        print(f"Temperature range: {weather_df['temp'].min():.1f}°C to {weather_df['temp'].max():.1f}°C")
        print(f"Rainy days: {weather_df['rain'].sum()}")
    else:
        print("\nFailed to fetch weather data")