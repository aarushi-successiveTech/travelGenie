def allocate_budget(data: dict, processing: dict) -> dict:
    total = data["budget"]
    days = data["days"]
    travel_type = data["travel_type"]
    cost_category = processing.get("cost_category", "moderate").lower()

    allocation = {
        "stay": 0.4,
        "food": 0.2,
        "transport": 0.2,
        "activities": 0.15,
        "buffer": 0.05
    }

    # Travel Type Adjustments
    if travel_type == "solo":
        allocation["stay"] -= 0.05
        allocation["activities"] += 0.05

    elif travel_type == "friends":
        allocation["stay"] -= 0.08
        allocation["activities"] += 0.05
        allocation["food"] += 0.03

    elif travel_type == "family":
        allocation["stay"] += 0.1
        allocation["transport"] += 0.05
        allocation["activities"] -= 0.05

    # Cost Category Adjustments
    if cost_category == "budget-friendly":
        allocation["stay"] -= 0.05
        allocation["activities"] += 0.05

    elif cost_category == "expensive":
        allocation["stay"] += 0.07
        allocation["food"] += 0.03
        allocation["activities"] -= 0.05

    elif cost_category == "luxury":
        allocation["stay"] += 0.1
        allocation["food"] += 0.05
        allocation["buffer"] += 0.03
        allocation["activities"] -= 0.08

    total_percent = sum(allocation.values())
    allocation = {k: v / total_percent for k, v in allocation.items()}
    total_budget_split = {k: v * total for k, v in allocation.items()}

    fixed_costs = {
        "transport": total_budget_split["transport"]
    }

    variable_costs = {
        "stay": total_budget_split["stay"],
        "food": total_budget_split["food"],
        "activities": total_budget_split["activities"]
    }

    # Per day allocation 
    per_day = {}

    stay_per_day = variable_costs["stay"] / days
    food_per_day = variable_costs["food"] / days
    activities_per_day = variable_costs["activities"] / days

    for day in range(1, days + 1):
        per_day[f"day_{day}"] = {
            "stay": int(stay_per_day),
            "food": int(food_per_day),
            "activities": int(activities_per_day)
        }

    return {
        "total": {k: int(v) for k, v in total_budget_split.items()},
        "per_day": per_day,
        "fixed_costs": {k: int(v) for k, v in fixed_costs.items()}
    }