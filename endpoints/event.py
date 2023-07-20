from flask import Flask, Blueprint, request, current_app
from sqlalchemy.orm import Session, Mapped
import pandas as pd


event = Blueprint("event", __name__, template_folder="templates")

class Events:
    __table_name__ = "events"

    id: Mapped[int]
    user_id: Mapped[int]
    title: Mapped[str]
    description: Mapped[str]

    def __repr__(self) -> str:
        return f"Event(id={self.id!r}, user_id={self.user_id!r}, title={self.title!r}, description={self.description!r})"

@event.route("/event", methods=["GET", "POST"])
def event_handler():
    if request.method == "POST":
        return post_event()
    elif request.method == "DELETE":
        return delete_event()
    else:
        return get_event()

def get_event():
    statement = "Select * from events;"
    df = pd.read_sql(statement, con=current_app.config["engine"])
    return df.to_json()

def post_event():
    return "Good post friend"

def delete_event():
    return "That'll fix it"