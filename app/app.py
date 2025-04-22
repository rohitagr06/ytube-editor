# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from routes.download import download_bp
from routes.edit import edit_bp  # Import the edit blueprint

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

# Register Blueprints with URL prefixes (optional)
app.register_blueprint(download_bp, url_prefix='/download')
app.register_blueprint(edit_bp, url_prefix='/edit')

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)