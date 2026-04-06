import google.generativeai as genai
from src.core.configurations import settings
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=settings.travel_genie_key)

plan_model = genai.GenerativeModel("gemini-2.5-flash-lite")

itinerary_model = genai.GenerativeModel("gemini-2.5-pro", generation_config={"temperature": 0.2})