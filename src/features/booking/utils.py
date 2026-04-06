def normalize_stay(stay_data): 
    normalised = []

    for item in stay_data: 
        try: 
            normalised.append({
                "name": item.get("name"),
                "type": item.get("type", "stay"),
                "price_per_night": item.get("price", {}).get("rate", 0),
                "location": item.get("city", ""),
                "rating": item.get("rating", 0),
                "amenities": item.get("amenities", []),
                "ideal_for": ["solo", "friends", "family"] 
            })

        except: 
            continue
    
    return normalised