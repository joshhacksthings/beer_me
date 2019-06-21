import pytest
from beer_me import main


@pytest.fixture
def app():
    app = main.app
    app.debug = True
    return app.test_client()


def test_add_post(app):
    res = app.get("/addpost")
    assert res.status_code == 200
    assert b"<title>Add Post" in res.data

    # Posting
    data = {
        "title": "test_post_title",
        "post_text": "test_post_text"
    }
    post = app.post("/addpost", json=data)
    # Should 302, redirect to /posts
    assert post.status_code == 302


def test_view_posts(app):
    res = app.get("/posts")
    assert res.status_code == 200
    # Check above post inputs
    assert b"test_post_title" in res.data
    assert b"test_post_text" in res.data
