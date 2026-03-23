import os
from bot.telegram_handler import run_bot

def main():
    os.makedirs("logs", exist_ok=True)
    run_bot()

if __name__ == "__main__":
    main()
