from flask import Flask

app = Flask(__name__)


# Note, for production deployment, one approach is to use Talisman:
# https://github.com/GoogleCloudPlatform/flask-talisman

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
