[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffike%2Fflask-tutorial.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffike%2Fflask-tutorial?ref=badge_shield)

Flaskr
======

This a repo that use originally Flask `tutorial` with example code from Flask-SQLAlchemy project, adding Flask Migrate to use 
migrations, PostgreSQL as database. Can use a virtualenv or a container environment with Docker an Docker-Composer


the original tutorial is:

.. _tutorial: http://flask.pocoo.org/docs/tutorial/


Install
-------

**You can follow original tutorial and create a virtualenv, but this version use containers to development and test**. Before to use this repo, install Docker and Docker-Compose

.. code-block:: text

    # clone the repository
    $ git clone https://github.com/fike/flask-tutorial

Run
---

For every change of model, run `make migrate` to update Alembic migrations.

.. code-block:: text

    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    $ make up-db
    $ make migrate

Run using Docker and Docker-Compose

.. code-block:: text
    # make up

Open http://127.0.0.1:5000 in a browser.

Test
----

.. code-block:: text

    $ make test

Coverage report will generate in *htmlcov* directory


TODO
----

* Add remote container development
* Add cookie session 
* Add cookie for change color theme

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffike%2Fflask-tutorial.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffike%2Fflask-tutorial?ref=badge_large)