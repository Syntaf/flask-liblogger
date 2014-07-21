LiBlogger
=========

An on-going project to provide a simple blogging web application. LiBlogger written using Python and Flask, and is based off of miguel grinberg's mega tutorial series [here](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Warning
------------
LiBlogger is my first attempt at writing a web application in Flask and Python, it is highly recommened you do **not** use my code as a guideline for writing other websites. I am far from an expert in this area, Liblogger is designed as a learning tool for myself that I can continusouly add features to.

Installation
------------

simply run `setup.py` to have the script automaticall create a virtual enviroment for development. You must have these packages installed however:

- Python 2.7
- Python development package (`python-dev` for most Linux distributions)
- git
 
The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that.
Running
-------

To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment.

