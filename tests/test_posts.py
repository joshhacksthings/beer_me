import os
import pytest
import tempfile
from beer_me import main


@pytest.fixture
def app():
    db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
    main.app.config['TESTING'] = True
    client = main.app.test_client()

    with main.app.app_context():
        main.db.create_all()

    yield client

    os.close(db_fd)
    os.unlink(main.app.config['DATABASE'])


def test_add_post(app):
    res = app.get("/addpost")
    assert res.status_code == 200
    assert b"<title>Add Post" in res.data

    from random import randint
    rand = randint(0, 10000)
    # Posting
    data = dict(
        title="test_title_{}".format(rand),
        post_text="test_text_3"
    )
    post = app.post("/addpost", data=data)
    # Should 302, redirect to /posts
    assert post.status_code == 302


def test_view_posts(app):
    res = app.get("/posts")
    assert res.status_code == 200
    # Check above post inputs
    assert b"test_title" in res.data
    assert b"test_text" in res.data
