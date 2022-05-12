"""signing"""
import logging
from app.auth.forms import login_form, register_form

def test_user_login(application):
    """old user"""
    log = logging.getLogger("myApp")
    log.info("user login test")
    with application.test_request_context():
        form = login_form()
        form.email.data = "keith@webizly.com"
        form.password.data = "testtest"
        assert form.validate


def test_user_register(application):
    """new"""
    log = logging.getLogger("myApp")
    log.info("user register test")
    with application.test_request_context():
        form = register_form()
        form.email.data = "keith@webizly.com"
        form.password.data = "testtest"
        form.confirm.data = "testtest"
        assert form.validate
