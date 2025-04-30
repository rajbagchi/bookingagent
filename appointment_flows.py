APPOINTMENT_FLOWS = [
    {"topic": "zoning_tree", "reconfirmation_prompt": "Is this a zoning or tree code question?", "follow_up_questions": ["What is the address?"]},
    # ... add more as needed
]

def get_appointment_flow(topic):
    for flow in APPOINTMENT_FLOWS:
        if flow["topic"] == topic:
            return flow
    return None
