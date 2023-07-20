from flask import Flask, Blueprint, request, current_app
from sqlalchemy import Table, Column, Integer, String, MetaData
from ORMClasses.Events import Events
from sqlalchemy.ext.declarative import declarative_base


# Every time we start the app, drop the table for events and recreate it.
def create_events_table(engine):
    # Recreate the table
    meta = MetaData()
    events = Table(
        "events",
        meta,
        Column("id", Integer, primary_key=True),
        Column("user_id", Integer),
        Column("title", String),
        Column("description", String),
    )

    Base = declarative_base()
    Base.metadata.drop_all(bind=engine, tables=[events])

    return meta.create_all(engine)
