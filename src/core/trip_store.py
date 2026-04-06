import uuid

trip_store={}
def generate_tripId(): 
    return str(uuid.uuid4())