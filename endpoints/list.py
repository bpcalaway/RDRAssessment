from flask import Flask, Blueprint, request, current_app
from sqlalchemy.orm import Session
from sqlalchemy import select
from ORMClasses.Events import Events

event_list = Blueprint("list", __name__, template_folder="templates")

@event_list.route("/list", methods=["GET"])
def event_handler():
    # Return a list of objects with table columns as arguments
    user_id = request.args.get("user_id", None)
    with Session(current_app.config["engine"]) as session:
        statement = select(Events).where(Events.user_id==user_id)
        all_events = list()
        for event in session.scalars(statement):
                all_events.append(event.to_json())
        return all_events

    return "full list by user_id goes here"