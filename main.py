from flask import Flask, render_template, Blueprint
from endpoints.event import event
from endpoints.list import event_list
from endpoints.search import event_search
from endpoints.tableHandler import create_events_table
from sqlalchemy import create_engine
import json

# We're only running locally, so we're not setting up CORS or anything.  Debug is fine for rapid dev, not being deployed
app = Flask(__name__)
app.debug = True
app.register_blueprint(event)
app.register_blueprint(event_list)
app.register_blueprint(event_search)

# Load the config from a local file, if your db is broken check this.
with open("config.json") as config_file:
    personal_data = json.load(config_file)
    app.config.update(personal_data)
    app.config["debug"] = True

# Create an engine that can be used at runtime
engine = create_engine(
    f"postgresql+psycopg2://{app.config['PSQLUsername']}:{app.config['PSQLPassword']}@localhost:{app.config['PSQLPort']}/postgres"
)
app.config["engine"] = engine
create_events_table(engine)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
    # Here, at the start of the app, recreate the events table
