from flask import Flask, Blueprint, request

event_list = Blueprint("list", __name__, template_folder="templates")

@event_list.route("/list", methods=["GET"])
def event_handler():
    return "full list by user_id goes here"