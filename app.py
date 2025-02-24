import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, and welcome to your first Flask Render app, Vikash"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render provides the PORT variable
    app.run(host='0.0.0.0', port=port)
