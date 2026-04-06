def interpret_budget(budget_output: dict, days: int) -> dict:
    activity_total = budget_output["total"]["activities"]
    stay_total = budget_output["total"]["stay"]

    activity_per_day = activity_total / days
    stay_per_day = stay_total / days

    #for activity
    if activity_per_day < 1000:
        activity_level = "low"
    elif activity_per_day < 3000:
        activity_level = "medium"
    else:
        activity_level = "high"

    #for stay
    if stay_per_day < 1500:
        stay_type = "budget"
    elif stay_per_day < 4000:
        stay_type = "midrange"
    else:
        stay_type = "luxury"

    return {
        "activity_budget_per_day": int(activity_per_day),
        "activity_budget_level": activity_level,
        "stay_budget_per_day": int(stay_per_day),
        "stay_type": stay_type
    }