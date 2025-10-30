from fastapi.testclient import TestClient
import os
import smtplib

from main import app

client = TestClient(app)


class DummySMTP:
    def __init__(self, host, port):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def login(self, user, pwd):
        # simulate success
        return None

    def send_message(self, msg):
        # simulate success
        return None


def test_contact_success(monkeypatch):
    # set env vars for the duration of the test
    monkeypatch.setenv("GMAIL_USER", "test@gmail.com")
    monkeypatch.setenv("GMAIL_PASSWORD", "password")
    monkeypatch.setattr(smtplib, "SMTP_SSL", DummySMTP)

    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "subject": "Hello",
        "message": "Hi there"
    }

    r = client.post("/contact", json=payload)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
