from flask import Flask, Blueprint, request, current_app
from sqlalchemy.orm import Session
from sqlalchemy import select
from ORMClasses.Events import Events
from json import loads


event = Blueprint("event", __name__, template_folder="templates")

@event.route("/event", methods=["GET", "POST", "DELETE"])
def event_handler():
    if request.method == "POST":
        data = request.form
        return post_event(data.get("user_id", None), data.get("title", ""), data.get("description", ""))
    elif request.method == "DELETE":
        return delete_event()
    else:
        return get_event(request.args.get("id", None))

def get_event(id: int):
    # Returns a single object with table column names, searched by its unique ID
    with Session(current_app.config["engine"]) as session:
        statement = select(Events).where(Events.id==id)
        for event in session.scalars(statement):
            return event.to_json()

def post_event(user_id: int, title=str(), description=str()):
    # Requires a user_id, other 2 args are technically optional, returns a blank status code
    with Session(current_app.config["engine"]) as session:
        new_event = Events(user_id=user_id, title=title, description=description)
        session.add(new_event)
        session.commit()
    return "Good post friend"

def delete_event():
    return "That'll fix it"