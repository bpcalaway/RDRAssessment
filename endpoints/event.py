from flask import Flask, Blueprint, request, current_app
from sqlalchemy.orm import Session
from sqlalchemy import select
from ORMClasses.Events import Events


event = Blueprint("event", __name__, template_folder="templates")


@event.route("/event", methods=["GET", "POST", "DELETE"])
def event_handler():
    # We're using a standard endpoint, handled by request type
    if request.method == "POST":
        data = dict(request.form)
        return post_event(
            data.get("user_id", None),
            data.get("title", ""),
            data.get("description", ""),
        )
    elif request.method == "DELETE":
        data = dict(request.form)
        return delete_event(data.get("id"))
    else:
        return get_event(request.args.get("id", None))


def get_event(id: int):
    # Returns a single object with table column names, searched by its unique ID
    with Session(current_app.config["engine"]) as session:
        statement = select(Events).where(Events.id == id)
        for event in session.scalars(statement):
            return event.to_json()


def post_event(user_id: int, title=str(), description=str()):
    # Requires a user_id, other 2 args are technically optional, returns a blank status code
    with Session(current_app.config["engine"]) as session:
        new_event = Events(user_id=user_id, title=title, description=description)
        session.add(new_event)
        session.commit()
    return "Success", 200, {"Content-Type": "text/plain"}


def delete_event(id: int):
    # Delete an event by its unique identifier, in a real example there would also be an ownership check
    with Session(current_app.config["engine"]) as session:
        statement = select(Events).where(Events.id == id)
        # offshot you've somehow violated a key constraint
        for event in session.scalars(statement):
            session.delete(event)
        session.commit()
    return "Success", 200, {"Content-Type": "text/plain"}
