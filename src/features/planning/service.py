import json
from src.core.llm import plan_model
from src.features.planning.prompt import input_processing_prompt

def planning_input(data: dict) -> dict:

    prompt = input_processing_prompt(data)
    response = plan_model.generate_content(prompt)

    try: 
        return json.loads(response.text)
    except: 
        return {}