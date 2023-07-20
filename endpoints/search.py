from flask import Flask, Blueprint, request, current_app
from sqlalchemy.orm import Session
from sqlalchemy import select
from ORMClasses.Events import Events

event_search = Blueprint("search", __name__, template_folder="templates")


@event_search.route("/search", methods=["GET"])
def search():
    # Returns a list of objects with partial title matches
    keyword = request.args.get("keyword")
    with Session(current_app.config["engine"]) as session:
        statement = select(Events).where(Events.title.contains(keyword))
        all_events = list()
        for event in session.scalars(statement):
            all_events.append(event.to_json())
    return all_events
