from datetime import datetime
from os import abort

from flask import make_response

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
        return PEOPLE.get(lname)

    else:
        abort(404, f"Person with last name {lname} not found")

def create(person):
    '''
    This function creates a new person in the people structure based on the passed-in person's data
    '''
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname, 
            "timestamp": get_timestamp()
        }

        return make_response(
            f"{lname} created successfully", 201
        )

    else:
        abort(
            406, f"Person with last name {lname} already exists"
        )

def update(lname, person):
    '''
    This function updates an existing person in the people structure
    '''
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return make_response(
            f"{lname} updated successfully", 200
        )

    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

def delete(lname):
    '''
    This function updates an existing person in the people structure
    '''
    if lname in PEOPLE:
        del(PEOPLE[lname])

        return make_response(
            f"{lname} deleted successfully", 200
        )

    else:
        abort(
            404, f"Person with last name {lname} not found"
        )
