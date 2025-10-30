from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
import os
import smtplib
from email.message import EmailMessage


class Contact(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    subject: str = Field(..., min_length=1, max_length=150)
    message: str = Field(..., min_length=1, max_length=5000)


app = FastAPI()

# Configure CORS to only allow requests from eademir.dev domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://eademir.dev",
        "https://www.eademir.dev",
        "http://localhost:3000",  # for local development
        "http://localhost:5173",  # for Vite dev server
    ],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


@app.post("/contact")
def post_contact(contact: Contact):
    """Accept a contact POST from the frontend and forward it to me@eademir.dev via Gmail.

    Expects environment variables:
    - GMAIL_USER: full Gmail address used to send (e.g. your@gmail.com)
    - GMAIL_PASSWORD: app password (recommended) or account password
    """
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWORD")
    if not gmail_user or not gmail_password:
        raise HTTPException(status_code=500, detail="Mail server not configured")

    msg = EmailMessage()
    msg["From"] = gmail_user
    msg["To"] = "me@eademir.dev"
    msg["Subject"] = f"[Contact] {contact.subject}"

    body = (
        f"Name: {contact.name}\n"
        f"Email: {contact.email}\n\n"
        f"{contact.message}\n"
    )

    msg.set_content(body)

    try:
        # Use Gmail SMTP over SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(gmail_user, gmail_password)
            smtp.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        raise HTTPException(status_code=500, detail="Authentication to mail server failed")
    except smtplib.SMTPException:
        raise HTTPException(status_code=500, detail="Failed to send email")

    return {"status": "ok", "message": "Email sent"}


if __name__ == "__main__":
    # Run with: python main.py or use uvicorn for production/dev
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
