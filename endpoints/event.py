from flask import Flask, Blueprint, request, current_app
from sqlalchemy.orm import Session
from sqlalchemy import select
from ORMClasses.Events import Events
import pandas as pd


event = Blueprint("event", __name__, template_folder="templates")

@event.route("/event", methods=["GET", "POST", "DELETE"])
def event_handler():
    if request.method == "POST":
        return post_event()
    elif request.method == "DELETE":
        return delete_event()
    else:
        return get_event(request.args.get("id", None))

def get_event(id: int):
    with Session(current_app.config["engine"]) as session:
        statement = select(Events).where(Events.id==id)
        for event in session.scalars(statement):
            return event.to_json()
    #df = pd.read_sql(statement, con=current_app.config["engine"])
    #return df.to_json()

def post_event():
    return "Good post friend"

def delete_event():
    return "That'll fix it"