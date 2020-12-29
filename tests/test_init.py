from flaskr import create_app
import os

def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_db_url_environ(monkeypatch):
    """Test DATABASE_URL environment variable."""
    monkeypatch.setenv("DATABASE_URL", "postgresql://flaskr:flaskr_pass@db:5432/test_flaskr")
    app = create_app()
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "postgresql://flaskr:flaskr_pass@db:5432/test_flaskr"


def test_init_db_command(runner, monkeypatch):
    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True

# def test_env_var(monkeypatch):
#     monkeypatch.setenv("OTELE_TRACE", "True")
#     otele_env_var = os.environ['OTELE_TRACE']
#     assert 'True' in otele_env_var