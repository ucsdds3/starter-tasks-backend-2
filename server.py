# Imports
from flask import Flask, request
from json import load, dump

# Init Flask app
app = Flask(__name__)


# HTTP route handler
@app.route('/', methods=['GET', 'POST', 'DELETE'])
def main():
    if request.method == 'GET':
        return request_get(request)
    elif request.method == 'POST':
        return request_post(request)
    elif request.method == 'DELETE':
        return request_delete(request)
    else:
        return {
            "success": 0,
            "message": "Request Unavailable"
        }, 403
    


# ------------------------- #
#          Methods          #
# ------------------------- #

def request_get(req):
    """ Handles GET request to the "/" endpoint
    """
    # Read from database
    json_data = {}
    with open("database.json", "r") as fh:
        json_data = load(fh)
    
    # Return json data
    responseObject = {
        "success": 1,
        "message": "GET Request Recieved",
        "data": json_data
    }
    return (responseObject, 200)

    
def request_post(req):
    """ Handles POSt request to the "/" endpoint
    """
    # Verify valid key
    if ("key" not in req.args) or (req.args.get("key") != "sample_key"):
        return {
            "success": 0,
            "message": "Incorrect parameter 'key'"
        }, 403
    
    # Update database
    json_data = {}
    with open("database.json", "r") as fh:
        json_data = load(fh)
        json_data.append(req.get_json())
    with open("database.json", "w") as fh:
        dump(json_data, fh)

    # Return json data
    responseObject = {
        "success": 1,
        "message": "POST Request Recieved",
        "data": json_data
    }
    return (responseObject, 200)

    
def request_delete(req):
    """ Handles DELETE request to the "/" endpoint
    """
    # Verify valid key
    if ("key" not in req.args) or (req.args.get("key") != "sample_key"):
        return {
            "success": 0,
            "message": "Incorrect parameter 'key'"
        }, 403
    elif ("title" not in req.args):
        return {
            "success": 0,
            "message": "Parameter 'title' missing"
        }, 403
    
    # Update database
    json_data = {}
    with open("database.json", "r") as fh:
        json_data = load(fh)
        json_data = list(filter(lambda d: d["title"] != req.args.get("title"), json_data))
    with open("database.json", "w") as fh:
        dump(json_data, fh)

    # Return json data
    responseObject = {
        "success": 1,
        "message": "DELETE Request Recieved",
        "data": json_data
    }
    return (responseObject, 200)
