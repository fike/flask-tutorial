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
* Auto-instrumentation by OpenTelemetry_

.. _OpenTelemetry: https://opentelemetry.io/

The original tutorial is here_.

.. _here: https://flask.palletsprojects.com/en/1.1.x/tutorial/

Install
-------

**You can follow original tutorial and create a virtualenv, but this version use containers to development and test**. Before to use this repo, install Docker and Docker-Compose

.. code-block:: text

    # clone the repository
    $ git clone https://github.com/fike/flask-tutorial

Run
---

For every change of model, run `make migrate` before to start this project to update Alembic migrations.

.. code-block:: text

    $ make up-db
    $ make migrate

To start just use `make up`:

.. code-block:: text
    
    $ make up


Instrumentation
---------------

To start see how instrumentation is working here, it changes **OTELE_TRACE** value to "**False**" in the Docker Compose file:

**deployments/docker-compose.yaml**

    [...]

    OTELE_TRACE=False
    
    [...]


And the terminal run:

.. code-block:: text
    
    $ make up-all


Open http://127.0.0.1:5000 in a browser to access application, go yo http://localhost:16686/ to access Jaeger UI.



Test
----

To run pytest and to know what's the test coverage runs:


.. code-block:: text

    $ make test

The coverage test report will generate in *htmlcov* directory


TODO
----

* Add remote container development
* Add Helm chart installation
* Add track based user id
* Add char limit for title post