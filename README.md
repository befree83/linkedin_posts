# LinkedIn Post Generator

A terminal-based chatbot application that transforms simple user ideas into professional, highly engaging LinkedIn posts. Built with Python, it leverages the latest **OpenAI Responses API** and **Pydantic** to guarantee 100% structured JSON outputs.

## Features

- **Interactive CLI:** A user-friendly terminal interface (UI in Spanish).
- **Structured Outputs:** Uses OpenAI's `client.responses.parse()` with strict schemas to ensure consistent results.
- **Pydantic Validation:** Automatically validates the AI's response against a predefined data model (`title`, `content`, `hashtags`, `category`).
- **Robust Error Handling:** Gracefully handles API quotas (429), validation errors, safety refusals, and unexpected exceptions without crashing.
- **Scalable Architecture:** Core logic is decoupled from the CLI, making it ready to be integrated into a FastAPI backend or a Next.js/React frontend.

## Project Structure

```text
├── main.py              # Application entry point
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (API Key)
├── README.md            # Project documentation
├── models/
│   ├── __init__.py
│   └── linkedin_post.py # Pydantic model for structured output
└── core/
    ├── __init__.py
    ├── api_client.py    # OpenAI API client wrapper
    └── chatbot.py       # Chatbot business logic & error handling
