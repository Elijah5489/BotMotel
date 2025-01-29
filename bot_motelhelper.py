import importlib.util
import sys
from flask import Flask

file_path = 'C:/code/botmotel/BotMotel.py'
spec = importlib.util.spec_from_file_location("botmotel", file_path)
bot_motel = importlib.util.module_from_spec(spec)
sys.modules["botmotel"] = bot_motel
spec.loader.exec_module(bot_motel)

app = bot_motel.app

if __name__ == "__main__":
    app.run()
    