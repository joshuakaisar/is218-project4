"""configuration"""
# pylint: disable=redefined-outer-name
import os
import pytest
from app import create_app, User
from app.db import db

@pytest.fixture()
def application():
    """app"""
    os.environ['FLASK_ENV'] = 'testing'

    application = create_app()

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()

@pytest.fixture()
def add_user(application):
    """user"""
    with application.app_context():
        #new record
        user = User('keith@webizly.com', 'testtest', True)
        db.session.add(user)
        db.session.commit()

@pytest.fixture()
def client(application):
    """client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """task"""
    return application.test_cli_runner()
