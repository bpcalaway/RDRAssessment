from flask import Flask, Blueprint, request

event_search = Blueprint("search", __name__, template_folder="templates")


@event_search.route("/search", methods=["GET"])
def search():
    return "This is going to take a little longer, unless we lazy partial match or something"
