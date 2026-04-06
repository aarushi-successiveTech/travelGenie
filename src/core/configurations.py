import os

class Settings: 
    travel_genie_key = os.getenv("API_KEY")
    airbnb_url = os.getenv("AIRBNB_URL")

settings = Settings()