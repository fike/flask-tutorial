Flaskr
======

This a repo that use originally Flask `tutorial` with example code from Flask-SQLAlchemy project, adding Flask Migrate to use 
migrations, PostgreSQL as database. Can use a virtualenv or a container environment with Docker an Docker-Composer.

Features
-------

This project has additional features that apply in my learned:

* Profile page with profile description
* An option to change top banner color.
* A cookie based of logged user to identify what's the color banner must to show. 


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
* Add Helm chart installation