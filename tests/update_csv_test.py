"""csv"""
import os
from flask_login import FlaskLoginClient
from app import db
from app.db.models import User
from app.auth.forms import csv_upload

def test_upload_csv(application):
    """upload"""
    application.test_client_class = FlaskLoginClient
    user = User('keith@webizly.com', 'testtest', is_admin=True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'keith@webizly.com'
    assert db.session.query(User).count() == 1

    root = os.path.dirname(os.path.abspath(__file__))
    transaction_csv = os.path.join(root, '../uploads/transactions.csv')

    with application.test_client(user = user) as client:
        # logged in
        response = client.get('/transactions/upload')
        assert response.status_code == 200
        form = csv_upload()
        form.file = transaction_csv
        assert form.validate

def test_upload_csv_denied(application):
    """Denied up"""
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0
    with application.test_client(user = None) as clients:
        # This request already has a user logged in.
        response = clients.get('/transactions/upload')
        assert response.status_code == 302
