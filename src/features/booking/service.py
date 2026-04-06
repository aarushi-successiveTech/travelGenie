from src.core.trip_store import generate_tripId

def filter_stays(stays, budget_context, processing, data):
    max_price = budget_context["stay_budget_per_day"]
    preferred_location = processing["travel_type_adjustments"]["location_preference"]
    travel_type = data["travel_type"]

    filtered = []

    for stay in stays:
        if stay["price_per_night"] <= max_price:
            if travel_type in stay["ideal_for"]:
                filtered.append(stay)

    return filtered

def score_stay(stay, processing, data):
    score = 0
    score += stay["rating"] * 2

    if data["travel_type"] in stay["ideal_for"]:
        score += 3
    pref_loc = processing["travel_type_adjustments"]["location_preference"]
    if pref_loc == "central":
        score += 2 
    elif pref_loc in stay["location"].lower():
        score += 3

    if "wifi" in stay["amenities"]:
        score += 1

    return score

def select_best_stay(stays, processing, data):
    scored = []

    for stay in stays:
        s = score_stay(stay, processing, data)
        scored.append((stay, s))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[0][0] if scored else None

def generate_booking_reason(stay, data, budget_context):
    return f"""
    Selected {stay['name']} because:
    - Fits your ₹{budget_context['stay_budget_per_day']} per day budget
    - Ideal for {data['travel_type']} travelers
    - Located in {stay['location']} which matches your travel pattern
    - Has strong rating of {stay['rating']}
    """

def simulate_booking(stay, days):
    total_cost = stay["price_per_night"] * days

    return {
        "stay_name": stay["name"],
        "price_per_night": stay["price_per_night"],
        "total_cost": total_cost,
        "status": "Reserved (Simulation)",
        "booking_id": generate_tripId()
    }