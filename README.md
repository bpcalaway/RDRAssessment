# RDRAssessment
Homework for VMC

[Initial]
- Assumptions:
    - Modern Python 3 installation
    - Postgres is installed and set up
    - pip is available and basic modules can be installed by tox
- If any of these are not available, links can be found below:
    - pip: https://pip.pypa.io/en/stable/installation/
    - postgres: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

[Description]
- This is a flask application that has one standard endpoint, located at localhost:8080/ that will describe some of the architecture
    - These endpoints listed on the index page and their acceptable endpoints will also be listed here:
        -/event [get/post/delete]
            -GET: Takes an id in query arguments, returns the data of the entry as a json compliant dictionary object
            -POST: Accepts data objects that MUST contain a user_id, with optional arguments for title and description.  returns a status code
            -DELETE: Accepts a data object with an id argument and removes it from the database
        -/list GET: takes a user_id query argument and returns a list of objects that matches those ids
        -/search GET: takes a keyword query argument and attempts to partial match titles
    - The 'events' table that is used in the database is described in the setup.sql file, which is not used.  Everything in the app uses the sqlalchemy orm layer, and importantly it will reset the table every time you reload the app for testing purposes
    - config.json is an important file that must be filled out with postgres login information to allow the app to communicate with the postgres database that has been installed.
    - Once you have a running version of the application, you can use the test files that are in the examples folder

[Commands]
# This is how we will manage our environment
- python -m pip install tox
- <Fill out config.json here>
# Main will install required packages and try to start the application and connect to the db
- python -m tox -e main
# Once this is up and running, you can query the endpoints.  I have a preset for that in tox you can use in a separate terminal with:
- python -m tox -e test

[Config]
- Users will need to view the config.json file and edit their personal details from when they set up postgres on their local machine, loading up postgres in a shell should allow users to verify they have the correct information.