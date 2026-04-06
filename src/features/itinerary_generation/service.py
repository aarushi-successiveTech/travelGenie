import json
from src.core.llm import plan_model
from src.features.itinerary_generation.prompt import itinerary_prompt

def generate_itinerary(data, processing, budget_context): 

    prompt = itinerary_prompt(data, processing, budget_context)
    response = plan_model.generate_content(prompt)

    try: 
        return json.loads(response.text)
    except:
        return {}