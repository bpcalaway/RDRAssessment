from flask import Flask, render_template, Blueprint
from endpoints.event import event
from endpoints.list import event_list
from endpoints.search import event_search

app = Flask(__name__)
app.register_blueprint(event)
app.register_blueprint(event_list)
app.register_blueprint(event_search)

@app.route("/")
def index():
    return render_template("index.html")

print("Starting local webservice on port 8080...")
app.run(host="localhost", port=8080)