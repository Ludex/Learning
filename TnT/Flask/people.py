from datetime import datetime
from os import abort

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },

    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },

    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people request
def read_all():
    '''
    This function responds to a request for /api/people with the complete list of people
    '''
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    '''
    This function responds to a request for /api/people/{lname} with one person matching from people
    '''

    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    else:
        abort(404, f"Person with last name {lname} not found")

    return person