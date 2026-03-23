import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_USER_ID = int(os.getenv("TELEGRAM_USER_ID", "0"))

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    DEFAULT_AI_PROVIDER = os.getenv("DEFAULT_AI_PROVIDER", "openai")

    BASE_DIR = os.path.expanduser("~/ai_projects")
