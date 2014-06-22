LiBlogger
=========

An on-going project to provide a simple blogging web application. LiBlogger written using Python and Flask, and is based off of miguel grinberg's mega tutorial series [here](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Installation
------------

simply run `setup.py` to have the script automaticall create a virtual enviroment for development. You must have these packages installed however:

- Python 2.7
- Python development package (`python-dev` for most Linux distributions)
- git
 
The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that. See the [Database tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) for the details.

Running
-------

To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment.

