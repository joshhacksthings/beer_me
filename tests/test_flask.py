import pytest
from beer_me import main


@pytest.fixture
def app():
    app = main.app
    app.debug = True
    return app.test_client()


def test_hello_world(app):
    res = app.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Hello World" in res.data


def test_some_id(app):
    res = app.get("/foo/12345")
    assert res.status_code == 200
    assert b"12345" in res.data


def test_beer_form(app):
    res = app.get("/form")
    print(res.status_code)
    assert res.status_code == 200
    assert b"<h1>Beer Data Form" in res.data


def test_beer_response(app):
    res = app.get("/ratebeer")
    print(res.status_code)
    assert res.status_code == 200
    assert b"<h1>Beer-Data Details" in res.data
