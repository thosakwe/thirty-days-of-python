from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <doctype html>
    <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
            Yeah...
        </body>
    </html>'''

