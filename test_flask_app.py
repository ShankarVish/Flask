"""import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()


def test_ping(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi There, I'm Working"}"""


import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):  # client fixture is passed here
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi There, I'm Working"}

def test_predict(client):
    test_data = {
        "Gender": "Male",
        "Married": "Unmarried",
        "Credit_History": "Cleared Debts",
        "ApplicantIncome": 100000,
        "LoanAmount": 2000000
        }
    resp = client.post('/predict', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"Loan Approval Status": "Approved"}

