# mailer

Simple FastAPI service that exposes a POST `/contact` endpoint and forwards messages to `me@eademir.dev` using a Gmail account.

## Environment

Set these environment variables before running the app (use an app password for Gmail):

- `GMAIL_USER` — your Gmail address (the sender)
- `GMAIL_PASSWORD` — your Gmail password or app password

For local development you can create a `.env` file and load it (we include `python-dotenv` as a dependency):

```
GMAIL_USER=your@gmail.com
GMAIL_PASSWORD=abcd-efgh-ijkl-mnop
```

## Run

Run with uvicorn for development:

```bash
uvicorn main:app --reload
```

Example curl request:

```bash
curl -X POST http://127.0.0.1:8000/contact \
	-H "Content-Type: application/json" \
	-d '{"name":"Alice","email":"alice@example.com","subject":"Hello","message":"Hi there"}'
```

## Tests

Run pytest to execute the small unit test which mocks SMTP so no real email is sent.

```bash
pytest -q
```

## Notes

- Use a Gmail App Password if your account has 2FA (recommended). Less-secure app access is deprecated by Google.
- The endpoint validates input (email format, length limits) and returns 400 on invalid input.
