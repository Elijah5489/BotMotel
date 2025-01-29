import os
import sys
import importlib.util

# Resolve the project directory dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
project_home = os.path.join(current_dir, 'Gitchfork/BotMotel')

# Add the project directory to the sys.path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate the virtual environment dynamically
activate_this = os.path.join(current_dir, '.virtualenvs/myenv/bin/activate_this.py')
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

# Load the Flask app from BotMotel.py
file_path = os.path.join(project_home, 'BotMotel.py')
spec = importlib.util.spec_from_file_location("BotMotel", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["BotMotel"] = module
spec.loader.exec_module(module)

app = module.app  # Assuming 'app' is the Flask app object

# Run the app using the built-in WSGI server
if __name__ == "__main__":
    app.run()
