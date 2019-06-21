# Beer Me
A Flask-based app for recording the beers you've had

[![Build Status](https://travis-ci.com/joshhacksthings/beer_me.svg?branch=master)](https://travis-ci.com/joshhacksthings/beer_me)
## About
An easy-to-use log of all of the delicious beer you drink.

## Technical Set-Up

Connecting Flask app to the Object Relational Mapper, SQLAlchemy, using Flask-SQLAlchemy. This is a Flask-friendly wrapper around the SQLAlchemy package.
This wrapper will allow management of the database at a high level. Database commands can be done using classes and methods in python, instead of usual table calls in SQL.

The application will use SQLAlchemy to make calls to the PostgreSQL database.


Next, I use Flask-Migrate, a wrapper for Alembic, a database migration framework for SQLAlchemy

## Notes
