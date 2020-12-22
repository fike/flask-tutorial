import pytest
from flask import g
from flask import session

from flaskr import db
from flaskr.auth.models import User


def test_register(client, app):
    # test that viewing the page renders without template errors
    assert client.get("/auth/register").status_code == 200

    # test that successful registration redirects to the login page
    response = client.post("/auth/register", data={"username": "a", "password": "a", "profile": "a user profile", "bgcolor": "ligthgray"})
    assert "http://localhost/auth/login" == response.headers["Location"]

    # test that the user was inserted into the database
    with app.app_context():
        assert User.query.filter_by(username="a").first() is not None


def test_user_password(app):
    user = User(username="a", password="a")
    assert user.password != "a"
    assert user.check_password("a")


@pytest.mark.parametrize(
    ("username", "password", "profile", "bgcolor", "message"),
    (
        ("", "", "", "", b"Username is required."),
        ("a", "", "", "", b"Password is required."),
        ("a", "a", "", "", b"Profile is required."),
        ("test", "test", "test user profile", "ligthgray", b"already registered"),
        ("other", "test1", "other user profile", "ligthgray", b"already registered"),
    ),
)
def test_register_validate_input(client, username, password, profile, bgcolor, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password, "profile": profile, "bgcolor": bgcolor}
    )
    assert message in response.data


def test_login(client, auth):
    # test that viewing the page renders without template errors
    assert client.get("/auth/login").status_code == 200

    # test that successful login redirects to the index page
    response = auth.login()
    assert response.headers["Location"] == "http://localhost/"

    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user.username == "test"


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "test", b"Incorrect username."), ("test", "a", b"Incorrect password.")),
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session


def test_profile_required(app, client, auth):
    auth.login()
    # current user can't see other user's profile
    assert client.get("/auth/2/profile").status_code == 403


def test_profile_update(client, auth, app):
    auth.login()
    assert client.get("/auth/1/profile").status_code == 200
    client.post("/auth/1/profile", data={"username": "a", "profile": "b", "bgcolor": "yellow"})

    with app.app_context():
        assert User.query.get(1).profile == "b"
        assert User.query.get(1).bgcolor == "yellow"
