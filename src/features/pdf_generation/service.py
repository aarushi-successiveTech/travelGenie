from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(data, processing, budget, itinerary, filename="trip_plan.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    content = []

    # adding title
    content.append(Paragraph(f"{data['destination']} Travel Plan", styles["Title"]))
    content.append(Spacer(1, 10))
    #days and travel type
    content.append(Paragraph(f"Duration: {data['days']} days", styles["Normal"]))
    content.append(Paragraph(f"Travel Type: {data['travel_type']}", styles["Normal"]))
    content.append(Spacer(1, 20))

    #adding overview
    content.append(Paragraph("Trip Overview", styles["Heading2"]))
    content.append(Paragraph(processing.get("destination_overview", ""), styles["BodyText"]))
    content.append(Spacer(1, 15))

    #travel style 
    content.append(Paragraph("Travel Strategy", styles["Heading2"]))
    tp = processing.get("travel_pattern", {})
    content.append(Paragraph(f"Style: {tp.get('exploration_style', '')}", styles["BodyText"]))
    content.append(Paragraph(f"Transport: {tp.get('primary_transport', '')}", styles["BodyText"]))
    content.append(Spacer(1, 10))

    #destination area split
    content.append(Paragraph("Area Plan", styles["Heading3"]))
    for area in tp.get("area_split", []):
        content.append(Paragraph(f"{area['area']} - {area['recommended_days']} days", styles["BodyText"]))
    content.append(Spacer(1, 15))

    #budget split in table
    content.append(Paragraph("Budget Breakdown", styles["Heading2"]))

    budget_data = [["Category", "Amount (₹)"]]
    for key, value in budget.get("total", {}).items():
        budget_data.append([key.capitalize(), str(value)])

    table = Table(budget_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ]))
    content.append(table)
    content.append(Spacer(1, 20))

    #display day-wise itinerary
    content.append(Paragraph("Day-wise Itinerary", styles["Heading2"]))

    for day in itinerary.get("days", []):
        content.append(Spacer(1, 10))
        content.append(Paragraph(f"Day {day['day']} - {day['area']}", styles["Heading3"]))

        for activity in day.get("activities", []):
            text = f"""
            <b>{activity['time'].capitalize()}: {activity['name']}</b><br/>
            Type: {activity['type']}<br/>
            Duration: {activity['duration_hours']} hrs<br/>
            Estimated Cost: ₹{activity.get('estimated_cost', 0)}<br/>
            {activity.get('description', '')}"""
            content.append(Paragraph(text, styles["BodyText"]))
    content.append(Spacer(1, 20))

    #display key attractions
    content.append(Paragraph("Top Attractions", styles["Heading2"]))
    for place in processing.get("key_attractions", [])[:6]:
        content.append(Paragraph(f"- {place['name']} ({place['type']})", styles["BodyText"]))
    content.append(Spacer(1, 15))

    #ai reasoning 
    content.append(Paragraph("Why this Itinerary will be good for your trip?", styles["Heading2"]))
    reasoning = itinerary.get("reasoning", "No reasoning available")
    content.append(Paragraph(reasoning, styles["BodyText"]))
    content.append(Spacer(1, 15))

    #extra info 
    content.append(Paragraph("Travel Tips", styles["Heading2"]))
    for tip in processing.get("seasonal_tips", []):
        content.append(Paragraph(f"- {tip}", styles["BodyText"]))
    content.append(Spacer(1, 20))

    doc.build(content)
    return filename