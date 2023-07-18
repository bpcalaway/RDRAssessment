from flask import Flask, Blueprint, request

event = Blueprint("event", __name__, template_folder="templates")

@event.route("/event", methods=["GET", "POST"])
def event_handler():
    if request.method == "POST":
        return post_event()
    elif request.method == "DELETE":
        return delete_event()
    else:
        return get_event()

def get_event():
    return "Wowzers"

def post_event():
    return "Good post friend"

def delete_event():
    return "That'll fix it"