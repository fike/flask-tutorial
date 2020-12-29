import os

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.jinja2 import Jinja2Instrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor


otele_enable = os.environ['OTELE_TRACE'] 
if otele_enable == "True":
    trace.set_tracer_provider(TracerProvider())  # pragma: no cover
    trace_exporter = jaeger.JaegerSpanExporter(  # pragma: no cover
        service_name="flask-tutorial",
        agent_host_name="jaeger-server",
        agent_port=6831,
    )
    trace.get_tracer_provider().add_span_processor(  # pragma: no cover
        BatchExportSpanProcessor(trace_exporter)
    )

__version__ = (1, 0, 0, "dev")

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    """Implement Opentelemetry"""
    FlaskInstrumentor().instrument_app(app)
    SQLAlchemyInstrumentor().instrument()
    Jinja2Instrumentor().instrument()

    # some deploy systems set the database url in the environ
    db_url = os.environ.get("DATABASE_URL")

    if db_url is None:
        # URI PostgreSQL Example
        db_url = "postgresql://flaskr:flaskr_pass@db:5432/flaskr"

    app.config.from_mapping(
        # default secret that should be overridden in environ or config
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=db_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # initialize Flask-SQLAlchemy and the init-db command
    db.init_app(app)
    migrate.init_app(app, db)

    # apply the blueprints to the app
    from flaskr import auth, blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make "index" point at "/", which is handled by "blog.index"
    app.add_url_rule("/", endpoint="index")

    return app


def init_db():
    db.drop_all()
    db.create_all()
